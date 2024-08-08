#!/bin/bash
set -e

# Make sure you've ran `pipenv shell` before running this
command="python baccarat_dataset_pipeline.py"

times_per_minute=5
minutes=2

total_runs=$((times_per_minute * minutes))
current_run=1

echo "Generating data! Please wait..."

seconds_per_iteration=$((60 / times_per_minute))

for ((i=0; i<$minutes*60; i+=$seconds_per_iteration)); do
  echo "Pipeline run $current_run of $total_runs"
  $command
  current_run=$((current_run + 1))
  sleep $seconds_per_iteration
done

echo "Done!"