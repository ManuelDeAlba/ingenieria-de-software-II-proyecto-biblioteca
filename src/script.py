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
    print("Buscar Libros")
    print("1) Titulo")
    print("2) Autor")
    print("3) Genero")
    print("4) Año")
    print("5) Estado")
    tipo = int(input("Buscar por: ")) - 1
    contenido = input("Escribe el texto que quieres buscar: ")

    TIPOS = ["titulo", "autor", "genero", "publicacion", "estado"]

    os.system("cls")

    # Se muestran los libros encontrados
    encontrados = biblioteca.buscarLibros(TIPOS[tipo], contenido)

    if encontrados:
        for libro in encontrados:
            print(libro.mostrarInformacion())
            print("--------------------")
    else:
        print("Libros no encontrados\n")

    os.system("pause")

ejecutando = True
while ejecutando:
    os.system("cls")
    print("¿Que accion deseas realizar?")
    print("1) Agregar libro")
    print("2) Mostrar libros registrados")
    print("3) Buscar libros")
    print("4) Reservar libro")
    print("5) Cancelar reserva de libro")
    print("6) Prestar libro")
    print("7) Devolver libro")
    print("8) Actualizar información de libro")
    print("9) Eliminar libro")
    print("10) Salir")
    opcion = input("Ingresa el número de la opción: ")

    os.system("cls")
    if opcion == "1": agregarLibro()
    elif opcion == "2": mostrarLibros()
    elif opcion == "3": buscarLibros()
    elif opcion == "4": biblioteca.reservarLibro()
    elif opcion == "5": biblioteca.cancelarReservacion()
    elif opcion == "10": ejecutando = False