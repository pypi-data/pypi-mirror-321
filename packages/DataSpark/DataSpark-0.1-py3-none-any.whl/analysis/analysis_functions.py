import pandas as pd
import numpy as np

def describe_data(df):
    """
    Provide summary statistics for each column in the DataFrame.
    
    :param df: pandas DataFrame
    :return: Dictionary with summary statistics
    """
    return df.describe().to_dict()

def correlation_matrix(df):
    """
    Compute and return the correlation matrix of the DataFrame.
    
    :param df: pandas DataFrame
    :return: pandas DataFrame with correlation coefficients
    """
    return df.corr()

def trend_analysis(df, column, window=5):
    """
    Perform a simple moving average trend analysis on a numeric column.
    
    :param df: pandas DataFrame
    :param column: Column name for trend analysis
    :param window: Size of the moving window
    :return: DataFrame with original and trend data
    """
    df[f'{column}_trend'] = df[column].rolling(window=window).mean()
    return df

def customer_segmentation(df):
    """
    Segment customers based on spend and frequency of purchase.
    
    :param df: DataFrame with 'total_spend' and 'purchase_count'
    :return: DataFrame with added 'customer_segment' column
    """
    conditions = [
        (df['total_spend'] > df['total_spend'].quantile(0.75)) & (df['purchase_count'] > df['purchase_count'].quantile(0.75)),
        (df['total_spend'] > df['total_spend'].quantile(0.5)) & (df['purchase_count'] > df['purchase_count'].quantile(0.5)),
        (df['total_spend'] <= df['total_spend'].quantile(0.5)) | (df['purchase_count'] <= df['purchase_count'].quantile(0.5))
    ]
    choices = ['High Value', 'Medium Value', 'Low Value']
    df['customer_segment'] = np.select(conditions, choices, default='Unknown')
    return df