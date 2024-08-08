from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="baccarat_dataset_source", max_table_nesting=2)
def baccarat_dataset_source(
    base_url: str = dlt.config.value,
) -> List[DltResource]:

    # source configuration
    source_config: RESTAPIConfig = {
        "client": {
            "base_url": base_url,
        },
        "resources": [
            {
                "name": "baccarat",
                "table_name": "baccarat",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/baccarat",
                    "params": {
                        # the parameters below can optionally be configured
                        "num_records": "100",
                    },
                    "paginator": "auto",
                },
            },
        ],
    }

    return rest_api_source(source_config)
