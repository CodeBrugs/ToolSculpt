# tests/test_tools/test_tool2.py
import unittest
from src.tools.Tool2.tool2_functions import process_data, analyze_data, perform_additional_task

class TestTool2Functions(unittest.TestCase):
    def test_process_data(self):
        # Prueba para la función process_data
        input_data = "example_data"
        result = process_data(input_data)
        self.assertEqual(result, "Tool2 processed the data: A_SPECIAL_TRANSFORMATION")

    def test_analyze_data(self):
        # Prueba para la función analyze_data
        input_data = "example_data"
        result = analyze_data(input_data)
        self.assertEqual(result, "Tool2 analyzed the data: example_data. Alphabetic characters: 11")

    def test_perform_additional_task(self):
        # Prueba para la función perform_additional_task
        result = perform_additional_task()
        self.assertEqual(result, "Tool2 performed an additional task successfully")

if __name__ == '__main__':
    unittest.main()

