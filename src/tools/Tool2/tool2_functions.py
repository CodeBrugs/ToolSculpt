# src/tools/Tool2/tool2_functions.py

def process_data(data):
    """
    Procesa los datos utilizando la lógica específica de Tool2.

    Parameters:
    - data (str): Datos de entrada.

    Returns:
    - result (str): Resultado del procesamiento.
    """
    # Operación específica: Invertir los datos
    inverted_data = data[::-1]
    
    # Operación específica: Aplicar una transformación especial
    processed_data = inverted_data.upper()  # Convertir a mayúsculas como ejemplo
    
    result = f"Tool2 aplicó una transformación especial: {processed_data}"
    return result

def analyze_data(data):
    """
    Analiza los datos utilizando la lógica específica de Tool2.

    Parameters:
    - data (str): Datos de entrada.

    Returns:
    - analysis (str): Resultado del análisis.
    """
    # Operación específica: Contar la cantidad de caracteres alfabéticos
    alphabet_count = sum(c.isalpha() for c in data)
    
    # Operación específica: Realizar un análisis basado en la cantidad de caracteres alfabéticos
    if alphabet_count > len(data) // 2:
        analysis = "Tool2 encontró más de la mitad de los caracteres como alfabéticos."
    else:
        analysis = "Tool2 encontró menos de la mitad de los caracteres como alfabéticos."
    
    return analysis

# Operación específica: Agregar una función para realizar una tarea adicional
def perform_additional_task():
    """
    Realiza una tarea adicional específica de Tool2.

    Returns:
    - task_result (str): Resultado de la tarea.
    """
    # Operación específica: Realizar una tarea adicional
    task_result = "Tool2 realizó una tarea adicional con éxito."
    return task_result

# Puedes agregar más funciones y operaciones específicas según sea necesario

