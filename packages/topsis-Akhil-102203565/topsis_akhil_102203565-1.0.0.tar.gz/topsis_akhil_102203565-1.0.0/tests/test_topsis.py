import unittest
import pandas as pd
import os
from topsis.topsis import topsis

class TestTOPSIS(unittest.TestCase):
    def test_topsis(self):
        input_file = "test_data.csv"
        output_file = "test_result.csv"

        # Create sample test file
        data = {
            "Alternative": ["A1", "A2", "A3", "A4"],
            "C1": [250, 200, 300, 275],
            "C2": [16, 20, 25, 22],
            "C3": [12, 15, 10, 8]
        }
        df = pd.DataFrame(data)
        df.to_csv(input_file, index=False)

        # Run TOPSIS
        topsis(input_file, "1,1,1", "+,+,-", output_file)

        # Check if output file exists
        self.assertTrue(os.path.exists(output_file))

        # Clean up
        os.remove(input_file)
        os.remove(output_file)

if __name__ == "__main__":
    unittest.main()
