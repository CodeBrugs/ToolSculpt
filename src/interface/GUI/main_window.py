import tkinter as tk
from tkinter import ttk
from src.interface.GUI.widgets.tool_preview import ToolPreviewWidget  # Ajusta la ruta según la estructura de tus archivos

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tu Aplicación")
        self.geometry("800x600")  # Ajusta el tamaño según tus preferencias
        self.create_widgets()

    def create_widgets(self):
        # Barra de menú (puedes agregar más opciones según sea necesario)
        menu_bar = tk.Menu(self)
        self.config(menu=menu_bar)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Salir", command=self.quit)
        menu_bar.add_cascade(label="Archivo", menu=file_menu)

        # Pestañas (si deseas organizar la interfaz en pestañas)
        notebook = ttk.Notebook(self)

        # Pestaña 1: Vista Previa de Herramienta
        tool_preview_tab = ttk.Frame(notebook)
        tool_preview = ToolPreviewWidget(tool_preview_tab)
        tool_preview.pack(padx=20, pady=20)
        notebook.add(tool_preview_tab, text="Vista Previa")

        # Pestaña 2: Otras Funcionalidades
        other_tab = ttk.Frame(notebook)

        # Ejemplo: Botón para realizar alguna acción
        action_button = ttk.Button(other_tab, text="Realizar Acción", command=self.perform_action)
        action_button.pack(pady=20)

        # Ejemplo: Entrada de texto para configuración
        config_entry = ttk.Entry(other_tab, width=30)
        config_entry.pack(pady=10)

        # Añadir más widgets y funcionalidades según sea necesario

        notebook.add(other_tab, text="Otras Funcionalidades")

        # Añadir más pestañas según sea necesario

        notebook.pack(fill="both", expand=True)

    def perform_action(self):
        # Acción a ejecutar cuando se presiona el botón de "Realizar Acción"
        config_value = ttk.Entry.winfo_string(self.children['.!frame.!notebook.!frame2.!entry'])
        print(f"Realizando acción con configuración: {config_value}")

def main():
    app = MainWindow()
    app.mainloop()

if __name__ == "__main__":
    main()

