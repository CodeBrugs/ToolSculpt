# src/tools/Tool2/tool2_main.py
import argparse
import os
from tool2_functions import process_data, analyze_data, perform_additional_task

def process_file(input_file, output_file):
    """
    Procesa un archivo de entrada y guarda el resultado en un archivo de salida.

    Parameters:
    - input_file (str): Ruta al archivo de entrada.
    - output_file (str): Ruta al archivo de salida.
    """
    try:
        # Validar que el archivo de entrada exista
        if not os.path.isfile(input_file):
            raise FileNotFoundError(f"No se encontró el archivo de entrada: {input_file}")

        with open(input_file, 'r') as f:
            input_data = f.read()
            processed_result = process_data(input_data)

        with open(output_file, 'w') as f:
            f.write(processed_result)

        print(f"Procesamiento mágico completado. Resultado guardado en {output_file}")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error mágico durante el procesamiento: {e}")

def main():
    parser = argparse.ArgumentParser(description="Herramienta 2 - Procesamiento de datos")
    parser.add_argument('--input', type=str, help='Ruta al archivo de entrada mágico')
    parser.add_argument('--output', type=str, help='Ruta al archivo de salida mágico')
    parser.add_argument('--perform-task', action='store_true', help='Realizar tarea adicional mágica')

    args = parser.parse_args()

    if args.input and args.output:
        process_file(args.input, args.output)
    elif args.perform_task:
        additional_task_result = perform_additional_task()
        print(f"Resultado de la tarea adicional mágica: {additional_task_result}")
    else:
        print("Uso mágico: tool2_main.py (--input INPUT_FILE --output OUTPUT_FILE) | (--perform-task)")

if __name__ == "__main__":
    main()

