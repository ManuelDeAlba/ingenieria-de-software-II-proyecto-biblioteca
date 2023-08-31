class Libro:
    def __init__(self, titulo, autor, genero, publicacion, estado="Disponible"):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.publicacion = publicacion
        self.estado = estado

    def mostrarInformacion(self):
        return f"Titulo: {self.titulo}\nAutor: {self.autor}\nGenero: {self.genero}\nPublicacion: {self.publicacion}\nEstado: {self.estado}"
	
    def toCSV(self):
        return [self.titulo, self.autor, self.genero, self.publicacion, self.estado]