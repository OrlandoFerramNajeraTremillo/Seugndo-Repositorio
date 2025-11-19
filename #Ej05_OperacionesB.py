#Ej05_OperacionesB.py

import tkinter as tk

#Funcion para sumar 
def sumar():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        suma = num1 + num2
        resultado.config(text=f"Resultado: {suma}")
    except ValueError:
        resultado.config(text="Por favor, ingresa solo números")

# Función para restar
def restar():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        resta = num1 - num2
        resultado.config(text=f"Resultado: {resta}")
    except ValueError:
        resultado.config(text="Por favor, ingresa solo números")

# Función para multiplicar
def multiplicar():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        multiplicacion = num1 * num2
        resultado.config(text=f"Resultado: {multiplicacion}")
    except ValueError:
        resultado.config(text="Por favor, ingresa solo números")

# Función para dividir
def dividir():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        if num2 != 0:
            division = num1 / num2
            resultado.config(text=f"Resultado: {division}")
        else:
            resultado.config(text="No se puede dividir entre cero")
    except ValueError:
        resultado.config(text="Por favor, ingresa solo números")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora Básica")
ventana.geometry("350x300")

# Entradas
entrada1 = tk.Entry(ventana, font=("Arial", 12))
entrada2 = tk.Entry(ventana, font=("Arial", 12))
entrada1.pack(pady=5)
entrada2.pack(pady=5)

# Botones de operaciones
boton_sumar = tk.Button(ventana, text="Sumar", command=sumar)
boton_sumar.pack(pady=5)

boton_restar = tk.Button(ventana, text="Restar", command=restar)
boton_restar.pack(pady=5)

boton_multiplicar = tk.Button(ventana, text="Multiplicar", command=multiplicar)
boton_multiplicar.pack(pady=5)

boton_dividir = tk.Button(ventana, text="Dividir", command=dividir)
boton_dividir.pack(pady=5)

# Resultado
resultado = tk.Label(ventana, text="Resultado:", font=("Arial", 12), fg="blue")
resultado.pack(pady=10)

# Ejecutar la aplicación
ventana.mainloop() 