#!/usr/bin/python3

import tkinter as tk
from tkinter import filedialog, messagebox 


class SimpleTextEditor:



    #Constructor
    def __init__(self, ventana:tk.Tk):
        #Recibo la ventana, en este caso la ventana root y la pongo como propiedad de clase
        self.ventana = ventana
        # Creo el area de texto con la clase de tkinter Text() y le paso la ventana donde quiero poner el widget
        self.area_de_texto = tk.Text(self.ventana)

        # Represento el widget de Text con el metodo pack y los parametros fill=tk.BOTH (el eje X y el eje Y) y el parametro expand=1 porque si no 
        # pongo esto el eje Y no se rellena completamente.
        self.area_de_texto.pack(fill=tk.BOTH, expand=1)

        self.archivo_abierto_actualmente = ''



    # Metodos de la clase
        

    def salir(self):
        """Este metodo muestra una ventana que dice 'Estas seguro de que deseas salir?' Y da las opciones de OK o Cancel, y si das a Ok sale.
        """

        respuesta = messagebox.askokcancel("Salir", "Estas seguro de que deseas salir?")
        if respuesta:
            self.ventana.destroy()

    
    def abrir_archivo(self):
        # Obtengo la ruta absoluta del archivo que selecciona el usuario.
        ruta_absoluta = filedialog.askopenfilename()
        # Si el archivo tiene contenido, lo abro y lo vuelco en el Text()
        if ruta_absoluta:
            # Limpiamos el contenido del area de texto por si ya habia texto escrito
            self.area_de_texto.delete("1.0", tk.END)
            with open(ruta_absoluta, 'r') as archivo:
                # Cargamos el contenido del archivo
                self.area_de_texto.insert("1.0", archivo.read())
            self.archivo_abierto_actualmente = ruta_absoluta


    def nuevo_archivo(self):
        """Tenemos que limpiar la ruta del archivo actual y limpiar la pantalla"""

        # Limpio la ruta del archivo actual 
        self.archivo_abierto_actualmente = ''
        # Limpio el editor
        self.area_de_texto.delete("1.0", tk.END) # ELimino desde linea 1 caracter 0 hasta el final.


    def guardar_archivo(self):
        """Guardamos el archivo con el nombre que corresponda"""

        # Vemos a ver si el archivo es nuevo, o si ya tenia un nombre y solo lo estamos editando
        if not self.archivo_abierto_actualmente: # Si es una ruta vacia
            ruta_nuevo_archivo = filedialog.asksaveasfilename()
            with open(ruta_nuevo_archivo, 'w') as nuevo_archivo:
                nuevo_archivo.write(self.area_de_texto.get("1.0", tk.END))
        else: # Si la ruta del archivo existe
            with open(self.archivo_abierto_actualmente, 'w') as archivo_actual:
                archivo_actual.write(self.area_de_texto.get("1.0", tk.END))
            

    def todo(self):
        messagebox.showinfo("Advertencia","Vaya, parece que esta funcion no se ha implementado todavia. Pronto estara disponible!")