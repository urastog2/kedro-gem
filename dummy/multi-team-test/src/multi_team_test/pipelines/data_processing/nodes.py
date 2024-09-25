# src/file_processing/pipelines/data_processing/nodes.py

import pandas as pd

def read_data(file_path: str) -> pd.DataFrame:
    """Reads the data from a CSV file."""
    return pd.read_csv(file_path)

def process_data(data: pd.DataFrame) -> pd.DataFrame:
    """Performs a simple transformation: Add a new column."""
    data["new_column"] = data["existing_column"] * 2  # Example transformation
    return data

def save_data(data: pd.DataFrame, output_path: str) -> None:
    """Saves the processed data to a CSV file."""
    data.to_csv(output_path, index=False)
