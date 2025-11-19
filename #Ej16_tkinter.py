#Ej16_tkinter.py
#Orlando Ferram Najera Tremillo 
#3°B Programación 
#programa que muestra una boleta de calificaciones y pide las calificaciones y materia al hacerlo muestra su promedio de cada materia y un promedio general con un messagebox
import tkinter as tk
from tkinter import messagebox

def calcular_promedios():
   total_promedios=0
   materias_validas=0
   for i in range(len(filas)):
      try:
         cal1 = float(filas[i][1].get())
         cal2 = float(filas[i][2].get())
         cal3 = float(filas[i][3].get())
         promedio = (cal1 + cal2 + cal3) / 3
         filas[i][4].config(text=f"{promedio:.2f}")
         total_promedios += promedio
         materias_validas += 1
         nombre=entry_nombre.get()
      except ValueError:
         messagebox.showerror("Error", f"Calificaciones inválidas en la fila {i + 1}")
   if materias_validas > 0:
        promedio_general = total_promedios / materias_validas
        messagebox.showinfo("Promedio General", f"El promedio general de {nombre} es: {promedio_general:.2f}")
# Crear ventana principal
ventana = tk.Tk()
ventana.title("Boleta de Calificaciones")
ventana.resizable(False,False)
# Nombre del alumno
tk.Label(ventana, text="Nombre del alumno:").grid(row=0, column=0, sticky="w")
entry_nombre = tk.Entry(ventana, width=40)
entry_nombre.grid(row=0, column=1, columnspan=4, sticky="we")

# Encabezados de tabla
encabezados = ["Materia", "Unidad 1", "Unidad 2", "Unidad 3", "Promedio"]
for col, encabezado in enumerate(encabezados):
   tk.Label(ventana, text=encabezado, font=('Arial', 10, 'bold')).grid(row=1, column=col, padx=5, pady=5)

# Crear filas para materias (ejemplo: 5 materias)
filas = []
for i in range(3):
    fila = []
   # Materia
    entry_materia = tk.Entry(ventana)
    entry_materia.grid(row=i+2, column=0, padx=5, pady=5)
    fila.append(entry_materia)
   # Calificaciones
    for j in range(1, 4):
      entry_cal = tk.Entry(ventana, width=10)
      entry_cal.grid(row=i+2, column=j, padx=5)
      fila.append(entry_cal)
# Promedio (etiqueta, no editable)
    label_promedio = tk.Label(ventana, text="0.00", width=10, bg="lightgray")
    label_promedio.grid(row=i+2, column=4, padx=5)
    fila.append(label_promedio)
    filas.append(fila)

# Botón para calcular promedios
btn_calcular = tk.Button(ventana, text="Calcular Promedios", command=calcular_promedios)
btn_calcular.grid(row=7, column=0, columnspan=5, pady=10)
ventana.mainloop()