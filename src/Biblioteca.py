import os

from Libro import *
from utils import *

script_dir = os.path.dirname(__file__) # Obtiene la ruta de este archivo
archivo = os.path.join(script_dir, "biblioteca.csv") # example.csv

class Biblioteca:
    def __init__(self):
        self.libros = []

        self.cargarDatos()

    # Se insertan los datos del csv al arreglo de libros
    def cargarDatos(self):
        datos = leerDatosCSV(archivo)
        if datos:
            for libro in datos:
                self.libros.append(Libro(*libro))

    def cambiarEstado(self, libroAReservar, nuevoEstado):
        if libroAReservar.estado == LIBRO_ESTADOS[nuevoEstado]: # Si se queda con el mismo estado
            raise Exception("ERROR_ESTADO")
        else: # Si encuentra el libro, le pone el nuevo estado (0: no disponible, 1: disponible)
            libroAReservar.estado = LIBRO_ESTADOS[nuevoEstado]

            # Guarda los libros con los cambios que se hayan hecho
            guardarDatosCSV([libro.toCSV() for libro in self.libros], archivo)

    def agregarLibro(self, libro):
        self.libros.append(libro)
        guardarDatosCSV([libro.toCSV() for libro in self.libros], archivo)

    def obtenerLibros(self):
        lista = []

        if self.libros:
            for libro in self.libros:
                lista.append(libro.obtenerInformacion().split("\n"))

        return lista
    
    def obtenerCamposLibros(self):
        lista = []

        if self.libros:
            for libro in self.libros:
                lista.append(libro.toCSV())

        return lista

    def buscarLibros(self, tipo, contenido):
        self.encontrados = []

        for libro in self.libros:
            if (
                (tipo.lower() == "titulo" and normalizarTexto(contenido) in normalizarTexto(libro.titulo)) or
                (tipo.lower() == "autor" and normalizarTexto(contenido) in normalizarTexto(libro.autor)) or
                (tipo.lower() == "genero" and normalizarTexto(contenido) in normalizarTexto(libro.genero)) or
                (tipo.lower() == "publicacion" and normalizarTexto(contenido) == normalizarTexto(str(libro.publicacion))) or
                (tipo.lower() == "estado" and normalizarTexto(contenido) == normalizarTexto(libro.estado))
            ):
                self.encontrados.append(libro)

        return self.encontrados
    
    def reservarLibro(self, libroAReservar):
        try:
            self.cambiarEstado(libroAReservar, 0)
        except Exception as err:
            if str(err) == "ERROR_ESTADO":
                return "El libro ya está reservado"

    def cancelarReservacion(self, libroACancelar):
        try:
            self.cambiarEstado(libroACancelar, 1)
        except Exception as err:
            if str(err) == "ERROR_ESTADO":
                return "El libro ya está disponible"

    def editarLibro(self, libroAEditar, nuevaInformacion):
        libroAEditar.titulo = nuevaInformacion["titulo"]
        libroAEditar.autor = nuevaInformacion["autor"]
        libroAEditar.genero = nuevaInformacion["genero"]
        libroAEditar.publicacion = nuevaInformacion["publicacion"]

        guardarDatosCSV([libro.toCSV() for libro in self.libros], archivo)

    def eliminarLibro(self, libroABorrar):
        # Se elimina el libro que se le pase por parametro
        self.libros = [libro for libro in self.libros if libro != libroABorrar]

        guardarDatosCSV([libro.toCSV() for libro in self.libros], archivo)