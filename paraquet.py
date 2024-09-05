import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

def detect_and_convert_mixed_types(df):
    for col in df.columns:
        # detect mixed types in the column
        if df[col].apply(type).nunique() > 1:
            # check if the column contains strings or floats
            if df[col].dtype == 'object' or pd.api.types.is_float_dtype(df[col]):
                # attempt to convert to float (which maps to double in Parquet)
                df[col] = pd.to_numeric(df[col], errors='coerce')
                print(f"Converted column {col} to float.")
    return df

def convert_csv_to_parquet(csv_file_path, parquet_file_path):
    try:
        # read CSV file into DataFrame
        df = pd.read_csv(csv_file_path, low_memory=False)
        
        # detect and convert columns with mixed types
        df = detect_and_convert_mixed_types(df)
        
        # convert DataFrame to Arrow Table
        table = pa.Table.from_pandas(df)
        
        # write Arrow Table to Parquet file
        pq.write_table(table, parquet_file_path)
        
        print(f"Successfully converted {csv_file_path} to {parquet_file_path}")
    except Exception as e:
        print(f"Failed to convert {csv_file_path} to {parquet_file_path}: {e}")

csv_file_path = 'concatenated_dataframe.csv'
parquet_file_path = 'combineddata.parquet'
convert_csv_to_parquet(csv_file_path, parquet_file_path)
