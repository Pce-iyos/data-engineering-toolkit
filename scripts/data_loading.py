import pandas as pd

def save_dataframe(df, filename, file_format):
    """
    Save a DataFrame to file in different formats.
    """
    if file_format == "csv":
        df.to_csv(filename, index=False)
    elif file_format == "json":
        df.to_json(filename, orient="records", lines=True)
    elif file_format == "parquet":
        df.to_parquet(filename, index=False)
    else:
        raise ValueError("Unsupported file format: choose csv, json, or parquet")
    print(f"DataFrame saved to {filename} in {file_format} format.")