import os
import pandas as pd

def add_date_columns_to_csv(file_path):
    try:
        # read the CSV file
        df = pd.read_csv(file_path)
        
        # check if the TransDate column exists
        if 'TransDate' in df.columns:
            # convert TransDate to datetime format with inferred format
            df['TransDate'] = pd.to_datetime(df['TransDate'], infer_datetime_format=True, dayfirst=False, errors='coerce')
            
            # extract year, month, and day
            df['Year'] = df['TransDate'].dt.year
            df['Month'] = df['TransDate'].dt.month
            df['Day'] = df['TransDate'].dt.day
            
            # save the modified DataFrame back to the CSV file
            df.to_csv(file_path, index=False)
            print(f"Processed {file_path}")
        else:
            print(f"TransDate column not found in {file_path}")
    except Exception as e:
        print(f"Failed to process {file_path}: {e}")

def recursively_process_csv_files(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.csv'):
                file_path = os.path.join(root, file)
                add_date_columns_to_csv(file_path)


directory_to_search = './files/2024/06'
recursively_process_csv_files(directory_to_search)
