# tests/test_auto_magico.py
import unittest
from src.core.AutoMagico.auto_magico import AutoMagico

class TestAutoMagico(unittest.TestCase):
    def setUp(self):
        # Configuración inicial común para las pruebas
        self.auto_magico = AutoMagico()

    def test_create_tool(self):
        # Prueba para la creación de una herramienta por AutoMagico
        tool_name = "Tool1"
        tool_description = "Una herramienta mágica"
        tool = self.auto_magico.create_tool(tool_name, tool_description)

        self.assertEqual(tool.name, tool_name)
        self.assertEqual(tool.description, tool_description)

    def test_train_auto_magico(self):
        # Prueba para entrenar AutoMagico
        training_data = ["data1", "data2", "data3"]
        self.auto_magico.train(training_data)

        # Verifica que AutoMagico ha aprendido correctamente
        self.assertIn("data1", self.auto_magico.learned_data)
        self.assertIn("data2", self.auto_magico.learned_data)
        self.assertIn("data3", self.auto_magico.learned_data)

    def test_generate_tool(self):
        # Prueba para generar una herramienta con AutoMagico
        tool_name = "Tool2"
        generated_tool = self.auto_magico.generate_tool(tool_name)

        # Verifica que la herramienta generada tenga el nombre correcto
        self.assertEqual(generated_tool.name, tool_name)

if __name__ == '__main__':
    unittest.main()

