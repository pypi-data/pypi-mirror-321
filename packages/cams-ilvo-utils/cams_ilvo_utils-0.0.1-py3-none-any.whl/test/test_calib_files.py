from unittest import TestCase

from cams_ilvo_utils.calib.board import CalibrationBoard
from cams_ilvo_utils.calib.process import CalibrationProcessIntrinsic, CalibrationProcessExtrinsic, \
    CalibrationProcessWhiteBalance
import numpy as np
from os import path


class TestCalibFiles(TestCase):
    def test_intrinsic_calib_chess_board(self):
        print("-- Starting demo: File calibration with checkerboard")
        # file_path = 'files/checker_board/intrinsic/img'
        file_path = 'files/checker_board/intrinsic/img'
        assert path.exists(file_path)

        calib = CalibrationProcessIntrinsic(CalibrationBoard(10, 9, 16.25, 16.25, "checker_board"))
        calib.calibrate_using_files(file_path)

        print("-- Stopped demo: File calibration with checkerboard")

    def test_intrinsic_calib_circle_board(self):
        print("-- Starting demo: File calibration with circle_board")
        file_path = 'files/circle_board/intrinsic/img'
        assert path.exists(file_path)

        calib = CalibrationProcessIntrinsic(CalibrationBoard(8, 6, 35, 35, "circle_board"))
        calib.calibrate_using_files(file_path)

        print("-- Stopped demo: File calibration with circle_board")

    def test_extrinsic_calib_checker_board(self):
        print("-- Starting demo: File calibration extrinsic using checker_board")
        intrinsic_file_name = 'files/checker_board/intrinsic/intrinsic.json'
        assert path.exists(intrinsic_file_name)
        file_path = 'files/checker_board/extrinsic/img'
        assert path.exists(file_path)

        calib = CalibrationProcessExtrinsic(CalibrationBoard(10, 9, 16.25, 16.25, "checker_board"), intrinsic_file_name)
        calib.calibrate_using_files(file_path)
        calib.show(for_time=-1)

        print("-- Stopped demo: File calibration extrinsic using checker_board")

    def test_extrinsic_calib_circle_board(self):
        print("-- Starting demo: File calibration extrinsic using circle_board")
        intrinsic_file_name = 'files/circle_board/intrinsic/intrinsic.json'
        assert path.exists(intrinsic_file_name)
        file_path = 'files/circle_board/extrinsic/img'
        assert path.exists(file_path)

        # test extrinsic calibration using circle_board
        calib = CalibrationProcessExtrinsic(CalibrationBoard(6, 3, 91.7, 96.0, "circle_board"),
                                            intrinsic_file_name,
                                            np.array([0.0, 180.0, 0.0]), np.array([-192.0, 0.0, 0.0]))
        calib.calibrate_using_files(file_path)
        calib.show(for_time=-1)

        print("-- Stopped demo: File calibration extrinsic using circle_board")

    def test_white_balance_calib(self):
        print("-- Starting demo: File calibration white balance")
        print("Set parameters")
        # cam.init_color_params()
        file_path = 'files/white_balance'
        assert path.exists(file_path)

        calib = CalibrationProcessWhiteBalance()
        calib.calibrate_using_files(file_path)

        print("-- Stopped demo: File calibration white balance")
