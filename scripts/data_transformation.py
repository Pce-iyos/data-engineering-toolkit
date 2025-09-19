import pandas as pd

def transform_dataframe(df):
    """
    Apply transformations to a DataFrame
    """
    # Rename columns
    df.columns = [col.lower() for col in df.columns]
