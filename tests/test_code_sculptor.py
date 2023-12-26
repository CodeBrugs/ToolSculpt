# tests/test_code_sculptor.py
import unittest
from src.core.CodeSculptor.code_sculptor import CodeSculptor

class TestCodeSculptor(unittest.TestCase):
    def setUp(self):
        # Configuración inicial común para las pruebas
        self.code_sculptor = CodeSculptor()

    def test_create_template(self):
        # Prueba para la creación de una plantilla por CodeSculptor
        template_name = "Template1"
        template_code = "Código de la plantilla 1"
        template = self.code_sculptor.create_template(template_name, template_code)

        self.assertEqual(template.name, template_name)
        self.assertEqual(template.code, template_code)

    def test_modify_template(self):
        # Prueba para modificar una plantilla existente
        template_name = "Template2"
        template_code = "Código original"
        modified_code = "Código modificado"
        template = self.code_sculptor.create_template(template_name, template_code)

        # Modifica la plantilla y verifica el cambio
        self.code_sculptor.modify_template(template, modified_code)
        self.assertEqual(template.code, modified_code)

    def test_generate_code(self):
        # Prueba para generar código utilizando CodeSculptor
        template_name = "Template3"
        template_code = "Código de la plantilla 3"
        template = self.code_sculptor.create_template(template_name, template_code)

        # Genera código y verifica que sea correcto
        generated_code = self.code_sculptor.generate_code(template)
        self.assertEqual(generated_code, "Código generado basado en Template3")

if __name__ == '__main__':
    unittest.main()

