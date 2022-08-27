"""Identifies color season for an individual's profile."""
import numpy as np
import face_detection
import image_color_summarizer

COLOR_SEASON_DICT = {
    # spring
    ("bright", "warm"): "bright spring",
    ("warm", "bright"): "true spring",
    ("light", "warm"): "light spring",
    # summer
    ("light", "cool"): "light summer",
    ("cool", "muted"): "true summer",
    ("muted", "cool"): "soft summer",
    # autumn
    ("muted", "warm"): "soft autumn",
    ("warm", "muted"): "true autumn",
    ("dark", "warm"): "dark autumn",
    # winter
    ("dark", "cool"): "dark winter",
    ("cool", "bright"): "true winter",
    ("bright", "cool"): "bright winter"
}


def match_characteristics_to_season(primary_characteristic: str,
                                    secondary_characteristic: str) -> str:
    return COLOR_SEASON_DICT[
        (primary_characteristic, secondary_characteristic)]


def get_primary_and_secondary_characteristics(
        hue: np.ndarry, sat: np.ndarray, val: np.ndarray):
    pass


def identify_color_season(img: np.ndarray):
    faces = face_detection.detect_faces(img)
    face = face_detection.crop(faces[0])

    hue, sat, val = image_color_summarizer(face)

    primary, secondary = get_primary_and_secondary_characteristics(
        hue, sat, val)
    color_season = match_characteristics_to_season(primary, secondary)

    return color_season
