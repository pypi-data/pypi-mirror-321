from unittest import TestCase
import cv2
from cams_ilvo_utils.calib.calibration import IntrinsicCalib, ExtrinsicCalib
from cams_ilvo_utils.img.image import Image, project_mm_to_px, project_px_to_mm
from os import path
import numpy as np
import pandas as pd


def project_px_to_mm_original(calib_extrinsic: ExtrinsicCalib, calib_intrinsic: IntrinsicCalib, image_coords_px, z_mm=0):
    """
    Converts plate coordinates (in mm) to img coordinates (in pixel)
    :param calib_extrinsic:
    :param calib_intrinsic:
    :param image_coords_px: object points in plate coordinates (in mm)
    :return: pixel coordinates
    """
    r = []
    if len(image_coords_px) > 0:
        mtx = calib_intrinsic['mtx']
        rvec = calib_extrinsic['rvec']
        tvec = calib_extrinsic['tvec']
        Lcam = mtx.dot(np.hstack((cv2.Rodrigues(rvec)[0], tvec)))
        for image_coord_px in image_coords_px:
            px, py = image_coord_px[:2]
            X = (np.linalg.inv(np.hstack((Lcam[:, 0:2], np.array([[-1 * px], [-1 * py], [-1]])))).
                 dot((-z_mm * Lcam[:, 2] - Lcam[:, 3])))
            X[2] = z_mm
            r.append(X)
    return r


def get_mask_contours(im_extrinsic, df_mask_rough):
    # Read in images

    mask_rough = np.zeros(im_extrinsic.shape[:2], dtype=np.uint8)
    cv2.drawContours(mask_rough, [df_mask_rough.to_numpy()], -1, (255, 255, 255), -1)

    im_extrinsic_masked = cv2.bitwise_and(im_extrinsic, im_extrinsic, mask=mask_rough)

    maks_inverted = 255 - mask_rough
    maks_inverted = np.stack((maks_inverted,) * 3, axis=-1)
    im_extrinsic_masked = im_extrinsic_masked + maks_inverted

    # Define the black color range with broader values
    lower_black = np.array([0, 0, 0])
    upper_black = np.array([100, 100, 100])

    # Create a binary mask where green colors are in range
    mask_black = cv2.inRange(im_extrinsic_masked, lower_black, upper_black)

    # Perform morphological operations to remove noise and fill gaps
    kernel = np.ones((5, 5), np.uint8)
    mask_black = cv2.morphologyEx(mask_black, cv2.MORPH_CLOSE, kernel, iterations=1)
    mask_black = cv2.morphologyEx(mask_black, cv2.MORPH_OPEN, kernel, iterations=1)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask_black, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return contours


class TestCameraDaheng(TestCase):
    def test_original_vs_new_px_to_mm(self):
        extrinsic_calib = ExtrinsicCalib("files/project_camera/extrinsic.json")
        intrinsic_calib = IntrinsicCalib("files/project_camera/intrinsic.json")
        extrinsic_image = Image(cv2.imread(
            "files/project_camera/extrinsic.png")).undistort(intrinsic_calib).im
        df_mask_rough = pd.read_csv("files/project_camera/mask-rough.csv")

        contours = get_mask_contours(extrinsic_image, df_mask_rough)
        contour = contours[0].squeeze(axis=1)

        coords_original = np.array(project_px_to_mm_original(extrinsic_calib, intrinsic_calib, contour))
        coords_new = np.array(project_px_to_mm(extrinsic_calib, intrinsic_calib, contour)).squeeze()

        difference = np.abs(coords_original - coords_new)
        self.assertTrue(np.allclose(difference, 0, atol=1), "Original and new implementation do not match")

