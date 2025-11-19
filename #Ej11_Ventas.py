#Ej11_Ventas.py
#CBTIS 89
#3°B Programacion Matutino
#Alumno: Orlando Ferram Najera Tremillo

import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Calculo de Ventas")
ventana.geometry("400x400")

etiqueta_cantidad = tk.Label(ventana, text="Ingresa la cantidad de articulos: ")
etiqueta_cantidad.pack(pady=10)

entrada_cantidad = tk.Entry(ventana, justify="left")
entrada_cantidad.pack(pady=10)

entrada_precio = tk.Entry(ventana, text="Precio de articulos: ")
entrada_precio.pack(pady=10)

entrada_precio = tk.Entry(ventana, justify="left")
entrada_precio.pack(pady=10)

def subtotal():
    try:
        cantidad = float(entrada_cantidad.get())
        precio = float(entrada_precio.get())
        subtotal = cantidad * precio
        etiqueta_resultado.config(text=f"Subtotal{subtotal:.2f}")

    except ValueError:
        messagebox.showerror("Error","Por favor ingresa una cantidad valida")

def Iva():
    try:
        cantidad = float(entrada_cantidad.get())
        precio = float(entrada_precio.get())
        subtotal=cantidad*precio
        iva=subtotal*0.16

        etiqueta_resultado.config(text=f"Iva{iva} ")
    
    except ValueError:
        messagebox.showerror("Error","Por favor ingrese una cantidad valida")

def total():
    try:
        cantidad = float(entrada_cantidad.get())
        precio = float(entrada_precio.get())
        subtotal=cantidad*precio
        iva=subtotal*0.16
        total=subtotal+iva

        etiqueta_resultado.config(text=f"Total{total} ")
    
    except ValueError:
        messagebox.showerror("Error","Por favor ingrese una cantidad valida")

btn_subtotal = tk.Button(ventana, text="Subtotal", command=subtotal)
btn_subtotal.pack(pady=5)

btn_iva = tk.Button(ventana, text="IVA", command=Iva)
btn_iva.pack(pady=5)

btn_total = tk.Button(ventana, text="Total", command=total)
btn_total.pack(pady=5)

etiqueta_resultado = tk.Label(ventana, text="", font=("Arial", 12, "bold"))
etiqueta_resultado.pack(pady=15)

ventana.mainloop()