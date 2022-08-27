"""Tests face detection functionality."""
from typing import Tuple
import unittest
import matplotlib.pyplot as plt
from skimage import data
import face_detection


class TestFaceDetection(unittest.TestCase):

    def test_face_detection(self):
        img = data.astronaut()

        face_rectangles = face_detection.detect_faces(img)

        self.assertIsNotNone(face_rectangles)
