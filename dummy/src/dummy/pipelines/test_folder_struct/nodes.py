from typing import Dict, Tuple

import pandas as pd
from pyspark.sql import Column
from pyspark.sql import DataFrame as SparkDataFrame
from pyspark.sql.functions import regexp_replace
from pyspark.sql.types import DoubleType

def process_data_tst(data: pd.DataFrame) -> pd.DataFrame:
    # Example processing: filter rows where 'value' column > 10
    processed_data = data[data['value'] > 5]
    return processed_data


def summarize_data_tst(data: pd.DataFrame) -> pd.DataFrame:
    """
    Summarize data by computing basic statistics.
    """
    summary = data.describe()
    return summary

def count_categories_tst(data: pd.DataFrame) -> pd.DataFrame:
    """
    Count occurrences of each category.
    """
    category_counts = data['category'].value_counts().reset_index()
    category_counts.columns = ['category', 'count']
    return category_counts

