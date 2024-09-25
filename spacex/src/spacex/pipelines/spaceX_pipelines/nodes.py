# from typing import Dict, Tuple

import pandas as pd

params={"filepath": "filepath"}

def save_to_csv(data: list, filepath: str) -> None:
    df = pd.DataFrame(data)
    df.to_csv(filepath, index=False)
    print(f"Data has been written to {filepath}")

