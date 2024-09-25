from kedro.pipeline import Pipeline, node, pipeline

from .nodes import save_to_csv, params


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=save_to_csv,
                inputs=["spacex_launches", "params:filepath"],  # Use the registered dataset
                outputs=None,
                # params={"filepath": "data/01_raw/spacex_launches.csv"}  # Change this path as needed
            ),
        ]
    )
