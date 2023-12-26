import os
import sys
import statistics

def cargar_datos(ruta_archivo):
    """
    Carga datos desde un archivo.

    Parameters:
    - ruta_archivo (str): Ruta al archivo de datos.

    Returns:
    - datos (list): Lista de datos cargados.
    """
    datos = []
    try:
        with open(ruta_archivo, 'r') as archivo:
            for linea in archivo:
                # Procesa cada línea según el formato de tus datos
                dato = linea.strip()
                datos.append(float(dato))  # Convierte a float para cálculos
    except FileNotFoundError:
        print(f"¡Error! El archivo {ruta_archivo} no existe.")
    except Exception as e:
        print(f"¡Error inesperado al cargar datos: {e}")

    return datos

def procesar_datos(datos):
    """
    Procesa los datos cargados.

    Parameters:
    - datos (list): Lista de datos a procesar.

    Returns:
    - resultados (dict): Resultados del procesamiento.
    """
    resultados = {
        'total_datos': len(datos),
        'promedio': statistics.mean(datos),
        'mediana': statistics.median(datos),
        'desviacion_estandar': statistics.stdev(datos),
        'minimo': min(datos),
        'maximo': max(datos),
        'suma_total': sum(datos),
        'rango': max(datos) - min(datos),
        'varianza': statistics.variance(datos),
        # Agrega más estadísticas según tus necesidades
    }

    return resultados

def mostrar_resultados(resultados):
    """
    Muestra los resultados por consola.

    Parameters:
    - resultados (dict): Resultados a mostrar.
    """
    print("Resultados del Procesamiento:")
    for clave, valor in resultados.items():
        print(f"{clave}: {valor}")

def guardar_resultados(resultados, ruta_salida):
    """
    Guarda los resultados en un archivo.

    Parameters:
    - resultados (dict): Resultados a guardar.
    - ruta_salida (str): Ruta al archivo de salida.
    """
    try:
        with open(ruta_salida, 'w') as archivo:
            for clave, valor in resultados.items():
                archivo.write(f"{clave}: {valor}\n")
        print(f"Resultados guardados en {ruta_salida}")
    except Exception as e:
        print(f"¡Error inesperado al guardar resultados: {e}")

def main():
    """
    Punto de entrada de la herramienta.

    Agrega la lógica específica de tu herramienta aquí.
    """
    print("¡Hola, CodeSculptor!")

    # Rutas a archivos de entrada y salida (personaliza según tu necesidad)
    ruta_entrada = "datos_entrada.txt"
    ruta_salida = "resultados_salida.txt"

    # Carga datos
    datos = cargar_datos(ruta_entrada)

    # Procesa datos
    if datos:
        resultados = procesar_datos(datos)

        # Muestra resultados por consola
        mostrar_resultados(resultados)

        # Guarda resultados
        guardar_resultados(resultados, ruta_salida)

if __name__ == "__main__":
    main()

