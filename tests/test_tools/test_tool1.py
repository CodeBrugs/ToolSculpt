# tests/test_tools/test_tool1.py
import unittest
from src.tools.Tool1.tool1_functions import process_data, analyze_data, perform_specific_task

class TestTool1Functions(unittest.TestCase):
    def test_process_data(self):
        # Prueba para la función process_data
        input_data = "example_data"
        result = process_data(input_data)
        self.assertEqual(result, "Tool1 processed the data: EXAMPLE_DATA")

    def test_analyze_data(self):
        # Prueba para la función analyze_data
        input_data = "example_data"
        result = analyze_data(input_data)
        self.assertEqual(result, "Tool1 analyzed the data: example_data")

    def test_perform_specific_task(self):
        # Prueba para la función perform_specific_task
        result = perform_specific_task()
        self.assertEqual(result, "Tool1 performed a specific task successfully")

if __name__ == '__main__':
    unittest.main()

