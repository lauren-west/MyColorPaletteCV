"""Tests face detection functionality."""
from typing import Tuple
import unittest
import numpy as np
import matplotlib.pyplot as plt
from skimage import data
import face_detection


class TestFaceDetection(unittest.TestCase):

    def test_face_detection(self):
       # Load the trained file from the module root.
        trained_file = data.lbp_frontal_face_cascade_filename()
        img = data.astronaut()

        face_rectangle = face_detection.detect_faces(
            trained_file, img)

        self.assertIsNotNone(face_rectangle)
