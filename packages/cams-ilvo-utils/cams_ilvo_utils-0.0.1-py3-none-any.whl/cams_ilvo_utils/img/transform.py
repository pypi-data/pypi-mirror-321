import numpy as np
import cv2


def rtvec_to_matrix(rvec, tvec):
    """
    Convert rotation vector and translation vector to 4x4 matrix
    :param rvec: rotation vector
    :param tvec: translation vector
    :return:
    """
    rvec = np.asarray(rvec)
    tvec = np.asarray(tvec)

    T = np.eye(4)
    R, jac = cv2.Rodrigues(rvec)
    T[:3, :3] = R
    T[:3, 3] = tvec
    return T


def matrix_to_rtvec(matrix):
    """
    Convert 4x4 matrix to rotation vector and translation vector
    :param matrix:
    :return:
    """
    rvec, jac = cv2.Rodrigues(matrix[:3, :3])
    tvec = matrix[:3, 3]
    return rvec, tvec
