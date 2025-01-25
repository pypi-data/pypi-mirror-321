import unittest
import pandas as pd
import os
from topsis import topsis

class TestTopsis(unittest.TestCase):

    def setUp(self):
        self.input_data = pd.DataFrame({
            'Object': ['A', 'B', 'C', 'D'],
            'Criterion1': [250, 200, 300, 275],
            'Criterion2': [50, 40, 45, 50],
            'Criterion3': [4, 3, 5, 4.5],
            'Criterion4': [400, 350, 450, 425]
        })
        self.weights = [1, 1, 1, 1]
        self.impacts = ['+', '-', '+', '+']
        self.result_file = "test-result.csv"

    def test_topsis_function(self):
        result = topsis(self.input_data, self.weights, self.impacts)

        self.assertIn('Topsis Score', result.columns, "Topsis Score column missing!")
        self.assertIn('Rank', result.columns, "Rank column missing!")

        self.assertEqual(len(result['Rank'].unique()), len(result), "Ranks are not unique!")

    def test_file_output(self):
        result = topsis(self.input_data, self.weights, self.impacts)
        result.to_csv(self.result_file, index=False)

        self.assertTrue(os.path.exists(self.result_file), "Result file not created!")

        saved_result = pd.read_csv(self.result_file)
        self.assertListEqual(list(saved_result.columns), list(self.input_data.columns) + ['Topsis Score', 'Rank'])

    def tearDown(self):
        if os.path.exists(self.result_file):
            os.remove(self.result_file)

if _name_ == '_main_':
    unittest.main()