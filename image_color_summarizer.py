"""
This function takes and image and summarizes hue, value, and chroma.

For 12 season color analysis, we care about rating the hue, value,
and chroma of an image.

Future work may involve creating another function that identifies
a face, or more specifically, eyes, hair, and skin to further
evaluate the color profile.
"""
import numpy as np
from typing import Tuple
import matplotlib.pyplot as plt
from skimage.io import imread, imshow
from skimage.color import rgb2hsv


def image_color_summarizer(rgb_img: np.ndarray
                           ) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    hsv_img = rgb2hsv(rgb_img)
    return (hsv_img[:, :, 0], hsv_img[:, :, 1], hsv_img[:, :, 2])
