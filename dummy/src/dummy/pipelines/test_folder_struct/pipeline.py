# src/<project_name>/pipelines/data_processing/pipeline.py
from kedro.pipeline import Pipeline, node
from .nodes import process_data_tst, count_categories_tst  

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            node(
                func=process_data_tst,          # Function that processes the data
                inputs="input_data",        # Input dataset defined in catalog.yml
                outputs="output_data_tst",      # Output dataset defined in catalog.yml
                name="process_data_node_tst",   # Name of the node
            ),
            node(
                func=count_categories_tst,
                inputs="input_data",  # Use the same input dataset
                outputs="category_counts_tst",  # New output dataset
                name="count_categories_node_tst"
            )
        ]
    )
