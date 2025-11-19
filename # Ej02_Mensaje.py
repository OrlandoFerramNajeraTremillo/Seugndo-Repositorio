# Ej02_Mensaje.py
# Programa que simula el envío de un mensaje
#Autor : Orlando Ferram Najera Tremillo

import tkinter as tk

ventana = tk.Tk()
ventana.title("Ejemplo de Widgets en Tkinter")
ventana.geometry("300x200")

etiqueta =tk.Label(ventana,text="Escribe algo:",font=("Arial", 12))
etiqueta.pack(pady=10)

entrada = tk.Entry(ventana, font=("Arial", 12))
entrada.pack(pady=5)

def mostrar_texto():
    texto = entrada.get()
    etiqueta_resultado.config(text=f"Escribiste: {texto}")

boton = tk.Button(ventana, text="Mostrar Texto", command=mostrar_texto)
boton.pack(pady=10)

etiqueta_resultado = tk.Label(ventana, text="", font=("Arial", 12),fg="blue")
etiqueta_resultado.pack(pady=5)

ventana.mainloop()