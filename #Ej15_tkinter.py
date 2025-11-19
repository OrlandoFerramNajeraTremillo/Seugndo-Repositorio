#Ej15_tkinter.py
#CBTIS89
#3°B Programación
#programa que muestra una lista desplegable con diferentes figuras geometricas y al seleccionar una se muestra la imagen de esa misma
import tkinter as tk
import os
from tkinter import ttk
from PIL import Image, ImageTk
BASE_DIR = r"C:\Users\LTI-1\Documents\imagenes"
figuras = {
    "Cuadrado": os.path.join(BASE_DIR, "cuadrado.png"),
    "Rectángulo": os.path.join(BASE_DIR, "rectangulo.png"),
    "Círculo": os.path.join(BASE_DIR, "triangulo.png"),
    "Triángulo": os.path.join(BASE_DIR, "tringulo 2.png"),
}

def mostrar_imagen(event):
   seleccion = lista_figuras.get(lista_figuras.curselection())
   ruta = figuras.get(seleccion)
   imagen = Image.open(ruta)
   imagen = imagen.resize((200, 200)) # Redimensionar imagen
   imagen_tk = ImageTk.PhotoImage(imagen)
   etiqueta_imagen.config(image=imagen_tk)
   etiqueta_imagen.image = imagen_tk

ventana = tk.Tk()
ventana.title("Visualizador de Figuras")
ventana.geometry("400x400")

titulo = tk.Label(ventana, text="Selecciona una figura:", font=("Arial", 14))
titulo.pack(pady=10)

lista_figuras = tk.Listbox(ventana, font=("Arial", 12), height=4)
for figura in figuras.keys():
   lista_figuras.insert(tk.END, figura)
   lista_figuras.pack()

etiqueta_imagen = tk.Label(ventana)
etiqueta_imagen.pack(pady=20)

lista_figuras.bind("<<ListboxSelect>>", mostrar_imagen)

ventana.mainloop()