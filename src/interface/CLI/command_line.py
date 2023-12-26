import argparse
from src.core.CodeSculptor.code_sculptor import main as code_sculptor_main
# Agrega otras importaciones según sea necesario

def parse_args():
    """
    Configura y analiza los argumentos de línea de comandos.
    """
    parser = argparse.ArgumentParser(description="Interfaz de Línea de Comandos para CodeSculptor")

    # Agrega aquí los argumentos específicos de tu interfaz
    parser.add_argument('--run-codesculptor', action='store_true', help='Ejecutar CodeSculptor')

    return parser.parse_args()

def main():
    """
    Punto de entrada principal de la interfaz de línea de comandos.
    """
    args = parse_args()

    if args.run_codesculptor:
        # Ejecutar la función principal de CodeSculptor
        print("Iniciando CodeSculptor...")
        code_sculptor_main()
        print("CodeSculptor finalizado con éxito.")
        # Puedes agregar más lógica aquí si es necesario

if __name__ == "__main__":
    main()

