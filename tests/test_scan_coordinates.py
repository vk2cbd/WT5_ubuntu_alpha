import math

import pytest

from ri_antenna import Axis
from ri_ubuntu_gui import scan_coordinate_label, scan_plot_offset


def test_azimuth_scan_uses_boresight_elevation_for_cross_elevation() -> None:
    row = {
        "offset_degrees": 3.0,
        "nominal_el": 85.0,
    }

    assert scan_plot_offset(Axis.AZIMUTH, row) == pytest.approx(
        3.0 * math.cos(math.radians(85.0))
    )
    assert scan_coordinate_label(Axis.AZIMUTH) == "Cross-elevation offset (deg)"


def test_stored_cross_elevation_coordinate_is_used() -> None:
    row = {
        "offset_degrees": 3.0,
        "nominal_el": 85.0,
        "cross_elevation_offset_degrees": 0.25,
    }

    assert scan_plot_offset(Axis.AZIMUTH, row) == pytest.approx(0.25)


def test_elevation_scan_keeps_elevation_offset() -> None:
    row = {
        "offset_degrees": -1.25,
        "nominal_el": 75.0,
    }

    assert scan_plot_offset(Axis.ELEVATION, row) == pytest.approx(-1.25)
    assert scan_coordinate_label(Axis.ELEVATION) == "Elevation offset (deg)"
