import argparse
from CodeSculptor.code_templates.template1 import main as template1_main
from CodeSculptor.code_templates.template2 import ejecutar_programa as template2_ejecutar_programa

def parse_args():
    """
    Configura y analiza los argumentos de línea de comandos.
    """
    parser = argparse.ArgumentParser(description="Code Sculptor - Herramientas de Automatización")

    # Argumentos específicos para tu orquestador
    parser.add_argument('--template1', action='store_true', help='Ejecutar Template 1')
    parser.add_argument('--template2', action='store_true', help='Ejecutar Template 2')
    parser.add_argument('--archivo_entrada', type=str, help='Ruta al archivo de entrada')
    parser.add_argument('--archivo_salida', type=str, help='Ruta al archivo de salida')

    return parser.parse_args()

def main():
    """
    Punto de entrada principal del orquestador.
    """
    args = parse_args()

    if args.template1:
        # Ejecutar el main de template1.py
        print("Ejecutando Template 1...")
        template1_main()
    elif args.template2:
        # Ejecutar la función ejecutar_programa de template2.py con argumentos personalizados
        if args.archivo_entrada and args.archivo_salida:
            print(f"Ejecutando Template 2 con archivo de entrada {args.archivo_entrada} y archivo de salida {args.archivo_salida}...")
            template2_ejecutar_programa(args.archivo_entrada, args.archivo_salida)
        else:
            print("Error: Se requieren las rutas a archivos de entrada y salida para Template 2.")
    else:
        print("No se proporcionó ninguna acción. Usa --help para ver las opciones disponibles.")

if __name__ == "__main__":
    main()

