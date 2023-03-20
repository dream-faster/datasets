from load_data import load_data


def test_industial_residual_load() -> None:
    df = load_data("energy/industrial_pv_load")

    assert len(df) == 105225, "Dataset length didn't match"
