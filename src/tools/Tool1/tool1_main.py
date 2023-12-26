# src/tools/Tool1/tool1_main.py
import argparse
from tool1_functions import process_data, analyze_data, perform_specific_task

def process_file(input_file, output_file):
    """
    Procesa un archivo de entrada y guarda el resultado en un archivo de salida.

    Parameters:
    - input_file (str): Ruta al archivo de entrada.
    - output_file (str): Ruta al archivo de salida.
    """
    try:
        with open(input_file, 'r') as f:
            input_data = f.read()
            processed_result = process_data(input_data)

        with open(output_file, 'w') as f:
            f.write(processed_result)

        print(f"Procesamiento completado. Resultado guardado en {output_file}")

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo de entrada {input_file}")
    except Exception as e:
        print(f"Error durante el procesamiento: {e}")

def main():
    parser = argparse.ArgumentParser(description="Herramienta 1 - Procesamiento de datos")
    parser.add_argument('--input', type=str, help='Ruta al archivo de entrada')
    parser.add_argument('--output', type=str, help='Ruta al archivo de salida')
    parser.add_argument('--perform-task', action='store_true', help='Realizar tarea específica')

    args = parser.parse_args()

    if args.input and args.output:
        process_file(args.input, args.output)
    elif args.perform_task:
        specific_task_result = perform_specific_task()
        print(f"Resultado de la tarea específica: {specific_task_result}")
    else:
        print("Uso: tool1_main.py (--input INPUT_FILE --output OUTPUT_FILE) | (--perform-task)")

if __name__ == "__main__":
    main()

