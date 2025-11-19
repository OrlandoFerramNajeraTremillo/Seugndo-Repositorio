#Ej12_Colores.py
#CBTIS 89
#3°B Programacion Matutino
#Alumno: Orlando Ferram Najera Tremillo

import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title("Lista desplegable ComboBox")
ventana.geometry("300x200")

etiqueta = tk.Label(ventana,text="Elije una opcion: ")
etiqueta.pack(pady=10)

opciones = ["Rojo", "Verde", "Azul", "Amarillo", "Naranja"]
ComboColores=ttk.Combobox(ventana,values=opciones,state="readonly")
ComboColores.pack(pady=5)

def mostrar_seleccion():
    Seleccion = ComboColores.get()

    if(Seleccion == "ROJO"):
        etiqueta_colores.config(fg="red")
        color = "red"
        etiqueta_resultado.config(text=f" Has seleccionado el color {Seleccion}", fg=color,bg="black")
    elif(Seleccion == "VERDE"):
        etiqueta_colores.config(fg="green")
        color = "green"
        etiqueta_resultado.config(text=f" Has seleccionado el color {Seleccion}", fg=color,bg="black")
    elif(Seleccion == "AZUL"):
        etiqueta_colores.config(fg="blue")
        color = "blue"
        etiqueta_resultado.config(text=f" Has seleccionado el color {Seleccion}", fg=color,bg="black")
    elif(Seleccion == "AMARILLO"):
        etiqueta_colores.config(fg="yellow")
        color = "yellow"
        etiqueta_resultado.config(text=f" Has seleccionado el color {Seleccion}", fg=color,bg="black")
    elif(Seleccion == "NARANJA"):
        etiqueta_colores.config(fg="orange")
        color = "orange"
        etiqueta_resultado.config(text=f" Has seleccionado el color {Seleccion}", fg=color,bg="black")

def mostrar_seleccion(event):
    seleccion = ComboColores.get()
    etiqueta_resultado.config(text=f"Seleccionaste: {seleccion}")
ComboColores.bind("<<ComboboxSelected>>", mostrar_seleccion)

etiqueta_resultado = tk.Label(ventana, text="Aun no has seleccionado nada")
etiqueta_resultado.pack(pady=20)

etiqueta_colores = tk.Label(text="")
etiqueta_colores.pack(pady=10)

ventana.mainloop()
