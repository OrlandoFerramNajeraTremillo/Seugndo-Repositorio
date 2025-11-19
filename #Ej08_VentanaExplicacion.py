#Ej08_VentanaExplicacion.py
#CBTIS 89
#3°B Programacion Matutino
#Alumno: Orlando Ferram Najera Tremillo

#Importamos lqa libreria Tkinter y le damos un alias "tk"
import tkinter as tk

#Crear la ventana principal 
ventana = tk.Tk() #Intancia principal de la aplicacion

#Configurar el titulo de la ventana
ventana.title("Ventana de saludo")

#Definir el tamaño de la ventana (ancho x alto)
ventana.geometry("400x300")

#Agregar un texto (etiqueta)
etiqueta = tk.Label(ventana, text="Hola buenos dias",font=("Arial", 16))
etiqueta.pack(pady=20) #Pack coloca el elemento en la ventana y pady de espacio 

#Agregar boton
def saludar():
    etiqueta.config(text=" Que rollo, como va tu dia? ")

boton = tk.Button(ventana, text="Saludar", command=saludar)
boton.pack(pady=10)

#Ejecutar el bucle principal de la aplicacion 
ventana.mainloop()
