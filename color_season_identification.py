"""Identifies color season for an individual's profile."""

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


def identify_color_season(primary_characteristic: str,
                          secondary_characteristic: str) -> str:
    return COLOR_SEASON_DICT[
        (primary_characteristic, secondary_characteristic)]
