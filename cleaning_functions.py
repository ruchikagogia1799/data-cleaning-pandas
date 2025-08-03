import pandas as pd

def clean_column_names(df):
    """
    Strips whitespace, converts to lowercase, and replaces spaces with underscores.
    """
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    return df

def drop_empty_rows(df):
    """
    Drops rows that are completely empty.
    """
    return df.dropna(how='all')

def convert_date_column(df, column_name):
    """
    Attempts to convert a column to datetime format.
    """
    df[column_name] = pd.to_datetime(df[column_name], errors='coerce')
    return df

def drop_duplicates(df):
    """
    Drops duplicate rows.
    """
    return df.drop_duplicates()
