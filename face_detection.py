"""Provides face detection functionality using scikit-image.

This computer vision example shows how to detect faces on an image using object
detection framework based on machine learning.

Take into account that false detections are inevitable and if
you want to have a really precise detector, you will have to train it yourself
using `OpenCV train cascade utility
<https://docs.opencv.org/2.4/doc/user_guide/ug_traincascade.html>`_.
"""
import numpy as np
from skimage import data
from skimage import feature

import matplotlib.pyplot as plt
from matplotlib import patches


def crop(face_rectangle, img: np.ndarray):
    """Helper function for detect_faces.

    Crops the image to contain just the detected face.
    """
    x0 = face_rectangle["x"]
    y0 = face_rectangle["y"]
    width = face_rectangle["width"]
    height = face_rectangle["height"]
    return img[y0:y0+height, x0:x0+width, :]


def detect_faces(trained_file: str, img: np.ndarray) -> plt.Axes:
    # Initialize the detector cascade.
    detector = feature.Cascade(trained_file)
    detected = detector.detect_multi_scale(img=img,
                                           scale_factor=1.2,
                                           step_ratio=1,
                                           min_size=(60, 60),
                                           max_size=(123, 123))
    face_rectangles = []
    for rectangle in detected:
        face_rectangle = {
            "x": rectangle['c'],
            "y": rectangle['r'],
            "width": rectangle['width'],
            "height": rectangle['height'],
        }
        face_rectangles.append(face_rectangle)

    return face_rectangles
