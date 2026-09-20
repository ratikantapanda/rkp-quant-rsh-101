from rkp_quant_rsh_101.config import DEFAULT_SERIES, OUTPUT_DIR


def test_default_series_are_defined() -> None:
    assert "fed_funds" in DEFAULT_SERIES
    assert "cpi" in DEFAULT_SERIES
    assert "unemployment" in DEFAULT_SERIES


def test_output_dir_is_configured() -> None:
    assert OUTPUT_DIR.exists()
