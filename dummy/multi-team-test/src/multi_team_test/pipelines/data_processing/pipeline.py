# src/file_processing/pipelines/data_processing/pipeline.py

from kedro.pipeline import Pipeline, node
from .nodes import read_data, process_data, save_data

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            node(
                func=read_data,
                inputs="params:input_file",
                outputs="raw_data",
                name="read_data_node",
            ),
            node(
                func=process_data,
                inputs="raw_data",
                outputs="processed_data",
                name="process_data_node",
            ),
            node(
                func=save_data,
                inputs=["processed_data", "params:output_file"],
                outputs=None,
                name="save_data_node",
            ),
        ]
    )
