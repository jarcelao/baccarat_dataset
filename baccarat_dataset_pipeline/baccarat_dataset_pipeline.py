import dlt

from baccarat_dataset import baccarat_dataset_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="baccarat_dataset_pipeline",
        destination='filesystem',
        dataset_name="baccarat_dataset_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = baccarat_dataset_source()
    info = pipeline.run(source)
    print(info)
