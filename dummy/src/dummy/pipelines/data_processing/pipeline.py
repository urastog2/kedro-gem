# src/<project_name>/pipelines/data_processing/pipeline.py
from kedro.pipeline import Pipeline, node
from .nodes import process_data, count_categories  

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            node(
                func=process_data,          # Function that processes the data
                inputs="input_data",        # Input dataset defined in catalog.yml
                outputs="output_data",      # Output dataset defined in catalog.yml
                name="process_data_node",   # Name of the node
            ),
            node(
                func=count_categories,
                inputs="input_data",  # Use the same input dataset
                outputs="category_counts",  # New output dataset
                name="count_categories_node"
            )
        ]
    )
