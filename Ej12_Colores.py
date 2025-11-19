# leilani avitia casarrubias
# Programación 3B T.M.
# muestra una lista para diferentes colores

import tkinter as tk #importar la biblioteca ded tkinter
from tkinter import ttk # caja de texto que manda un mensaje (error, etc)

ventana = tk.Tk()
ventana.title("Cambio de color")
ventana.geometry("400x300")
ventana.resizable(False,False)

def mostrarColor (event):
    Selecion == textCombobox.get ()
    
    if Selecion == "Amarillo":
        colores.config (background = 'yellow')
        color = "yellow"
    elif Selecion == "Azul":
        colores.config (background = "blue")
        color = "blue"
    elif Selecion == "Amazul":
        colores.config (background = "green")
        color = "green"
    elif Selecion == "Morado":
        colores.config (background = "purple")
        color = "purple"
    else:
        colores.config (background= "red")
        color = "red"

opciones =["Amarillo", "Azul", "Amazul", "morado", "rojo"]

textCombobox = ttk.Combobox (ventana, value= opciones, state = "readonly")
textCombobox.pack (pady=2)
textCombobox.bind ('<<ComboboxSelected>>', mostrarColor)

colores = tk.Label (ventana, text="     ",)
colores.pack(pady=2)

text = tk.Label (ventana,text='texto de prueba',font=("Arial",16))
text.pack(pady=20)

Selecion = textCombobox.get ()

ventana.mainloop ()