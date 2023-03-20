import pandas as pd


def load_data(dataset_name: str, base_path: str = "datasets") -> pd.DataFrame:
    return pd.read_csv(f"{base_path}/{dataset_name}.csv")
