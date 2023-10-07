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

        # print("\nLibro agregado con éxito\n")
        # print(libro.obtenerInformacion(), "\n")
        # os.system("pause")

    def obtenerLibros(self):
        lista = []

        if self.libros:
            for libro in self.libros:
                lista.append(libro.obtenerInformacion().split("\n"))

        return lista

    def mostrarLibros(self):
        if not self.libros:
            print("No hay libros registrados\n")
        else:
            print("Libros encontrados\n")
            print("--------------------")

            for libro in self.libros:
                print(libro.obtenerInformacion())
                print("--------------------")

            print("")

    def buscarLibros(self, tipo, contenido):
        self.encontrados = []

        for libro in self.libros:
            if (
                (tipo.lower() == "titulo" and normalizarTexto(contenido) in normalizarTexto(libro.titulo).split(" ")) or
                (tipo.lower() == "autor" and normalizarTexto(contenido) in normalizarTexto(libro.autor).split(" ")) or
                (tipo.lower() == "genero" and normalizarTexto(contenido) in normalizarTexto(libro.genero).split(" ")) or
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

    def editarLibro(self, titulo):
        librosEncontrados = [libro for libro in self.libros if libro.titulo.lower() == titulo.lower()]

        if not librosEncontrados:
            print("\nLibro no encontrado\n")
            os.system("pause")
            return
        
        libro = librosEncontrados[0]

        print("\nLibro encontrado:\n" + libro.obtenerInformacion() + "\n")

        os.system("pause")

        os.system("cls")
        print("Campo a editar")
        print("1) Titulo")
        print("2) Autor")
        print("3) Genero")
        print("4) Año")
        print("5) Cancelar")
        opc = int(input("¿Qué deseas editar?: "))

        while opc < 1 and opc > 5:
            print("Ingresa una opción válida\n")
            os.system("pause")

        if opc == 5: return

        contenidoNuevo = input("Introduce el contenido nuevo: ")

        if opc == 1: libro.titulo = contenidoNuevo
        elif opc == 2: libro.autor = contenidoNuevo
        elif opc == 3: libro.genero = contenidoNuevo
        elif opc == 4: libro.publicacion = contenidoNuevo

        guardarDatosCSV([libro.toCSV() for libro in self.libros], archivo)

        print("\nLibro actualizado")
        print(libro.obtenerInformacion(), "\n")
        
        os.system("pause")

    def eliminarLibro(self, libroABorrar):
        # Se elimina el libro que se le pase por parametro
        self.libros = [libro for libro in self.libros if libro != libroABorrar]

        guardarDatosCSV([libro.toCSV() for libro in self.libros], archivo)