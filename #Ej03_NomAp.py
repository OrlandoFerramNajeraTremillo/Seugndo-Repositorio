#Ej03_NomAp.py

import tkinter as tk 

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mostrar Nombre Completo")
ventana.geometry("350x250")

#Etiqueta y entrada para el nombre
etiqueta_nombre = tk.Label(ventana, text="Nombre:",font=("Arial", 12))
etiqueta_nombre.pack(pady=(10, 0))
entrada_nombre = tk.Entry(ventana, font=("Arial", 12))
entrada_nombre.pack(pady=5)

#Etiqueta y entrada para el apellido
etiqueta_apellido = tk.Label(ventana, text="Apellido:",font=("Arial", 12))
etiqueta_apellido.pack(pady=(10, 0))
entrada_apellido = tk.Entry(ventana, font=("Arial", 12))
entrada_apellido.pack(pady=5)

#Funcion al presionar el boton
def mostrar_nombre_completo():
    nombre = entrada_nombre.get()
    apellido = entrada_apellido.get()
    etiqueta_resultado.config(text=f"Nombre Completo: {nombre} {apellido}")

boton = tk.Button(ventana, text="Mostrar el Nombre", command=mostrar_nombre_completo) 
boton.pack(pady=10)

#Etiqueta para mostrar el resultado 
etiqueta_resultado = tk.Label(ventana, text="", font=("Arial", 12), fg="green")
etiqueta_resultado.pack(pady=10)

#Iniciar el bucle principal de la ventana
ventana.mainloop()
