import pandas as pd

def clean_dataframe(df):
    """
    Perform basic cleaning on a DataFrame
    """
    df = df.drop_duplicates()
    df = df.dropna(axis=1, how="all")
    return df
