import unittest
import os
import pandas as pd
from topsis.topsis import topsis

class TestTopsisWithLocalFile(unittest.TestCase):

    def setUp(self):
        # Input CSV file
        self.input_file = pd.read_csv("C:/Users/aarus/OneDrive/Desktop/102216107-data.csv")
        self.result_file = "102216107-result.csv"

    def test_topsis_with_local_file(self):
        # Set weights and impacts
        weights = "1,1,1,2"
        impacts = "+,+,-,+"

        # Run the TOPSIS function
        topsis(self.input_file, weights, impacts, self.result_file)

        # Check if the result file is created
        self.assertTrue(os.path.exists(self.result_file))

        # Validate the result file's content
        result_df = pd.read_csv(self.result_file)
        self.assertIn("Topsis Score", result_df.columns)
        self.assertIn("Rank", result_df.columns)
        print(f"Test passed. Results stored in {self.result_file}")

if __name__ == "__main__":
    unittest.main()
