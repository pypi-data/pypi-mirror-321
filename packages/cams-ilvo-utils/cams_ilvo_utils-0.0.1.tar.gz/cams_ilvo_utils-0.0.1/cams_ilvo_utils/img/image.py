from enum import Enum
import cv2
import numpy as np
from copy import deepcopy
from cams_ilvo_utils.calib.calibration import IntrinsicCalib, ExtrinsicCalib, WhiteBalanceCalib


def cv_to_np(cv_im):
    return np.array(cv2.cvtColor(cv_im, cv2.COLOR_BGR2RGB))


def square(im):
    orig_px_h, orig_px_w = im.shape[:2]
    color_im = (len(im.shape) == 3)

    # make rectangular
    px_offset = int((orig_px_w - orig_px_h) / 2)
    if color_im:
        return im[:, px_offset:px_offset + orig_px_h, :]
    else:
        return im[:, px_offset:px_offset + orig_px_h]


def unsquare(im, new_px_width):
    orig_px_h, orig_px_w = im.shape[:2]
    color_im = (len(im.shape) == 3)

    px_offset = int((new_px_width - orig_px_w) / 2)
    if color_im:
        new_im = np.zeros((orig_px_h, new_px_width, 3)).astype(np.uint8)
        new_im[:, px_offset:px_offset + orig_px_w, :] = im
        return new_im
    else:
        new_im = np.zeros((orig_px_h, new_px_width)).astype(np.uint8)
        new_im[:, px_offset:px_offset + orig_px_w] = im
        return new_im


def undistort(im, intrinsic_calib: IntrinsicCalib, crop=False):
    h, w = im.shape[:2]
    new_camera_mtx, roi = cv2.getOptimalNewCameraMatrix(intrinsic_calib['mtx'], intrinsic_calib['dist'], (w, h), 1,
                                                        (w, h))
    im = cv2.undistort(im, intrinsic_calib['mtx'], intrinsic_calib['dist'], None, new_camera_mtx)
    if crop:
        # crop the img
        x, y, w, h = roi
        im = im[y:y + h, x:x + w]

    return im


def correct_white(im, calib_im, cst=50):
    c_im = deepcopy(calib_im)
    c_im[c_im <= 0] = 1
    b = np.multiply(np.divide(im[:, :, 0], c_im), cst)
    b = b.astype(np.uint8)
    g = np.multiply(np.divide(im[:, :, 1], c_im), cst)
    g = g.astype(np.uint8)
    r = np.multiply(np.divide(im[:, :, 2], c_im), cst)
    r = r.astype(np.uint8)
    return cv2.merge((b, g, r))


def project_mm_to_px(calib_extrinsic: ExtrinsicCalib, calib_intrinsic: IntrinsicCalib, plate_coords_mm):
    """
    Converts plate coordinates (in mm) to img coordinates (in pixel)
    :param calib_extrinsic:
    :param calib_intrinsic:
    :param plate_coords_mm: object points in plate coordinates (in mm)
    :return: pixel coordinates
    """
    # Old implementation
    # r = []
    # if len(objpoints_mm) > 0:
    #     impoints, _ = cv2.projectPoints(objpoints_mm, calib_extrinsic['rvec'], calib_extrinsic['tvec'],
    #                                     calib_intrinsic['mtx'], calib_intrinsic['dist'])
    #     impoints = impoints.astype(int)
    #     r = [p[0] for p in impoints]
    #
    # return r

    K = calib_intrinsic['mtx']
    R, _ = cv2.Rodrigues(calib_extrinsic['rvec'])
    t = calib_extrinsic['tvec']
    dist = calib_intrinsic['dist']

    obj_points_3D = np.array(plate_coords_mm, dtype=np.float32)
    obj_points_3D = obj_points_3D[:, :3]
    im_coords, _ = cv2.projectPoints(obj_points_3D, R, t, K, dist)
    im_coords = im_coords.squeeze()
    return im_coords.round().astype(int)


def project_px_to_mm(calib_extrinsic: ExtrinsicCalib, calib_intrinsic: IntrinsicCalib, image_coords_px, z_mm=0.0):
    """
    converts img coordinates (in pixel) to plate coordinates (in mm)
    :param calib_extrinsic:
    :param calib_intrinsic:
    :param image_coords_px: img points (in pixel)
    :param z_mm: height of point in respect to the plate (in mm)
    :return: plate coordinates (in mm)
    """
    # Old implementation
    # r = []
    # if len(impoints_px) > 0:
    #     mtx = calib_intrinsic['mtx']
    #     rvec = calib_extrinsic['rvec']
    #     tvec = calib_extrinsic['tvec']
    #     Lcam = mtx.dot(np.hstack((cv2.Rodrigues(rvec)[0], tvec)))
    #     for impoint_px in impoints_px:
    #         px, py = impoint_px
    #         X = (np.linalg.inv(np.hstack((Lcam[:, 0:2], np.array([[-1 * px], [-1 * py], [-1]])))).
    #              dot((-z_mm * Lcam[:, 2] - Lcam[:, 3])))
    #         r.append(X)
    # return r
    K = calib_intrinsic['mtx']
    R, _ = cv2.Rodrigues(calib_extrinsic['rvec'])
    t = calib_extrinsic['tvec']

    mm_coords = []
    for image_coord in image_coords_px:
        image_coord = np.append(image_coord, 1)
        leftSideMat = np.matmul(np.matmul(np.linalg.inv(R), np.linalg.inv(K)), image_coord.reshape(3, 1))
        rightSideMat = np.matmul(np.linalg.inv(R), t)
        # derde rij extraheren voor s factor:
        s = (z_mm + rightSideMat[2, 0]) / leftSideMat[2, 0]
        mm_coords.append(np.matmul(np.linalg.inv(R), (s * np.matmul(np.linalg.inv(K), image_coord.reshape(3, 1)) - t)))
    return mm_coords


def project_coordinate_system(cv_image, calib_extrinsic: ExtrinsicCalib, calib_intrinsic: IntrinsicCalib):
    """
    :param cv_image: cv img (reference will be altered)
    :param calib_extrinsic:
    :param calib_intrinsic:
    :return:
    """
    objpoints = np.array([[0, 0, 0], [100.0, 0.0, 0.0], [0.0, 100.0, 0.0], [0.0, 0.0, 100.0]])
    impoints, _ = cv2.projectPoints(objpoints, calib_extrinsic['rvec'], calib_extrinsic['tvec'],
                                    calib_intrinsic['mtx'], calib_intrinsic['dist'])
    impoints = impoints.astype(int)
    center = impoints[0][0]
    x_end = impoints[1][0]
    y_end = impoints[2][0]
    z_end = impoints[3][0]

    cv2.arrowedLine(cv_image, center, x_end, (0, 0, 255), 5)
    cv2.arrowedLine(cv_image, center, y_end, (0, 255, 0), 5)
    cv2.arrowedLine(cv_image, center, z_end, (255, 0, 0), 5)


class ImageType(Enum):
    COLOR = 0
    MONO = 1


class Image:
    def __init__(self, np_array, im_type: ImageType = ImageType.COLOR):
        if im_type == ImageType.COLOR:
            self.im = cv2.cvtColor(np_array, cv2.COLOR_RGB2BGR)
        elif im_type == ImageType.MONO:
            self.im = cv2.cvtColor(np_array, cv2.COLOR_GRAY2BGR)

        self.undistorted = False
        self.squared = False

    @staticmethod
    def load(im_path):
        cv_im = cv2.imread(im_path)
        return Image(cv_to_np(cv_im))

    def show(self, window="Display",delay=10):
        cv2.imshow(window, self.im)
        cv2.waitKey(delay)
    def save(self, im_path):
        cv2.imwrite(im_path, self.im)

    def get(self):
        return self.im

    def set(self, new_im):
        self.im = new_im

    def undistort(self, calib: IntrinsicCalib, crop=False):
        if not self.undistorted:
            self.im = undistort(self.im, calib, crop)
            self.undistorted = True

        return self

    def calib_white(self, calib_white: WhiteBalanceCalib, calib_intrinsics: IntrinsicCalib, const_factor=55):
        if not self.undistorted:
            self.undistort(calib_intrinsics)

        calib_im = undistort(deepcopy(calib_white.im), calib_intrinsics, False)
        if self.squared:
            calib_im = square(calib_im)
        self.im = correct_white(self.im, calib_im, const_factor)

        return self

    def square(self):
        if not self.squared:
            self.im = square(self.im)
            self.squared = True

        return self

    def unsquare(self, new_width_px):
        if self.squared:
            self.im = unsquare(self.im, new_width_px)
            self.squared = False

        return self

    def project_mm_to_px(self, calib_extrinsic: ExtrinsicCalib, calib_intrinsic: IntrinsicCalib, objpoints_mm):
        centers = project_mm_to_px(calib_extrinsic, calib_intrinsic, objpoints_mm)
        i = 0
        for center in centers:
            markerSize = 15
            thickness = 2
            cv2.drawMarker(self.im, center, (0, 255, 0), cv2.MARKER_CROSS, markerSize, thickness)
            cv2.circle(self.im, center, 100, (0, 0, 255), 5)
            i += 1
        return centers

    def project_px_to_mm(self, calib_extrinsic: ExtrinsicCalib, calib_intrinsic: IntrinsicCalib, impoints_px, z_mm=0.0):
        centers = project_px_to_mm(calib_extrinsic, calib_intrinsic, impoints_px, z_mm)
        return centers

    def display(self, text, origin):
        cv2.putText(self.im, text, origin, cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
        return self

    def project_coordinate_system(self, calib_extrinsic: ExtrinsicCalib, calib_intrinsic: IntrinsicCalib):
        # alters the reference
        project_coordinate_system(self.im, calib_extrinsic, calib_intrinsic)

        return self
