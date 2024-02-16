import tkinter as tk
import numpy as np
import sympy as sym
import MatrixCalc as MC
from tkinter import scrolledtext


class MatrixGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("MatrixCalc.offline")

        self.matrix_size_label = tk.Label(root, text="Matrix Größe:")
        self.matrix_size_label.grid(row=0, column=0, padx=10, pady=10)

        self.matrix_size_entry = tk.Entry(root)
        self.matrix_size_entry.grid(row=0, column=1, padx=10, pady=10)

        self.create_matrix_button = tk.Button(root, text="Matrix erstellen", command=self.create_matrix)
        self.create_matrix_button.grid(row=0, column=2, padx=10, pady=10)

        self.matrix_entries = []

        self.submit_button = tk.Button(root, text="Lineare Abhängigkeit prüfen", command=self.check_matrix)
        self.submit_button.grid(row=1, column=1, padx=10, pady=10)

    def create_matrix(self):
        try:
            size = int(self.matrix_size_entry.get())
            if size <= 0:
                raise ValueError("Die Größe der Matrix muss größer als 0 sein.")
            
            # Matrix-Eingabe erstellen
            for i in range(size):
                row_entries = []
                for j in range(size):
                    entry = tk.Entry(self.root, width=5)
                    entry.grid(row=i + 2, column=j, padx=5, pady=5)
                    row_entries.append(entry)
                self.matrix_entries.append(row_entries)
        except ValueError as e:
            tk.messagebox.showerror("Fehler", str(e))
    


    def check_matrix(self):
        matrix = []

        for row_entries in self.matrix_entries:
            row_values = [float(entry.get()) for entry in row_entries]
            matrix.append(row_values)
            
        numpy_matrix = np.array(matrix)
        result = MC.check_linear_dependency(numpy_matrix)

        if result:
            solution_text = self.load_solution_text()
            self.display_solution_text(solution_text)
        else:
            tk.messagebox.showinfo("Ergebnis", "Die Vektoren sind linear unabhängig.")

    def load_solution_text(self):
        try:
            with open('solution_steps.txt', 'r') as file:
                solution_text = file.read()
            return solution_text
        except FileNotFoundError:
            tk.messagebox.showwarning("Warnung", "Die Datei 'solution_text.txt' wurde nicht gefunden.")
        except Exception as e:
            tk.messagebox.showerror("Fehler", f"Fehler beim Laden der Datei: {str(e)}")

    def display_solution_text(self, text):
        solution_text_window = tk.Toplevel(self.root)
        solution_text_window.title("Solution Text")

        solution_text_label = scrolledtext.ScrolledText(solution_text_window, wrap=tk.WORD, width=40, height=10)
        solution_text_label.insert(tk.END, text)
        solution_text_label.pack(padx=10, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = MatrixGUI(root)
    root.mainloop()