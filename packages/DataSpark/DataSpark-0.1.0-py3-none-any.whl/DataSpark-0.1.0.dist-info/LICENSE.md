
### **data_handling/data_operations.py**

Ensure all functions have updated or added docstrings:

```python
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def load_data(file_path, file_type='csv'):
    """
    Load data from a file into a pandas DataFrame.
    
    :param file_path: Path to the data file
    :param file_type: Type of the file (csv, json, or excel)
    :return: pandas DataFrame
    """
    if file_type == 'csv':
        return pd.read_csv(file_path)
    elif file_type == 'json':
        return pd.read_json(file_path)
    elif file_type == 'excel':
        return pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file type")

def save_data(df, file_path, file_type='csv'):
    """
    Save DataFrame to a file.
    
    :param df: DataFrame to save
    :param file_path: Path where to save the file
    :param file_type: Type of file to save as (csv, json, or excel)
    """
    if file_type == 'csv':
        df.to_csv(file_path, index=False)
    elif file_type == 'json':
        df.to_json(file_path, orient='records')
    elif file_type == 'excel':
        df.to_excel(file_path, index=False)
    else:
        raise ValueError("Unsupported file type")

def clean_data(df):
    """
    Perform basic data cleaning operations, like removing NaN values.
    
    :param df: DataFrame to clean
    :return: Cleaned DataFrame
    """
    return df.dropna()

def merge_datasets(df1, df2, on=None, how='inner'):
    """
    Merge two DataFrames based on common columns or index.
    
    :param df1: First DataFrame
    :param df2: Second DataFrame
    :param on: Column name(s) to join on (can be a string or list of strings)
    :param how: Type of merge to be performed ('left', 'right', 'outer', 'inner')
    :return: Merged DataFrame
    """
    return pd.merge(df1, df2, on=on, how=how)

def convert_data_type(df, column, new_type):
    """
    Convert the data type of a specified column in the DataFrame.
    
    :param df: DataFrame to modify
    :param column: Name of the column to convert
    :param new_type: New data type to convert to (e.g., 'int64', 'float64', 'category')
    :return: DataFrame with converted column
    """
    return df.astype({column: new_type})

def apply_feature_engineering(df, feature_engineering_func):
    """
    Apply a custom feature engineering function to the DataFrame.
    
    :param df: DataFrame to engineer
    :param feature_engineering_func: A function that takes a DataFrame and returns a DataFrame with new features
    :return: DataFrame with new features
    """
    return feature_engineering_func(df)

def example_feature_engineering(df):
    """
    Example function to add new features.
    Adds 'age_group' based on age ranges and normalizes 'income'.
    
    :param df: DataFrame including 'age' and 'income' columns
    :return: DataFrame with new 'age_group' and 'normalized_income' features
    """
    df['age_group'] = pd.cut(df['age'], bins=[0, 18, 65, 100], labels=['child', 'adult', 'senior'])
    
    # Normalize income using StandardScaler from sklearn
    scaler = StandardScaler()
    df['normalized_income'] = scaler.fit_transform(df[['income']])
    return df

def scale_large_dataset(df, chunk_size=100000):
    """
    Scale a large dataset using Dask for memory efficiency.
    
    :param df: DataFrame or Dask DataFrame
    :param chunk_size: Number of rows to process at once
    :return: Dask DataFrame with scaled features
    """
    import dask.dataframe as dd
    
    if not isinstance(df, dd.DataFrame):
        df = dd.from_pandas(df, npartitions=df.shape[0] // chunk_size + 1)
    
    scaler = StandardScaler()
    df['scaled_feature'] = df.map_partitions(lambda x: scaler.fit_transform(x), meta=('x', np.float64))
    return df