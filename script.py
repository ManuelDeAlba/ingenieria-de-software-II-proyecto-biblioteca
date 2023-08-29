import os

class Biblioteca:
	def __init__(self):
		self.libros = [] #! Hacer los cambios para que lo guarde en un .csv
	def agregarLibro(self, libro):
		self.libros.append(libro)
	def mostrarLibros(self):
		if not self.libros:
			print("No hay libros registrados")
		else:
			for libro in self.libros:
				libro.mostrarInformacion()
				print("--------------------")

		os.system("pause")

class Libro:
	def __init__(self, titulo, autor, genero, publicacion):
		self.titulo = titulo
		self.autor = autor
		self.genero = genero
		self.publicacion = publicacion
	def mostrarInformacion(self):
		print(f"Titulo: {self.titulo}\nAutor: {self.autor}\nGenero: {self.genero}\nPublicacion: {self.publicacion}")

biblioteca = Biblioteca()

def agregarLibro():
	titulo = input("Introduce el titulo del libro: ")
	autor = input("Introduce el autor del libro: ")
	genero = input("Introduce el genero del libro: ")
	publicacion =  input("Introduce el año de publicacion: ")

	libro = Libro(titulo, autor, genero, publicacion)
	biblioteca.agregarLibro(libro)

def mostrarLibros():
	biblioteca.mostrarLibros()

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
	elif opcion == "10": ejecutando = False