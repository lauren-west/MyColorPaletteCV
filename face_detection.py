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


def detect_faces(trained_file: str, img: np.ndarray) -> plt.Axes:
    # Initialize the detector cascade.
    detector = feature.Cascade(trained_file)
    detected = detector.detect_multi_scale(img=img,
                                           scale_factor=1.2,
                                           step_ratio=1,
                                           min_size=(60, 60),
                                           max_size=(123, 123))
    img_desc = plt.gca()
    for patch in detected:
        img_desc.add_patch(
            patches.Rectangle(
                (patch['c'], patch['r']),
                patch['width'],
                patch['height'],
                fill=False,
                color='r',
                linewidth=2
            )
        )
    return img_desc
