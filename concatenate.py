import os
import pandas as pd

def read_and_concatenate_csv_files(directory):
    all_dfs = []

    # recursively search for CSV files in the directory
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.csv'):
                file_path = os.path.join(root, file)
                try:
                    df = pd.read_csv(file_path)
                    all_dfs.append(df)
                    print(f"Processed {file_path}")
                except Exception as e:
                    print(f"Failed to process {file_path}: {e}")

    if all_dfs:
        combined_df = pd.concat(all_dfs, ignore_index=True)
        return combined_df
    else:
        print("No CSV files found.")
        return None


def save_dataframe_to_csv(df, output_path):
    try:
        df.to_csv(output_path, index=False)
        print(f"Combined DataFrame saved to {output_path}")
    except Exception as e:
        print(f"Failed to save DataFrame to {output_path}: {e}")


directory_to_search = './files/2024/07'
output_file_path = 'concatenated_dataframe.csv'

combined_df = read_and_concatenate_csv_files(directory_to_search)

if combined_df is not None:
    save_dataframe_to_csv(combined_df, output_file_path)
    print("Combined DataFrame shape:", combined_df.shape)
