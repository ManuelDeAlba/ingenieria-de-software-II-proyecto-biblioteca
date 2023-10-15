import math
from tkinter import *

class Tabla(Frame):
    def __init__(self, root, titulos=[], info=[], tamanos=[]):
        Frame.__init__(self, root)

        self.titulos = titulos
        self.info = info
        self.tamanos = tamanos or [30]*len(self.info)
        self.filasPorPagina = 10
        self.rows = len(self.info)
        # Si no hay filas entonces no hay columnas
        self.columns = len(self.info[0]) if self.rows > 0 else 0
        self.paginas = math.ceil(len(self.info) / self.filasPorPagina)
        self.pagina = 1 if self.rows > 0 else 0

        self.entries = []

        # Rellena la tabla
        self.crear()

        # Botones para cambiar pagina
        frame_botones = Frame(self)
        frame_botones.grid(row=11, column=0, columnspan=max(len(self.titulos), self.columns), pady=10)
        
        self.boton_anterior = Button(frame_botones, text="Anterior", command=lambda: self.cambiarPagina(-1))
        self.boton_anterior.grid(row=0, column=1)
        self.label_paginas = Label(frame_botones, text=f"{self.pagina}/{self.paginas}")
        self.label_paginas.grid(row=0, column=2)
        self.boton_siguiente = Button(frame_botones, text="Siguiente", command=lambda: self.cambiarPagina(1))
        self.boton_siguiente.grid(row=0, column=3)

    def crear(self):
        # Se insertan los titulos
        for x, titulo in enumerate(self.titulos):
            # Se crea el input 
            self.entry = Entry(self, fg='blue', width=self.tamanos[x])

            # Se posiciona y se insertan los datos
            self.entry.grid(row=0, column=x)
            self.entry.insert(END, titulo)

            # Se evita que se pueda escribir
            self.entry.config(state="readonly")
            self.entries.append(self.entry)

        # Se insertan los datos
        for i in range(self.rows):
            for j in range(self.columns):
                # Si está dentro del rango que se tiene que mostrar (paginacion)
                if (self.pagina - 1) * self.filasPorPagina <= i < self.pagina * self.filasPorPagina:
                    # Se crea el input 
                    self.entry = Entry(self, fg='black', width=self.tamanos[j])

                    # Se posiciona y se insertan los datos
                    self.entry.grid(row=1 + i % self.filasPorPagina, column=j)
                    self.entry.insert(END, self.info[i][j])

                    # Se evita que se pueda escribir
                    self.entry.config(state="readonly")
                    self.entries.append(self.entry)

    def cambiarPagina(self, cambio):
        # Se borran los datos anteriores
        for entry in self.entries:
            entry.destroy()

        # Cambia la pagina solo si no se sale de los límites
        if self.pagina + cambio > 0 and self.pagina + cambio <= self.paginas:
            self.pagina += cambio

        # Se cambia el texto de la paginacion
        self.label_paginas.config(text=f"{self.pagina}/{self.paginas}")

        # Crea la nueva tabla con la nueva pagina
        self.crear()
    
    def actualizar(self, info):
        self.info = info

        # Se borran todos los datos anteriores
        for entry in self.entries:
            entry.destroy()
        
        self.entries = []

        # Se actualiza la cantidad de filas y columnas
        self.rows = len(info)
        self.columns = len(info[0]) if self.rows > 0 else 0
        self.pagina = 1 if self.rows > 0 else 0
        # Se calculan las paginas totales
        self.paginas = math.ceil(len(self.info) / self.filasPorPagina)

        # Se cambia el texto de la paginacion
        self.label_paginas.config(text=f"{self.pagina}/{self.paginas}")

        # Se llena la tabla con los datos nuevos
        self.crear()