# baccarat_dataset

Ingest data from [https://baccarat-api-v1.onrender.com/](https://baccarat-api-v1.onrender.com/) using [dlt](https://dlthub.com/).

## Description

The source for this dataset is an API that generates data for games of [Baccarat](https://en.wikipedia.org/wiki/Baccarat). However, the data is exposed only via an API that returns up to 100 games at a time. Thus, a data scientist may struggle to gather enough data for their analysis.

This is a data engineering project that aims to alleviate this problem by automatically ingesting the data from the API and preparing a workable dataset from it. The backbone for this project is dlt, a Python library designed for ELT workloads.

## Getting Started

### Dataset

The raw dataset is already available at a simulated data lakehouse located at `data_export/baccarat_dataset_data`. It is divided into 3 main folders, each representing a table.

* `baccarat` contains data about the game itself
* `baccarat__banker_hand` contains data about the banker's hand for each game
* `baccarat__player_hand` contains data about the player's hand for each game

As of writing, the dataset contains the data for 1000 games, spread over 10 parquet files, with 100 rows per file, for each table.

Below are the data dictionaries for each table:

**Table: baccarat**

|  | name               | data_type | nullable |
|--------|--------------------|-----------|----------|
| 0      | game               | text      | true     |
| 1      | game_id            | text      | true     |
| 2      | player_id          | text      | true     |
| 3      | status             | text      | true     |
| 4      | start_time         | timestamp | true     |
| 5      | end_time           | timestamp | true     |
| 6      | player_hand_value  | bigint    | true     |
| 7      | banker_hand_value  | bigint    | true     |
| 8      | last_action        | text      | true     |
| 9      | player_wager       | double    | true     |
| 10     | player_payout      | double    | true     |
| 11     | game_outcome       | text      | true     |
| 12     | player_bet         | text      | true     |
| 13     | player_bet_outcome | text      | true     |
| 14     | _dlt_load_id       | text      | false    |
| 15     | _dlt_id            | text      | false    |

**Table: baccarat__player_hand / baccarat__banker_hand**

|  | name           | data_type | nullable |
|--------|----------------|-----------|----------|
| 0      | value          | text      | true     |
| 1      | rank           | text      | true     |
| 2      | _dlt_parent_id | text      | false    |
| 3      | _dlt_list_idx  | bigint    | false    |
| 4      | _dlt_id        | text      | false    |

Each row in the above table represents one card played in a certain game. Note the column `_dlt_parent_id`, which identifies the parent game for a row. In addition, each card played in the same game is indexed by the `_dlt_list_idx` column. `_dlt_id` is a unique object identifier for each row.

In addition, note that no additional processing has been done on the tables apart from ingesting and normalizing them. It is up to you how to model the data to fit your own needs.

### Ingestion Script

To run the ingestion script on your own, you'll need to have **Python 3.12** with the **[pipenv](https://pipenv.pypa.io/en/latest/)** package installed. Enter the below commands to quickly execute the script.

```
pipenv shell
pipenv install
cd baccarat_dataset_pipeline
./generate_data.sh
```

This will generate 10 parquet files for each table containing 100 rows each, appending them to the existing tables at `data_export/baccarat_dataset_data`. If you wish to change these parameters, you may do so at `baccarat_dataset_pipeline/generate_data.sh`.

If you wish to work on the ingestion code itself, you may access the [dlt documentation](https://dlthub.com/docs/intro).

## What's Next
As suggested by the API's creator, you may use the data for the below purposes

* Create dashboards,
* Perform statistical analysis,
* Perform clustering analysis to detect anomalies in the data.

As the data is stored in parquet files, you may use software such as [Pandas](https://pandas.pydata.org/), [PySpark](https://spark.apache.org/docs/latest/api/python/index.html), or [DuckDB](https://duckdb.org/) to read the data.

In addition, you also may expand on the project with the below suggestions:

* Fully automate the pipeline using a data orchestrator (e.g. [Airflow](https://airflow.apache.org/))
* Change the sink to a working data warehouse or lakehouse (e.g. [BigQuery](https://cloud.google.com/bigquery), [GCS](https://cloud.google.com/storage?hl=en))
* Play the role of an Analytics Engineer and transform the data using [dbt](https://www.getdbt.com/)

## Special Thanks
Special thanks to [gryAI](https://github.com/gryAI) for developing and deploying the API! The source repo is available [here](https://github.com/gryAI/Baccarat-Game-Data-Generator-API).
