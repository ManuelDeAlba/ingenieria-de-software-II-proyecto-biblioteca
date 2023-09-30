import os

from Biblioteca import *
from Libro import *

biblioteca = Biblioteca()

def agregarLibro():
    print("Agregar libro\n")
    titulo = input("Introduce el titulo del libro: ")
    autor = input("Introduce el autor del libro: ")
    genero = input("Introduce el genero del libro: ")
    publicacion =  input("Introduce el año de publicacion: ")

    libro = Libro(titulo, autor, genero, publicacion)
    biblioteca.agregarLibro(libro)

def mostrarLibros():
    biblioteca.mostrarLibros()
    os.system("pause")

def buscarLibros():
    TIPOS = ["titulo", "autor", "genero", "publicacion", "estado"]

    tipo = len(TIPOS)
    while tipo >= len(TIPOS):
        os.system("cls")
        print("Buscar Libros")
        print("1) Titulo")
        print("2) Autor")
        print("3) Genero")
        print("4) Año")
        print("5) Estado")
        tipo = int(input("Buscar por: ")) - 1

    contenido = input("Escribe el texto que quieres buscar: ")

    os.system("cls")

    # Se muestran los libros encontrados
    encontrados = biblioteca.buscarLibros(TIPOS[tipo], contenido)

    if encontrados:
        print("Libros encontrados\n")
        print("--------------------")
        
        for libro in encontrados:
            print(libro.obtenerInformacion())
            print("--------------------")

        print("")
    else:
        print("Libros no encontrados\n")

    os.system("pause")

def reservarLibro():
    print("Reservar libro\n")

    if not biblioteca.libros:
        print("No hay libros registrados\n")
        return
    
    titulo = input("Introduce el nombre del libro a reservar: ")
    biblioteca.reservarLibro(titulo)

def cancelarLibro():
    print("Cancelar libro\n")

    if not biblioteca.libros:
        print("No hay libros registrados\n")
        return
    
    titulo = input("Introduce el nombre del libro a cancelar: ")
    biblioteca.cancelarReservacion(titulo)

def editarLibro():
    print("Editar libro\n")

    if not biblioteca.libros:
        print("No hay libros registrados\n")
        return
    
    titulo = input("Introduce el nombre del libro a editar: ")
    biblioteca.editarLibro(titulo)

def eliminarLibro():
    print("Eliminar libro\n")

    if not biblioteca.libros:
        print("No hay libros registrados\n")
        return
    
    titulo = input("Introduce el nombre del libro a eliminar: ")
    biblioteca.eliminarLibro(titulo)

ejecutando = True
while ejecutando:
    os.system("cls")
    print("¿Que accion deseas realizar?")
    print("1) Agregar libro")
    print("2) Mostrar libros registrados")
    print("3) Buscar libros")
    print("4) Reservar libro")
    print("5) Cancelar reserva de libro")
    print("6) Editar información de libro")
    print("7) Eliminar libro")
    print("8) Salir")
    opcion = input("Ingresa el número de la opción: ")

    os.system("cls")
    if opcion == "1": agregarLibro()
    elif opcion == "2": mostrarLibros()
    elif opcion == "3": buscarLibros()
    elif opcion == "4": reservarLibro()
    elif opcion == "5": cancelarLibro()
    elif opcion == "6": editarLibro()
    elif opcion == "7": eliminarLibro()
    elif opcion == "8": ejecutando = False