#!/usr/bin/python3

"""Proyecto: Editor de texto.


Vamos a crear un editor de texto simple. Este editor va a tener las siguientes funciones:

1) Crear un nuevo archivo.
2) Abrir un archivo.
3) Guardar un archivo.
4) Salir.


"""


# Comenzamos importando tkinter

import tkinter as tk
import simpletext as st
from tkinter import PhotoImage
from simpletext import *
# Importo filedialog (para el explorador de archivos) y messagebox para las ventanas informativas flotantes

#Definimos la ventana principal o padre
root = tk.Tk()
root.title("Proyecto: Editor de texto.")
root.geometry("700x500")
img = PhotoImage(file='icon.png')
root.iconphoto(False, img)

editor = st.SimpleTextEditor(root)


# Creamos la barra de menu y la asignamos a la ventana principal
barra_menu_principal = tk.Menu(root)
root.config(menu=barra_menu_principal) # Le decimos a la ventana root cual es el menu que tenemos que incorporar

# Creo un menu para meter en la barra de menu principal. tearoff para que no se despegue el desplegable de la ventana
archivo_menu = tk.Menu(barra_menu_principal, tearoff=0)

ayuda_menu = tk.Menu(barra_menu_principal, tearoff=0)
ayuda_menu.add_command(label="Manual de usuario", command=editor.todo)

# Defino las subopciones que tendra el menu
archivo_menu.add_command(label="Nuevo", command = editor.nuevo_archivo)
archivo_menu.add_command(label="Abrir", command = editor.abrir_archivo)
archivo_menu.add_command(label="Guardar", command = editor.guardar_archivo)
archivo_menu.add_command(label="Salir", command=editor.salir)

# Y agrego la entrada del menu a la barra de menu (barra_menu_principal)
barra_menu_principal.add_cascade(label="Archivo", menu=archivo_menu) # Agrego a la barra de menu principal el submenu de Archivo
barra_menu_principal.add_cascade(label="Ayuda", menu=ayuda_menu)

# Esto es para poder interactuar con la ventana.
root.mainloop()