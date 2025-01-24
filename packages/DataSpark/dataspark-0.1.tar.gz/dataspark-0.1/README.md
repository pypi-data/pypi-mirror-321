# DataSpark

A Python-based tool for empowering SMEs with data analytics.

## Features

- **Cost-Effective Data Analysis**: Affordable access and scalable plans for all business sizes.
- **Ease of Use for Non-Tech Users**: 
  - User-friendly interface with wizards for all tasks.
  - No-code customization for dashboards and reports.
  - Pre-made templates for common SME analytics.
- **Immediate Insights without Data Expertise**:
  - Automated analysis suggestions based on data characteristics.
  - Clear interpretations in plain business language.
- **Scalability with Simplicity**: 
  - Performance optimization using Dask for larger datasets while maintaining a simple interface.
- **Offline and Local Data Handling**:
  - Full functionality without internet for privacy and remote work.
  - Local data security to enhance control.
- **Quick Onboarding**:
  - Easy installation process.
  - Interactive tutorials within the application.

## Data Handling Module

### Capabilities

- **Data Loading**: Supports CSV, JSON, and Excel formats.
- **Data Saving**: Save data back to CSV, JSON, or Excel.
- **Data Cleaning**: Basic cleaning operations like removing NaN values.
- **Data Merging**: Combine datasets based on common keys.
- **Data Type Conversion**: Convert column types to suit analysis needs.
- **Feature Engineering**: Apply custom transformations or use predefined functions for feature creation.
- **Large Dataset Scaling**: Utilizes Dask for memory-efficient operations on large datasets.

### Usage

```python
from data_handling import load_data, save_data, clean_data, merge_datasets, convert_data_type, apply_feature_engineering

# Load data
df = load_data('path/to/your/file.csv', 'csv')

# Clean data
cleaned_df = clean_data(df)

# Merge data
df_merged = merge_datasets(df1, df2, on='common_column')

# Convert data type
df = convert_data_type(df, 'column_name', 'new_type')

# Apply feature engineering
df = apply_feature_engineering(df, your_feature_engineering_function)

# Scale large datasets
scaled_df = scale_large_dataset(df)