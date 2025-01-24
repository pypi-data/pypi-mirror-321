import unittest
from machine_learning.ml_models import simple_regression
import pandas as pd
import numpy as np

class TestML(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({
            'feature1': [1, 2, 3, 4, 5],
            'feature2': [2, 4, 5, 4, 5],
            'target': [1, 2, 3, 4, 5]
        })

    def test_simple_regression(self):
        model, predictions, mse = simple_regression(self.df, 'target', ['feature1', 'feature2'])
        
        # Check if model is fitted
        self.assertTrue(hasattr(model, 'coef_'))
        self.assertTrue(hasattr(model, 'intercept_'))
        
        # Check if predictions are of correct type and shape
        self.assertIsInstance(predictions, np.ndarray)
        self.assertEqual(len(predictions), 1)  # Since we're testing with only one feature

        # MSE should be a number
        self.assertIsInstance(mse, float)

if __name__ == '__main__':
    unittest.main()