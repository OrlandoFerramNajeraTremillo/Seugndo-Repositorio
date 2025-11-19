#Examen2_NajeraTremillo.py

import tkinter as tk
from tkinter import messagebox

def calcular_sueldo():
    nombre = entrada_nombre.get()
    try:
        sueldo = float(entrada_sueldo.get())
        meses = int(entrada_meses.get())
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa valores numéricos válidos")
        return

    # Validación de rango de meses
    if meses < 0 or meses > 12:
        messagebox.showerror("Error", "Los meses deben estar entre 0 y 12")
        return

    # Calcular sueldo por meses
    sueldo_meses = sueldo * meses

    # Calcular aguinaldo
    if meses > 3:
        aguinaldo = sueldo / 2
    else:
        aguinaldo = 0

    # Calcular subtotal
    subtotal = sueldo_meses + aguinaldo

    # Calcular bono anual según tipo
    tipo = bono.get()
    if tipo == 1:
        bono_anual = subtotal * 0.10
    elif tipo == 2:
        bono_anual = subtotal * 0.05
    else:
        bono_anual = 0

    # Sueldo total
    total = subtotal + bono_anual

    # Mostrar resultados
    resultado.config(text=f"Trabajador: {nombre}\n"
                          f"Sueldo por mes: ${sueldo:,.2f}\n"
                          f"Sueldo por {meses} meses: ${sueldo_meses:,.2f}\n"
                          f"Aguinaldo: ${aguinaldo:,.2f}\n"
                          f"Subtotal: ${subtotal:,.2f}\n"
                          f"Bono anual: ${bono_anual:,.2f}\n"
                          f"Sueldo TOTAL anual: ${total:,.2f}")

# Ventana principal
ventana = tk.Tk()
ventana.title("Escribe aquí tu nombre completo")
ventana.geometry("450x420")
ventana.configure(bg="#ffffff")

# Entradas
tk.Label(ventana, text="Nombre del trabajador:", bg="#ffffff").pack()
entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack(pady=5)

tk.Label(ventana, text="Sueldo mensual:", bg="#ffffff").pack()
entrada_sueldo = tk.Entry(ventana)
entrada_sueldo.pack(pady=5)

tk.Label(ventana, text="Meses trabajados:", bg="#ffffff").pack()
entrada_meses = tk.Entry(ventana)
entrada_meses.pack(pady=5)

# Radio buttons para tipo de bono
tk.Label(ventana, text="Seleccione tipo de bono anual:", bg="#ffffff").pack(pady=5)
bono = tk.IntVar()
tk.Radiobutton(ventana, text="Completo (10%)", variable=bono, value=1, bg="#ffffff").pack()
tk.Radiobutton(ventana, text="Parcial (5%)", variable=bono, value=2, bg="#ffffff").pack()
tk.Radiobutton(ventana, text="Sin bono (0%)", variable=bono, value=3, bg="#ffffff").pack()

# Botón
tk.Button(ventana, text="Calcular Sueldo Total", command=calcular_sueldo, bg="#007fff", fg="white").pack(pady=15)

# Resultado
resultado = tk.Label(ventana, text="", bg="#ffffff", justify="left")
resultado.pack()

ventana.mainloop()