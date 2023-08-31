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

		os.system("pause")
  
	def reservarLibro(self):
		os.system("pause")
		if not self.libros:
			print("No hay libros registrados")
		else:
			titulo_libro = input("Introduce el nombre del libro a reservar: ")
			libro_encontrado = None   
			for libro in self.libros:
				if libro.titulo.lower() == titulo_libro.lower() and libro.estado=="Disponible":
					libro_encontrado = libro
					libro.estado = "No disponible"