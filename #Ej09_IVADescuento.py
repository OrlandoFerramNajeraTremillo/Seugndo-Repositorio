#Ej09_IVADescuento.py
#CBTIS 89
#3°B Programacion Matutino
#Alumno: Orlando Ferram Najera Tremillo

#Importamos la biblioteca tkinter, que permite crear interfases graficas en python
import tkinter as tk
from tkinter import messagebox

#FUNCIONES PRINCIPALES

#Funciona para calcular el IVA ( impuesto al valor agregado 16% )
def calcular_iva():
    try:
        #Obtenemos el valor que el usuario escribio en la caja de texto
        cantidad = float(entrada_cantidad.get())

        #Calculamos el 16% de IVA
        iva = cantidad * 0.16

        #Mostramos el resultado en la etiqueta de resultados
        etiqueta_resultado.config(text=f"IVA 16%: ${iva:.2f}")

    #si el usuario no ingresa un numero; mostramos la etiqueta de resultados
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa una cantidad valida.")

    #Funcion para calcular el 10% de descuento
def calcular_descuento():
    try:
        #Obtenemos el valor que el usuario escribio en la caja de texto
        cantidad = float(entrada_cantidad.get())

        #Calculamos el 16% de descuento
        descuento = cantidad * 0.10

        #Mostramos el resultado en la etiqueta de resultados
        etiqueta_resultado.config(text=f"Descuento del 10%: ${descuento:.2f}")

    #si el usuario no ingresa un numero; mostramos la etiqueta de resultados
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa una cantidad valida.")

    #Funcion para calcular el total a pagar considerando el iva y el descuento 
def calcular_total():
    try:
        #Obtenemos el valor que el usuario escribio en la caja de texto
        cantidad = float(entrada_cantidad.get())

        #Calculamos el IVA y el descuento
        iva = cantidad * 0.16
        descuento = cantidad * 0.10

        #Calculamos el total a pagar
        total = cantidad + iva - descuento

        #Mostramos el resultado en la etiqueta de resultados
        etiqueta_resultado.config(text=f"Total a pagar: ${total:.2f}")

        #si el usuario no ingresa un numero; mostramos mostramos un mensaje de error
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa una cantidad valida.")

 #INTERFAS GRAFICA DE LA VENTANA PRINCIPAL

#Creamos la ventana principal
ventana = tk.Tk() #Incia la aplicacion grafica
ventana.title("Calcular iva y descuento") #Titulo de la ventana
ventana.geometry("300x250") #Tamaño de la ventana (ancho/alto)
ventana.resizable(False, False) #Evita que el usuario cambie el tamaño de la ventana

#ETIQUETA  Y CAJA DE TEXTO

#Creamos una etiqueta que indica que debe escribir el usuario
etiqueta_cantidad = tk.Label(ventana, text="Ingresa la cantidad:")
etiqueta_cantidad.pack(pady=10) # .pack() coloca el elemento y pady de un margen vertical

#Caja de texto donde se escribira la cantidad
entrada_cantidad = tk.Entry(ventana,justify="center")   #C¿Justify centra el texxto
entrada_cantidad.pack()  #Se agrega aa la ventana

#Botones de accion 

#Puedes buscar los codigos de los colores en esta pagina https://python-chartes.com/es/colores/

#Boton que calcula el IVA
btn_iva = tk.Button(
    ventana,
    text="Calcular IVA",
    command= calcular_iva,
    bg="yellow", #Color de fondo (amarillo) color de letra (azul)
)
btn_iva.pack(pady=5)

#Boton que calcula el descuento
btn_descuento = tk.Button(
    ventana,
    text="Calcular 10% Descuento",
    command = calcular_descuento,
    bg="blue", #Color de letra (Azul)
)
btn_descuento.pack(pady=5)

#Boton que calcula el total a pagar
btn_total = tk.Button(
    ventana,
    text ="Calcular Total a pagar",
    command = calcular_total #Color de fondo (azul) color de letra (blanco)
)
btn_iva.pack(pady=5)

#Etiqueta de resultados

#Aqui se mostrara el resultado despues de presionar un boton
etiqueta_resultado = tk.Label(
    ventana,
    text="", #Vacia al inicio
    font=("Arial",12,"bold") #Tamaño y estilo de la letra
)
etiqueta_resultado.pack(pady=15)

#Incio del programa 

#Inicia el ciclo principal de la aplicacion 
#Este ciclo mantiene la ventana abierta y esperando interaccion del usuario

ventana.mainloop()