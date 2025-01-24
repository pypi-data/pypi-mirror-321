from unittest import TestCase
from cams_ilvo_utils.img.image import Image, cv_to_np
from cams_ilvo_utils.calib.calibration import IntrinsicCalib, ExtrinsicCalib, WhiteBalanceCalib
from copy import deepcopy
import numpy as np
import cv2


class TestImage(TestCase):
    def test_undistort(self):
        calib = IntrinsicCalib("files/checker_board/intrinsic/intrinsic.json")

        cv_im = cv2.imread("files/checker_board/intrinsic/img/1.jpg")
        im = Image(cv_to_np(cv_im))

        window_name = "Display"
        cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
        im.undistort(calib).show()
        cv2.waitKey(-1)

        cv2.destroyAllWindows()

    def test_project(self):
        calib_intrinsic = IntrinsicCalib("files/checker_board/intrinsic/intrinsic.json")
        calib_extrinsic = ExtrinsicCalib("files/checker_board/extrinsic/extrinsic.json")

        cv_im = cv2.imread("files/checker_board/extrinsic/img/1.jpg")
        im = Image(cv_to_np(cv_im))

        centers_mm_orig = [[0, 0, 0], [130.0, 0.0, 0.0], [0.0, 146.25, 0.0]]
        objpoints = np.array(centers_mm_orig)

        window_name = "Display"
        cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

        centers_px = im.undistort(calib_intrinsic).project_mm_to_px(calib_extrinsic, calib_intrinsic, objpoints)
        centers_mm = im.project_px_to_mm(calib_extrinsic, calib_intrinsic, centers_px)
        print(centers_mm_orig, centers_px, centers_mm)
        im.show()
        cv2.waitKey(-1)

        cv2.destroyAllWindows()

    def test_calib_white(self):
        calib_intrinsic = IntrinsicCalib("files/white_balance/intrinsic/intrinsic.json")
        calib_white = WhiteBalanceCalib("files/white_balance/white_balance.png")

        cv_im = cv2.imread("files/white_balance/1.png")
        im = Image(cv_to_np(cv_im))
        im_square = Image(cv_to_np(cv_im)).square()

        window_name = "Display"
        window_name_square = "Display Square"

        cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
        cv2.namedWindow(window_name_square, cv2.WINDOW_NORMAL)

        im_show = np.hstack([im.get(), im.calib_white(calib_white, calib_intrinsic).get()])
        im_show_square = np.hstack([im_square.get(), im_square.calib_white(calib_white, calib_intrinsic).get()])

        cv2.imshow(window_name, im_show)
        cv2.imshow(window_name_square, im_show_square)

        cv2.waitKey(-1)
        cv2.destroyAllWindows()

        self.assertEqual(im.get().shape[:2], (1200, 1600))
        self.assertEqual(im_square.get().shape[:2], (1200, 1200))

    def test_square(self):
        cv_im = cv2.imread("files/white_balance/1.png")
        im = Image(cv_to_np(cv_im))
        _, orig_w_px, _ = im.get().shape
        im_square = Image(cv_to_np(cv_im)).square()

        im_unsquare = deepcopy(im_square)
        im_unsquare.unsquare(orig_w_px)

        window_name = "Image squarification"

        cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
        im_show = np.hstack([im.get(), im_square.get(), im_unsquare.get()])
        cv2.imshow(window_name, im_show)

        cv2.waitKey(-1)

        self.assertEqual(im.get().shape, im_unsquare.get().shape)
        self.assertTrue(im_square.squared)
        self.assertFalse(im_unsquare.squared)
