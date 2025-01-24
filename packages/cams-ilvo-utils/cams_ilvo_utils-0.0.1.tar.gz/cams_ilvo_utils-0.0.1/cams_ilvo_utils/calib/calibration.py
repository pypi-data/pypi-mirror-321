import json
from abc import ABC, abstractmethod
from fileinput import filename

import cv2
import numpy as np
from copy import deepcopy
from cams_ilvo_utils.img.transform import rtvec_to_matrix


class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()  # Convert ndarray to list
        return super().default(obj)

class CalibDict(dict, ABC):
    def __init__(self, data=None):
        super().__init__()

        if isinstance(data, str):
            # Filename
            self.load(data)
        elif isinstance(data, dict):
            # Dict
            self.set(data)

    @abstractmethod
    def _prepare_save(self):
        pass

    def to_dict(self):
        return dict(self)

    def save(self, file_name):
        self._prepare_save()
        with open(file_name, 'w') as handle:
            json.dump(self, handle, indent=4, cls=CustomEncoder)
        print(f"The calibration file is saved to: {file_name}")
        # print(self)
        print("---")

    def load(self, file_name: str):
        # Load data (deserialize)
        with open(file_name, 'r') as handle:
            d = json.load(handle)
            self.set(d)

    def set(self, data: dict):
        for k in data.keys():
            if k in ['rvec', 'tvec', 'mtx', 'dist']:
                self[k] = np.array(data[k])
            else:
                self[k] = data[k]


class IntrinsicCalib(CalibDict, ABC):
    def __init__(self, data=None):
        super().__init__(data)

        if data is None:
            self['reprojection_errors'] = []
            self['reprojection_mean_error'] = 0.0


    def _prepare_save(self):
        for e in self['reprojection_errors']:
            print(f"{e['im_name']}: {e['error']}")
        print(
            f"This intrinsic calibration process has a mean re-projection error of {self['reprojection_mean_error']}.")

    def calculate_reprojection_error(self, objpoints, imgpoints, imnames):
        for k in ['rvecs', 'tvecs', 'mtx', 'dist']:
            assert k in self.keys(), f"'{k}' is not present in this calib object!"

        mean_error = 0
        for i in range(len(objpoints)):
            imgpoints2, _ = cv2.projectPoints(objpoints[i], self['rvecs'][i], self['tvecs'][i],
                                              self['mtx'], self['dist'])
            error = cv2.norm(imgpoints[i], imgpoints2, cv2.NORM_L2) / len(imgpoints2)
            self['reprojection_errors'].append({'im_name': imnames[i], 'error': error})
            mean_error += error
        self['reprojection_mean_error'] = mean_error / len(objpoints)


class ExtrinsicCalib(CalibDict, ABC):
    def __init__(self, data=None):
        super().__init__(data)

    def _prepare_save(self):
        pass

    def affine(self):
        return rtvec_to_matrix(self['rvec'], self['tvec'])

    def calculate_reprojection_error_extrinsic(self, objpoints, imgpoints, mtx, dist, r_calib, t_vec):
        imgpoints_reprojected, _ = cv2.projectPoints(objpoints, r_calib, t_vec, mtx, dist)
        mean_reprojection_error = cv2.norm(imgpoints, imgpoints_reprojected, cv2.NORM_L2) / len(imgpoints_reprojected)
        print("Reprojection error:", mean_reprojection_error)
        self['reprojection_mean_error'] = mean_reprojection_error


class WhiteBalanceCalib:
    def __init__(self, file_name=None):
        self.im = None
        if file_name:
            self.load(file_name)

    def set(self, im):
        self.im = deepcopy(im)

    def save(self, file_name):
        if self.im is not None:
            cv2.imwrite(file_name, self.im)
            print(f"The calibration file is saved to: {file_name}")
            print("---")

    def load(self, file_name):
        self.im = cv2.imread(file_name, cv2.IMREAD_GRAYSCALE)
