"""Tests color season identification functionality."""
from typing import Tuple
import unittest
import color_season_identification


class TestColorSeasonIdentification(unittest.TestCase):

    def test_identify_color_season(self):
        expected_color_season = "light summer"
        primary, secondary = "light", "cool"

        actual_color_season = (
            color_season_identification.match_characteristics_to_season(
                primary, secondary))

        self.assertEqual(actual_color_season, expected_color_season)
