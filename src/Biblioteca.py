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

    def cambiarEstado(self, nuevoEstado):
        if not self.libros:
            print("No hay libros registrados\n")
            return
        
        titulo = input("Introduce el nombre del libro a reservar: ")

        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                # Si encuentra el libro, le pone el nuevo estado (0: no disponible, 1: disponible)
                libro.estado = LIBRO_ESTADOS[nuevoEstado]

                # Se muestra el libro actualizado
                print("\nEstado actualizado\n")
                print(libro.mostrarInformacion(),"\n")
                os.system("pause")

        # Guarda los libros con los cambios que se hayan hecho
        guardarDatosCSV([libro.toCSV() for libro in self.libros], archivo)

    def agregarLibro(self, libro):
        self.libros.append(libro)
        guardarDatosCSV([libro.toCSV() for libro in self.libros], archivo)

    def mostrarLibros(self):
        if not self.libros:
            print("No hay libros registrados")
        else:
            for libro in self.libros:
                print(libro.mostrarInformacion())
                print("--------------------")

    def buscarLibros(self, tipo, contenido):
        self.encontrados = []

        for libro in self.libros:
            if (
                (tipo == "titulo" and contenido.lower() in libro.titulo.lower()) or
                (tipo == "autor" and contenido.lower() in libro.autor.lower()) or
                (tipo == "genero" and contenido.lower() in libro.genero.lower()) or
                (tipo == "publicacion" and contenido == str(libro.publicacion)) or
                (tipo == "estado" and libro.estado.lower() == contenido.lower())
            ):
                self.encontrados.append(libro)

        return self.encontrados
    
    def reservarLibro(self):
        self.cambiarEstado(0)

    def cancelarReservacion(self):
        self.cambiarEstado(1)