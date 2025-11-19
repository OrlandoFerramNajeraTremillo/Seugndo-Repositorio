#Ej14_Descuentos.py
#CBTIS 89
#3°B Programacion Matutino
#Alumno: Orlando Ferram Najera Tremillo

import tkinter as tk

ventana = tk.Tk()
ventana.title("Calcular descuento")
ventana.geometry("400x300")
ventana.resizable(False,False)

etiqueta_cantidad = tk.Label(ventana, text="Ingresa la cantidad")
etiqueta_cantidad.pack(pady=10)

entrada_cantidad = tk.Entry(ventana,justify="center")
entrada_cantidad.pack()

def ejecutar_radio():
    opcion = seleccion.get()

    if opcion == 1:
        cantidad = float(entrada_cantidad.get())
        descuento = cantidad * 0.05
        etiqueta_resultado.config(text=f" Hola estimado cliente usted obtuvo un descuento del 5% su total a pagar es: {cantidad - descuento} ")
    elif opcion == 2:
        cantidad = float(entrada_cantidad.get())
        descuento = cantidad * 0.10
        etiqueta_resultado.config(text=f" Hola estimado cliente usted obtuvo un descuento del 10% su total a pagar es: {cantidad - descuento} ")
    elif opcion == 3:
        cantidad = float(entrada_cantidad.get())
        descuento = cantidad * 0.15
        etiqueta_resultado.config(text=f" Hola estimado cliente usted obtuvo un descuento del 15% su total a pagar es: {cantidad - descuento} ")

seleccion = tk.IntVar()

radio_boton1 = tk.Radiobutton(ventana, text="Descuento del 5%", variable=seleccion, value=1,command=ejecutar_radio)
radio_boton2 = tk.Radiobutton(ventana, text="Descuento del 10%", variable=seleccion, value=1,command=ejecutar_radio)
radio_boton3 = tk.Radiobutton(ventana, text="Descuento del 15%", variable=seleccion, value=1,command=ejecutar_radio)

radio_boton1.pack(pady=10)
radio_boton2.pack(pady=10)
radio_boton3.pack(pady=10)

etiqueta_resultado = tk.Label(ventana, text="",wraplength=350, justify="left")
etiqueta_resultado.pack(pady=20)

ventana.mainloop()