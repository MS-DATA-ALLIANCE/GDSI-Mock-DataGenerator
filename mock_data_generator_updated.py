
import pandas as pd
import random
import numpy as np

def generate_mock_data(num_records, unique_values_dict):
    """
    Generate mock data based on the unique values and data types found in the original dataset.
    
    Parameters:
    - num_records: The number of records to generate.
    - unique_values_dict: Dictionary containing unique values for each column in the original dataset.
    
    Returns:
    - mock_df: A DataFrame containing the generated mock data.
    """
    
    # Initialize an empty dictionary to store the generated data
    mock_data = {}
    
    # Generate unique "secret_name" identifiers
    mock_data["secret_name"] = [f"C_{1000 + i}" for i in range(num_records)]
    
    # Generate data for each column except "secret_name"
    for column, unique_values in unique_values_dict.items():
        if column == "secret_name":
            continue
        if df[column].dtype == 'object':
            mock_data[column] = random.choices(unique_values, k=num_records)
        elif df[column].dtype == 'int64':
            mock_data[column] = random.choices(unique_values, k=num_records)
        elif df[column].dtype == 'float64':
            min_val = np.min(unique_values)
            max_val = np.max(unique_values)
            mock_data[column] = np.random.uniform(min_val, max_val, num_records)
        else:
            mock_data[column] = [np.nan] * num_records
    
    # Create a DataFrame from the generated data
    mock_df = pd.DataFrame(mock_data)
    
    return mock_df

# Load the original dataset
df = pd.read_csv('GDSI_OpenDataset_Final.csv')

# Prepare the unique values dictionary based on the original dataset
unique_values_dict = {}
for column in df.columns:
    unique_values = df[column].dropna().unique()
    unique_values_dict[column] = unique_values

# Ask the user for the number of records to generate
try:
    num_records = int(input("How many records would you like to generate? "))
    if num_records < 1:
        print("The number of records should be at least 1.")
    else:
        # Generate the mock data
        mock_df = generate_mock_data(num_records, unique_values_dict)
        
        # Save the mock data to a CSV file
        mock_data_file_path = 'generated_mock_data.csv'
        mock_df.to_csv(mock_data_file_path, index=False)
        
        print(f"Mock data has been generated and saved to {mock_data_file_path}.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")

