from cams_ilvo_utils.calib.board import CalibrationBoard
from cams_ilvo_utils.calib.calibration import IntrinsicCalib, ExtrinsicCalib, WhiteBalanceCalib
from cams_ilvo_utils.img.image import Image
from cams_ilvo_utils.img.image import project_coordinate_system

from abc import ABC, abstractmethod
import cv2
import numpy as np
import glob
import math
from itertools import chain
from datetime import datetime
from os import path, makedirs


class CalibrationProcess(ABC):
    def __init__(self, calibration_board: CalibrationBoard, calib_dir, calib_type):
        self._calibration_board = calibration_board
        self.calibration = None
        self.calib_dir = ""
        self.num_frames = 0
        self.calib_type = calib_type
        # im names
        self.image_names = []
        self.cv_image = None
        # termination criteria
        self._criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
        self._blob_detector_params = cv2.SimpleBlobDetector_Params()  # min threshold, max threshold, min area, max Area, min intertia, min circularity, min distance between blobs
        self._blob_detector_params.minThreshold = 1
        self._blob_detector_params.maxThreshold = 255
        self._blob_detector_params.filterByArea = True
        self._blob_detector_params.minArea = 1000
        self._blob_detector_params.maxArea = 60000
        self._blob_detector_params.filterByInertia = True
        self._blob_detector_params.minInertiaRatio = 0.5
        self._blob_detector_params.filterByCircularity = True
        self._blob_detector_params.minCircularity = 0.8
        self._blob_detector_params.minDistBetweenBlobs = 7
        # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
        self._objp = np.zeros((self._calibration_board.width * self._calibration_board.height, 3), np.float32)
        self._objp[:, :2] = np.mgrid[0:self._calibration_board.height, 0:self._calibration_board.width].T.reshape(-1, 2)
        self._objp[:, 0] *= self._calibration_board.pattern_size_mm_height
        self._objp[:, 1] *= self._calibration_board.pattern_size_mm_width
        print("Printing _objp matrix:")
        for row in self._objp:
            print(f"{row[0]:.2f}\t{row[1]:.2f}\t{row[2]:.2f}")
        # Arrays to store object points and img points from all the images.
        self._objpoints = []  # 3d point in real world space
        self._imgpoints = []  # 2d points in img plane.
        # Create directory tree
        self.create_directory_tree(calib_dir)

    @abstractmethod
    def prepare_image(self, img) -> Image:
        pass

    @abstractmethod
    def process_chess_board(self, corners, gray, img, ret):
        pass

    @abstractmethod
    def calculate_result(self, cv_image):
        pass

    @abstractmethod
    def create_directory_tree(self, calib_dir):
        pass

    @abstractmethod
    def show(self):
        pass

    def find_pattern(self, cv_image):
        cv_gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)

        ret = 0
        corners = []
        if self._calibration_board.pattern_type == "checker_board":
            ret, corners = cv2.findChessboardCorners(cv_gray, self._calibration_board.dimension(), None)
        # If found, add object points, img points (after refining them)
        elif self._calibration_board.pattern_type == "circle_board":
            params = self._blob_detector_params
            detector = cv2.SimpleBlobDetector_create(params)
            ret, corners = cv2.findCirclesGrid(cv_gray, self._calibration_board.dimension(), None,
                                               cv2.CALIB_CB_SYMMETRIC_GRID + cv2.CALIB_CB_CLUSTERING, detector)

        if ret:
            self.process_chess_board(corners, cv_gray, cv_image, ret)
            self.num_frames += 1
        else:
            print(f"Searching for a {self._calibration_board.dimension()} {self._calibration_board.pattern_type} "
                  f"calibration board pattern. Did not find any checker board with this pattern. Make sure you count "
                  f"the inner corners to get the current checker board dimension")
        return ret

    def calibrate_using_camera(self, cam):
        window_name = "Camera Calibration"
        cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
        print("-- Started calibration process")
        cam.start_acquisition()

        print("Press 'q' to terminate the calibration process, 's' to save intermediately "
              "and ' ' to capture an img.")

        key = None

        while 1:
            cam_img = cam.get_image()
            if not cam_img:
                continue

            img = self.prepare_image(cam_img)
            cv_image = img.get().copy()

            wait_time_ms = 10
            if key == ord(' '):  # only save when key is ' '
                # Find the pattern
                ret = self.find_pattern(cv_image)
                if ret:
                    # save img (do this first otherwise checkerboard is drawn on saved img)
                    im_path = path.join(self.calib_dir, 'img', f"{self.num_frames}.jpg")
                    self.image_names.append(im_path)
                    print(f"Saving {self.num_frames}'th calibration img to '{im_path}'")
                    img.save(im_path)
                    # wait for visualization
                    wait_time_ms = 2000  # To visualize pattern layout wait for 2 secs when pattern is found!

            cv2.imshow(window_name, img.get())
            key = cv2.waitKey(wait_time_ms)

            if key == ord('q'):
                self.calculate_result(cv_image)
                break
            elif key == ord('s'):
                self.calculate_result(cv_image)

        cv2.destroyAllWindows()
        cam.stop()
        print("-- Stopped calibration process")

    def calibrate_using_files(self, img_dir_path=""):
        window_name = "File Calibration"
        cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
        print("-- Started calibration process")
        print("Press any key to continue the calibration process")

        #self._im_names = glob.glob(path.join(img_dir_path, '*.jpg')) + glob.glob(path.join(img_dir_path, '*.png')) + glob.glob(path.join(img_dir_path, '*.bmp'))
        self.image_names = list(
            chain.from_iterable(glob.glob(path.join(img_dir_path, ext)) for ext in ('*.jpg', '*.png', '*.bmp')))

        cv_image = None
        for f_name in self.image_names:
            # Find the pattern
            cv_image = cv2.imread(f_name)
            cv_image_orig = cv_image.copy()
            self.find_pattern(cv_image)

            # save img
            im_path = path.join(self.calib_dir, 'img', path.basename(f_name))
            cv2.imwrite(im_path, cv_image_orig)

            # Show image
            cv2.imshow(window_name, cv_image)
            cv2.waitKey(500)

        self.calculate_result(cv_image)
        cv2.destroyAllWindows()
        print("-- Stopped calibration process")


class CalibrationProcessIntrinsic(CalibrationProcess, ABC):
    def __init__(self, calibration_board: CalibrationBoard, calib_dir=None):
        super().__init__(calibration_board, calib_dir, "intrinsic")

    def create_directory_tree(self, calib_dir):
        if not calib_dir:
            self.calib_dir = datetime.now().strftime("%Y%m%d_%H%M%S_intrinsic")
        else:
            self.calib_dir = calib_dir
        makedirs(self.calib_dir, exist_ok=True)
        makedirs(path.join(self.calib_dir, 'img'), exist_ok=True)

    def prepare_image(self, img) -> Image:
        return img

    def process_chess_board(self, corners, gray, img, ret):
        """
        :param corners: detected corners
        :param gray: grayscale img
        :param img: original img (reference will be altered)
        :param ret: if pattern was found
        """
        self._objpoints.append(self._objp)

        if self._calibration_board.pattern_type == "checker_board":
            corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), self._criteria)
            self._imgpoints.append(corners2)
            cv2.drawChessboardCorners(img, self._calibration_board.dimension(), corners2, ret)

        elif self._calibration_board.pattern_type == "circle_board":
            self._imgpoints.append(corners)
            cv2.drawChessboardCorners(img, self._calibration_board.dimension(), corners, ret)

    def calculate_result(self, cv_image):
        self.cv_image = cv_image
        shape = cv_image.shape[:2][::-1]
        # Assertion
        assert len(self._imgpoints) == len(self._objpoints), "imgpoints not equals objpoints"
        if len(self._imgpoints) == 0:
            print("No object points to calibrate.")
            return

        # Calibration
        self.calibration = IntrinsicCalib()
        ret, self.calibration['mtx'], self.calibration['dist'], self.calibration['rvecs'], self.calibration['tvecs'] = \
            cv2.calibrateCamera(self._objpoints, self._imgpoints, shape, None, None)
        self.calibration.calculate_reprojection_error(self._objpoints, self._imgpoints, self.image_names)
        self.calibration.save(path.join(self.calib_dir, 'intrinsic.json'))

    def show(self):
        print("Not implemented!")


class CalibrationProcessExtrinsic(CalibrationProcess, ABC):
    def __init__(self, chess_board: CalibrationBoard, intrinsic_file_name: str,
                 additional_rotation_vec_d=None, additional_translation_vec_mm=None, calib_dir=None):
        """
        Initialization of the extrinsic calibration vector
        :param chess_board: chess board used for the calibration
        :param intrinsic_file_name: file name to the intrinsic calibration to be used
        :param additional_rotation_vec_d: additional rotation vector expressed in [degrees]
        """
        super().__init__(chess_board, calib_dir, "extrinsic")
        if additional_rotation_vec_d is None:
            self.additional_rotation_vec = np.array([0.0, 0.0, 0.0]) * (math.pi / 180)
        else:
            self.additional_rotation_vec = np.array(additional_rotation_vec_d) * (math.pi / 180)
        self.additional_translation_vec = additional_translation_vec_mm
        self.intrinsic_calib = IntrinsicCalib()
        self.intrinsic_calib.load(intrinsic_file_name)

    def create_directory_tree(self, calib_dir):
        if not calib_dir:
            self.calib_dir = datetime.now().strftime("%Y%m%d_%H%M%S_extrinsic")
        else:
            self.calib_dir = calib_dir
        makedirs(self.calib_dir, exist_ok=True)
        makedirs(path.join(self.calib_dir, 'img'), exist_ok=True)

    def prepare_image(self, img) -> Image:
        return img.undistort(self.intrinsic_calib)

    def process_chess_board(self, corners, gray, img, ret):
        """
        :param corners: detected corners
        :param gray: grayscale img
        :param img: original img (reference will be altered)
        :param ret: if pattern was found
        """
        corners_ = []
        if self._calibration_board.pattern_type == "checker_board":
            corners_ = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), self._criteria)
        elif self._calibration_board.pattern_type == "circle_board":
            corners_ = corners
        cv2.drawChessboardCorners(img, self._calibration_board.dimension(), corners_, ret)
        self.calibration = ExtrinsicCalib()

        # Draw and display the corners

        # Calibration
        ret, self.calibration['rvec'], self.calibration['tvec'] = \
            cv2.solvePnP(self._objp, corners_, self.intrinsic_calib['mtx'], self.intrinsic_calib['dist'])

        # apply additional rotation

        r_calib = cv2.Rodrigues(self.calibration['rvec'])[0]
        r_extra = cv2.Rodrigues(np.array(
            [self.additional_rotation_vec[0], self.additional_rotation_vec[1], self.additional_rotation_vec[2]]))[0]
        r_mult = np.matmul(r_calib, r_extra)
        self.calibration['rvec'] = cv2.Rodrigues(r_mult)[0]
        # determine reprojection error
        self.calibration.calculate_reprojection_error_extrinsic(self._objp, corners_, self.intrinsic_calib['mtx'],
                                                                self.intrinsic_calib['dist'], r_calib,
                                                                self.calibration['tvec'])

    def calculate_result(self, cv_image):
        self.cv_image = cv_image
        # save calibration
        self.calibration.save(path.join(self.calib_dir, 'extrinsic.json'))

    def show(self, for_time=500):
        if self.cv_image is not None:
            window_name2 = "Calib output"
            cv2.namedWindow(window_name2, cv2.WINDOW_NORMAL)
            Image(np.array(cv2.cvtColor(self.cv_image, cv2.COLOR_BGR2RGB))). \
                project_coordinate_system(self.calibration, self.intrinsic_calib). \
                show(window_name2, for_time)

        print(self.calibration)


class CalibrationProcessWhiteBalance:
    def __init__(self):
        self._im_names = []
        self.calib_dir = datetime.now().strftime("%Y%m%d_%H%M%S_white")
        self.white_balance_calib = WhiteBalanceCalib()

    def get_color_map(self, shape):
        h, w = shape
        w = 100
        color_line = np.round(np.linspace(255, 0, h)).astype(np.uint8)
        color_map = np.vstack([[color_line] * w]).transpose()
        bar_color_map = cv2.applyColorMap(color_map, cv2.COLORMAP_JET)
        bar_color_map[0:h, 0:10, :] = 0
        return bar_color_map

    def process_im(self, im):
        cv_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        cv_gray_color = cv2.cvtColor(cv_gray, cv2.COLOR_GRAY2RGB)
        img_color_map = cv2.applyColorMap(cv_gray, cv2.COLORMAP_JET)
        color_bar = self.get_color_map(cv_gray.shape)
        im_show = np.hstack([cv_gray_color, img_color_map, color_bar])
        return cv_gray, im_show

    def save_calibration(self, cv_gray):
        makedirs(self.calib_dir, exist_ok=True)
        im_path = path.join(self.calib_dir, "white_balance.png")
        self.white_balance_calib.set(cv_gray)
        self.white_balance_calib.save(im_path)

    def calibrate_using_camera(self, cam):
        window_name = "Camera Calibration"
        cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
        print("-- Started calibration process")
        cam.start_acquisition()

        print("Press 'q' to terminate the calibration process, 's' to save intermediately "
              "and ' ' to capture an img.")

        key = None
        while 1:
            cam_img = cam.get_image()
            if not cam_img:
                continue

            cv_gray, im_show = self.process_im(cam_img.get())

            wait_time_ms = 10
            if key == ord(' '):  # only save when key is ' '
                self.save_calibration(cv_gray)
                # wait for visualization
                wait_time_ms = 2000  # To visualize pattern layout wait for 2 secs when pattern is found!
            if key == ord('q'):
                break

            cv2.imshow(window_name, im_show)
            key = cv2.waitKey(wait_time_ms)
        cv2.destroyAllWindows()
        cam.stop()
        print("-- Stopped calibration process")

    def calibrate_using_files(self, img_dir_path=""):
        window_name = "File Calibration"
        cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
        print("-- Started calibration process")

        print("Press any key to coninue the calibration process")

        self._im_names = glob.glob(path.join(img_dir_path, '*.png'))
        i = 0
        while i < len(self._im_names):
            f_name = self._im_names[i]
            img = cv2.imread(f_name)

            cv_gray, im_show = self.process_im(img)

            cv2.imshow(window_name, im_show)
            key = cv2.waitKey(-1)

            if key == ord('n'):
                i += 1
            if key == ord(' '):  # only save when key is ' '
                self.save_calibration(cv_gray)
            if key == ord('q'):
                break

        cv2.destroyAllWindows()
        print("-- Stopped calibration process")
