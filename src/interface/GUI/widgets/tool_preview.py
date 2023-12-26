import tkinter as tk
from tkinter import ttk

class ToolPreviewWidget(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.create_widgets()

    def create_widgets(self):
        # Etiqueta para la vista previa de la herramienta
        label = ttk.Label(self, text="Vista Previa de Tu Herramienta", font=("Arial", 18, "bold"))
        label.pack(pady=10)

        # Descripción o detalles de la herramienta
        description_label = ttk.Label(self, text="Descripción:")
        description_label.pack(pady=5)

        description_text = tk.Text(self, height=4, width=40)
        description_text.insert(tk.END, "Tu herramienta realiza las siguientes funciones:\n\n1. Funcionalidad A\n2. Funcionalidad B")
        description_text.config(state=tk.DISABLED)  # Hace que el área de texto sea de solo lectura
        description_text.pack(pady=10)

        # Botón para simular la ejecución de la herramienta
        run_button = ttk.Button(self, text="Ejecutar Herramienta", command=self.run_tool)
        run_button.pack(pady=10)

    def run_tool(self):
        # Acción a ejecutar cuando se presiona el botón
        result_label = ttk.Label(self, text="¡La herramienta se ejecutó con éxito!", foreground="green")
        result_label.pack(pady=10)

def main():
    # Crear la ventana principal de la aplicación
    root = tk.Tk()
    root.title("Vista Previa de Tu Herramienta")

    # Crear y mostrar el widget de vista previa de la herramienta
    tool_preview = ToolPreviewWidget(root)
    tool_preview.pack(padx=20, pady=20)

    # Iniciar el bucle de eventos de Tkinter
    root.mainloop()

if __name__ == "__main__":
    main()

