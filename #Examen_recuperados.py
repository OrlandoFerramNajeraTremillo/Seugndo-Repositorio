#CBTIS 89 
## Orlando Ferram Najera Tremillo

import tkinter as tk
from tkinter import messagebox

def calcular_total():
    try:
        nombre = txtNombre.get()
        cantidad = int(txtCantidad.get())
        edad = int(txtEdad.get())
        descuento = descuento_var.get()

        precio_llanta = 950  # precio unitario
        subtotal = cantidad * precio_llanta
        iva = subtotal * 0.16
        descuento_aplicado = subtotal * (descuento / 100)

        # Calcular incentivo por edad
        if 50 <= edad <= 59:
            incentivo = precio_llanta / 2  # media llanta
        elif edad >= 60:
            incentivo = precio_llanta  # una llanta completa
        else:
            incentivo = 0

        total = subtotal + iva - descuento_aplicado - incentivo

        lblResultado.config(text=f"""
Nombre del cliente: {nombre}
Subtotal: ${subtotal:.2f}
IVA: ${iva:.2f}
Descuento aplicado: ${descuento_aplicado:.2f}
Incentivo por edad: ${incentivo:.2f}
-----------------------------
TOTAL A PAGAR: ${total:.2f}
""")

    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa valores válidos.")

# Ventana principal
ventana = tk.Tk()
ventana.title("HORIZON TIRE - Cálculo de compra")

tk.Label(ventana, text="Nombre del cliente:").grid(row=0, column=0, sticky="w")
txtNombre = tk.Entry(ventana)
txtNombre.grid(row=0, column=1)

tk.Label(ventana, text="Cantidad de llantas:").grid(row=1, column=0, sticky="w")
txtCantidad = tk.Entry(ventana)
txtCantidad.grid(row=1, column=1)

tk.Label(ventana, text="Edad del cliente:").grid(row=2, column=0, sticky="w")
txtEdad = tk.Entry(ventana)
txtEdad.grid(row=2, column=1)

tk.Label(ventana, text="Porcentaje de descuento:").grid(row=3, column=0, sticky="w")

descuento_var = tk.IntVar()
tk.Radiobutton(ventana, text="10%", variable=descuento_var, value=10).grid(row=3, column=1, sticky="w")
tk.Radiobutton(ventana, text="20%", variable=descuento_var, value=20).grid(row=4, column=1, sticky="w")
tk.Radiobutton(ventana, text="0%", variable=descuento_var, value=0).grid(row=5, column=1, sticky="w")
descuento_var.set(0)

tk.Button(ventana, text="Calcular total", command=calcular_total).grid(row=6, column=0, columnspan=2, pady=10)

lblResultado = tk.Label(ventana, text="", justify="left")
lblResultado.grid(row=7, column=0, columnspan=2) 

ventana.mainloop()