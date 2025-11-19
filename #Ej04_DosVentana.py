#Ej04_DosVentana.py

import tkinter as tk
from tkinter import Toplevel

#Crear la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Ventana Principal")
ventana_principal.geometry("300x200")

#Funcion para abrir la primera ventana hija (Nombre y Apellidos)
def abrir_ventana_nombre():
    ventana_nombre = Toplevel(ventana_principal)
    ventana_nombre.title("Nombre y Apellidos")
    ventana_nombre.geometry("250x150")

    etiqueta_nombre = tk.Label(ventana_nombre, text="Nombre: Orlando Ferram", font=("Arial", 12))
    etiqueta_nombre.pack(pady=5)

    etiqueta_apellidos = tk.Label(ventana_nombre, text="Apellidos: Najera Tremillo", font=("Arial", 12))
    etiqueta_apellidos.pack(pady=5)

    boton_cerrar = tk.Button(ventana_nombre, text="Cerrar", command=ventana_nombre.destroy)
    boton_cerrar.pack(pady=10)

#Funcion para abrir la segunda ventana hija (Mensaje)
def abrir_ventana_mensaje():
    ventana_mensaje = Toplevel(ventana_principal)
    ventana_mensaje.title("Mensaje")
    ventana_mensaje.geometry("250x120")

    etiqueta_mensaje = tk.Label(ventana_mensaje, text="Cerrar", command=ventana_mensaje.destroy)
    etiqueta_mensaje.pack(pady=20)

    boton_cerrar = tk.Button(ventana_mensaje, text="Cerrar", command=ventana_mensaje.destroy)
    boton_cerrar.pack()

#Botones en la ventana principal
boton1 = tk.Button(ventana_principal, text="Mostrar Nombre", command=abrir_ventana_nombre)
boton1.pack(pady=10)

boton2 = tk.Button(ventana_principal, text="Mostrar Mensaje", command=abrir_ventana_mensaje)
boton2.pack(pady=10)

#Iniciar el loop principal
ventana_principal.mainloop()