"""Tests image color summarizer for determining hue, saturdation, and value"""
import unittest
from skimage import data
import image_color_summarizer


class TestImageColorSummarizer(unittest.TestCase):

    def test_image_color_summarizer(self):
        example_rgb_img = data.coffee()

        hue, saturation, value = image_color_summarizer.image_color_summarizer(
            example_rgb_img)

        self.assertIsNotNone(hue)
        self.assertIsNotNone(saturation)
        self.assertIsNotNone(value)
