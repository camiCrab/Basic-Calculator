import tkinter as tk
from tkinter import messagebox

# Función para realizar la operación
def calcular():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        symbol = operation.get()

        if symbol == "+":
            result = a + b
        elif symbol == "-":
            result = a - b
        elif symbol == "*":
            result = a * b
        elif symbol == "/":
            result = a / b
        elif symbol == "%":
            result = a % b
        elif symbol == "**":
            result = a ** b
        elif symbol == "//":
            result = a // b
        else:
            result = "Operación no válida"

        result_label.config(text=f"Resultado: {result}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese números válidos")
    except ZeroDivisionError:
        messagebox.showerror("Error", "División por cero no permitida")

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora")

# Crear los widgets
label1 = tk.Label(root, text="Inserte el primer número")
label1.pack()

entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Inserte el segundo número")
label2.pack()

entry2 = tk.Entry(root)
entry2.pack()

label3 = tk.Label(root, text="Indique la operación (+, -, *, /, %, **, //)")
label3.pack()

operation = tk.Entry(root)
operation.pack()

calculate_button = tk.Button(root, text="Calcular", command=calcular)
calculate_button.pack()

result_label = tk.Label(root, text="Resultado: ")
result_label.pack()

# Ejecutar el bucle principal
root.mainloop()
