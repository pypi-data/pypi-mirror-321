import sys
import os
import unittest
import pandas as pd

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))  # Add src/ to path

# Import the required functions directly
from topsis_Urvi_102203720.topsis import process_inputs, compute_topsis


class TestTOPSIS(unittest.TestCase):

    def test_process_inputs(self):
        dataframe = pd.read_csv('102203720-data.csv')  # Reading the actual input data file
        weight_str = '0.1,0.2,0.3,0.2,0.2'  # Example weights (5 values)
        impact_str = '+,+,-,+,+'  # Example impacts (5 values)

        weight_list, impact_list = process_inputs(dataframe, weight_str, impact_str)

        # Check if the weight and impact lists are processed correctly
        self.assertEqual(weight_list, [0.1, 0.2, 0.3, 0.2, 0.2])
        self.assertEqual(impact_list, ['+', '+', '-', '+', '+'])

    def test_compute_topsis(self):
        dataframe = pd.read_csv('102203720-data.csv')  # Reading the actual input data file
        weights = [0.1, 0.2, 0.3, 0.2, 0.2]  # Example weights (5 values)
        impacts = ['+', '+', '-', '+', '+']  # Example impacts (5 values)

        result = compute_topsis(dataframe, weights, impacts)

        # Check if the 'Topsis Score' and 'Rank' columns are added
        self.assertIn('Topsis Score', result.columns)
        self.assertIn('Rank', result.columns)

        # Save the result to a CSV file
        result.to_csv('102203720-result.csv', index=False)
        print("Results saved to '102203720-result.csv'")

        # Optionally, check that the result CSV file is created
        self.assertTrue(os.path.exists('102203720-result.csv'))

        # Add more assertions based on your expected output
        # You can also load the saved result CSV and verify its contents, if needed
        result_data = pd.read_csv('102203720-result.csv')
        self.assertIn('Topsis Score', result_data.columns)
        self.assertIn('Rank', result_data.columns)


if __name__ == '__main__':
    unittest.main()
