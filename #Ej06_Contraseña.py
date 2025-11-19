#Ej06_Contraseña.py

import tkinter as tk
from tkinter import messagebox
from tkinter import font

import tkinter as tk
from tkinter import messagebox

#funcion para abrir la ventana principal despues del login 
def abrir_ventana_principal():
    ventana_principal = tk.Toplevel()
    ventana_principal.title("Ventana Principal")
    ventana_principal.geometry("300x200")
    etiqueta = tk.Label(ventana_principal, text="Bienvenido al sistema", font=("Helvetica",14))
    etiqueta.pack(pady=50)

#funcion para verificar el login 
def verificar_login():
    usuario = entrada_usuario.get()
    password = entrada_password.get()

    if usuario == "admin" and password == "1234":
        messagebox.showinfo("Acceso", "Acceso correcto")
        ventana_login.destroy()
        abrir_ventana_principal()
    else:
        messagebox.showerror("Acceso", "Acceso denegado")

#crear ventana de login 
ventana_login = tk.Tk()
ventana_login.title("Sistema de Acceso")
ventana_login.geometry("400x250")
ventana_login.configure(bg="#ffffff")

#etiquetas de texto 
etiqueta_usuario = tk.Label(ventana_login, text="Ingrese su usuario:", font=("Helvetica",10), bg="#ffffff")
etiqueta_usuario.pack(pady=5)
entrada_usuario = tk.Entry(ventana_login, font=("Helvetica",10))
entrada_usuario.pack(pady=5)

etiqueta_password = tk.Label(ventana_login, text="Ingrese su contraseña:", font=("Helvetica",10), bg="#ffffff")
etiqueta_password.pack(pady=5)
entrada_password = tk.Entry(ventana_login, show="*", font=("Helvetica",10))
entrada_password.pack(pady=5)

#boton para verificar login 
boton_verificar = tk.Button(ventana_login, text="Iniciar Sesión", command=verificar_login, font=("Helvetica",10), bg="#007fff", fg="white", width=15)
boton_verificar.pack(pady=15)

ventana_login.mainloop()