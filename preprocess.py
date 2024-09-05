import os
import pandas as pd
import numpy as np

def determine_majority_type(series):
    # get the types of all non-null values
    types = series.dropna().apply(type)
    # count the occurrences of each type
    type_counts = types.value_counts()
    # return the type with the highest count
    return type_counts.idxmax()

def convert_column_to_majority_type(df, column):
    try:
        majority_type = determine_majority_type(df[column])
        if majority_type == int:
            df[column] = df[column].astype(np.int64)
        elif majority_type == float:
            df[column] = df[column].astype(np.float64)
        elif majority_type == str:
            df[column] = df[column].astype(str)
        print(f"Converted column {column} to {majority_type}")
    except Exception as e:
        print(f"Failed to convert column {column}: {e}")

def convert_mixed_types_in_csv(file_path):
    try:
        # read the CSV file
        print("Processing file " + file_path)
        df = pd.read_csv(file_path)
        
        # iterate over the columns and check for mixed types
        for column in df.columns:
            if df[column].apply(type).nunique() > 1:
                convert_column_to_majority_type(df, column)
        
        # save the modified CSV file
        df.to_csv(file_path, index=False)
        print(f"Processed {file_path}")
    except Exception as e:
        print(f"Failed to process {file_path}: {e}")

def recursively_process_csv_files(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.csv'):
                file_path = os.path.join(root, file)
                convert_mixed_types_in_csv(file_path)


directory_to_search = './files/2024/06'
recursively_process_csv_files(directory_to_search)
