import unittest
from data_handling import load_data, save_data, clean_data, merge_datasets, convert_data_type, apply_feature_engineering, example_feature_engineering
import pandas as pd
import os
import numpy as np

class TestDataHandling(unittest.TestCase):
    
    def setUp(self):
        self.sample_data = pd.DataFrame({
            'A': [1, 2, 3],
            'B': [4, 5, 6],
            'age': [25, 35, 60],
            'income': [50000, 75000, 100000]
        })
        self.sample_data.to_csv('test_data.csv', index=False)

    def test_load_data_csv(self):
        df = load_data('test_data.csv')
        self.assertEqual(len(df), 3)
        
    def test_save_data_csv(self):
        save_data(self.sample_data, 'test_output.csv')
        self.assertTrue(os.path.exists('test_output.csv'))
        
    def test_clean_data(self):
        df = pd.DataFrame({
            'A': [1, None, 3],
            'B': [4, 5, 6]
        })
        cleaned_df = clean_data(df)
        self.assertEqual(len(cleaned_df), 2)

    def test_merge_datasets(self):
        df1 = pd.DataFrame({'id': [1, 2], 'value': ['a', 'b']})
        df2 = pd.DataFrame({'id': [2, 3], 'value2': ['x', 'y']})
        merged_df = merge_datasets(df1, df2, on='id', how='inner')
        self.assertEqual(len(merged_df), 1)  # Only id=2 matches

    def test_convert_data_type(self):
        df = pd.DataFrame({'A': ['1', '2', '3']})
        df = convert_data_type(df, 'A', 'int64')
        self.assertEqual(df['A'].dtype, np.int64)

    def test_apply_feature_engineering(self):
        df = self.sample_data.copy()
        engineered_df = apply_feature_engineering(df, example_feature_engineering)
        self.assertIn('age_group', engineered_df.columns)
        self.assertIn('normalized_income', engineered_df.columns)
        self.assertEqual(engineered_df['age_group'].dtype, 'category')

    def tearDown(self):
        # Clean up test files
        if os.path.exists('test_data.csv'):
            os.remove('test_data.csv')
        if os.path.exists('test_output.csv'):
            os.remove('test_output.csv')

if __name__ == '__main__':
    unittest.main()