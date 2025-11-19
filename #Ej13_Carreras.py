#Ej13_Carreras.py
#CBTIS 89
#3°B Programacion Matutino
#Alumno: Orlando Ferram Najera Tremillo

import tkinter as tk
from tkinter import ttk

ventana=tk.Tk()
ventana.title("Lista desplegable ComboBox")
ventana.geometry("300x200")

etiqueta=tk.Label(ventana,text="Elije una opcion:")
etiqueta.pack(pady=10)

opciones=["Arquitectura","ARH","Construccion","Contabilidad","CIA","Comercio electronico","Mecatronica","Programacion"]
ComboColores=ttk.Combobox(ventana,values=opciones,state="readoly")
ComboColores.pack(pady=5)

def mostrar_seleccion(event):
    seleccion = ComboColores.get()
    etiqueta_resultado.config(text=f"Seleccionaste: {seleccion}")

ComboColores.bind("<<ComboboxSelected>>", mostrar_seleccion)

etiqueta_resultado = tk.Label(ventana)
etiqueta_resultado.pack(pady=20)

ventana.mainloop()