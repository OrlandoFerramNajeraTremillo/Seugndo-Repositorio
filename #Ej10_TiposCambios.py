#Ej10_TiposCambios.py
#CBTIS 89
#3°B Programacion Matutino
#Alumno: Orlando Ferram Najera Tremillo

import tkinter as tk
from tkinter import messagebox 

ventana = tk.Tk()
ventana.title("Divisas ")
ventana.geometry("300x300")

etiqueta_cantidad = tk.Label(ventana, text="Ingresa la cantidad. ")
etiqueta_cantidad.pack(pady=10)

entrada_cantidad = tk.Entry(ventana,justify="left")
entrada_cantidad.pack(pady=10)

def Dolares():
    try:
        cantidad=float(entrada_cantidad.get())
        dolar = cantidad * 0.0547
        etiqueta_resultado.config(text=f"Dolares: $ {dolar:.2f}")
    except ValueError:
        messagebox.showerror("Error","Por favor ingresa una cantidad valida.")

def Euros():
    try:
        cantidad=float(entrada_cantidad.get())
        euro = cantidad * 0.047
        etiqueta_resultado.config(text=f"Euros: $ {euro:.2f}")
    except ValueError:
        messagebox.showerror("Error","Por favor ingresa una cantidad valida.")

def Libras():
    try:
        cantidad=float(entrada_cantidad.get())
        libra = cantidad * 0.041
        etiqueta_resultado.config(text=f"Libras: $ {libra:.2f}")
    except ValueError:
        messagebox.showerror("Error","Por favor ingresa una cantidad valida.")

def Yen():
    try:
        cantidad=float(entrada_cantidad.get())
        yen = cantidad * 8.22
        etiqueta_resultado.config(text=f"Yenes: $ {yen:.2f}")
    except ValueError:
        messagebox.showerror("Error","Por favor ingresa una cantidad valida.")

btn_dolares = tk.Button(ventana, text="Dolar", command=Dolares)
btn_dolares.pack(pady=5)

btn_euros = tk.Button(ventana, text="Euro", command=Euros)
btn_euros.pack(pady=5)

btn_libras = tk.Button(ventana, text="Libra", command=Libras) 
btn_libras.pack(pady=5)

btn_yen = tk.Button(ventana, text="Yen", command=Yen)
btn_yen.pack(pady=5)

etiqueta_resultado = tk.Label(ventana, text="",font=("Arial", 12, "bold"))
etiqueta_resultado.pack(pady=15)

ventana.mainloop()
