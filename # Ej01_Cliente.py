# Ej01_Cliente.py
#3°B Programacion Matutino
#Autor: Olrando Ferram Najera Tremillo 

import tkinter as tk

#Crear la ventana principal 
ventana = tk.Tk()
ventana.title("Sistema ed Venta de Aplicaciones")

#Agregar un campo de texto para ingresar el nombre del cliente
etiqueta_cliente = tk.Label (ventana, text="Nombre del Cliente:")
etiqueta_cliente.pack()
entrada_cliente = tk.Entry(ventana)
entrada_cliente.pack()

#Agregar un boton para confirmar la venta 
boton_confirmar = tk.Button(ventana,text="Confirmar Venta")
boton_confirmar.pack()

#Iniciar la ventana
ventana.mainloop()
