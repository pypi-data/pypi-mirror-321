import unittest
from analysis.analysis_functions import describe_data, correlation_matrix, trend_analysis, customer_segmentation
import pandas as pd
import numpy as np

class TestAnalysis(unittest.TestCase):
    def setUp(self):
        self.sample_data = pd.DataFrame({
            'A': [1, 2, 3],
            'B': [4, 5, 6],
            'total_spend': [100, 200, 300],
            'purchase_count': [1, 2, 3]
        })

    def test_describe_data(self):
        result = describe_data(self.sample_data)
        self.assertIsInstance(result, dict)

    def test_correlation_matrix(self):
        corr = correlation_matrix(self.sample_data)
        self.assertIsInstance(corr, pd.DataFrame)

    def test_trend_analysis(self):
        df = trend_analysis(self.sample_data, 'A')
        self.assertTrue('A_trend' in df.columns)

    def test_customer_segmentation(self):
        segmented = customer_segmentation(self.sample_data)
        self.assertTrue('customer_segment' in segmented.columns)

if __name__ == '__main__':
    unittest.main()