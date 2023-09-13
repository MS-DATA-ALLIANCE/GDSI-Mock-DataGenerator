
# Mock Data Generator for COVID-MS Dataset

This repository contains a Python script to generate mock data that resembles the original COVID-MS dataset.

## About the Original Dataset

The original dataset can be downloaded from [PhysioNet](https://physionet.org/content/patient-level-data-covid-ms/1.0.0/). It contains various features related to COVID-19 cases among multiple sclerosis (MS) patients.

## How to Use the Mock Data Generator

1. Download the original dataset from PhysioNet and place it in the same directory as the Python script (`mock_data_generator_updated.py`).
2. Run the Python script. It will prompt you to enter the number of records you'd like to generate.
3. The script will generate a CSV file (`generated_mock_data.csv`) containing the synthetic data.

## How the Script Works

- The script first loads the original dataset to understand its structure and unique values for each feature.
- It then generates synthetic records, mimicking the data types and unique values found in the original dataset.
- Special care is taken to generate unique "secret_name" identifiers for each synthetic record.

## Requirements

- Python 3.x
- pandas
- numpy

## Disclaimer

This is a mock data generator and the generated data should not be used for any clinical or diagnostic purposes.
