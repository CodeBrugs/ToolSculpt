# ToolSculpt/src/tools/Tool3/tool3_main.py
from tool3_functions import generate_code, analyze_data

def run_tool3():
    """
    Función principal que demuestra el uso de las funciones de la Tool3 de ToolSculpt.
    """
    user_input = input("Ingresa datos para la Tool3: ")

    # Generar código basado en los datos
    generated_code = generate_code(user_input)
    print(f"\nTool3 Output - Generated Code: {generated_code}")

    # Analizar los datos
    analysis_result = analyze_data(user_input)
    print(f"Tool3 Output - Analysis Result: {analysis_result}")

if __name__ == "__main__":
    print("Bienvenido a la Tool3 de ToolSculpt\n")
    run_tool3()

