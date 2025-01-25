import unittest  
from plte.module import load_data

class TestLoadData(unittest.TestCase):
    
    def test_load_data(self):
        # Load the actual data from the file
        data = load_data("p.txt")
        
        # Read the expected data from an external file (if you have a reference file)
        with open("tests/expected_p.txt", "r") as file:
            expected_data = file.read()
        
        # Assert that the loaded data is equal to the expected data
        self.assertEqual(data.strip(), expected_data.strip())
    
    def test_load_data_line_check(self):
        # Load the actual data from the file
        data = load_data("p.txt")
        
        # Read the first and last lines from the data
        data_lines = data.split("\n")
        first_line = data_lines[0].strip()
        last_line = data_lines[-1].strip()
        
        # Define what the first and last lines of the expected data should be
        expected_first_line = "PROGRAM 1"  # Update with actual first line of expected data
        expected_last_line = "plt.show()"  # Update with actual last line of expected data
        
        # Assert the first and last lines are correct
        self.assertEqual(first_line, expected_first_line)
        self.assertEqual(last_line, expected_last_line)

if __name__ == "__main__":
    unittest.main()
