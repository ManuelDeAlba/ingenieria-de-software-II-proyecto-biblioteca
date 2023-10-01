from tkinter import *

from Biblioteca import *
from Libro import *
from Tabla import *

biblioteca = Biblioteca()

root = Tk()
root.title("Biblioteca")
root.resizable(0, 0)

# Titulo de la aplicacion
Label(root, text="Biblioteca", font=('Arial', 16, 'bold')).pack(pady=10)

# Mostrar libros (Tabla con los libros)
libros = biblioteca.obtenerLibros()
datos_tabla = [["Indice: " + str(x), *y] for x, y in enumerate(libros)]
tabla = Tabla(root, datos_tabla)
tabla.pack()

# Frame para poner los botones con las acciones
frame_botones = Frame(root)
frame_botones.pack(pady=10)

def actualizar_tabla():
    libros = biblioteca.obtenerLibros()
    datos_tabla = [["Indice: " + str(x), *y] for x, y in enumerate(libros)]
    tabla.actualizar(datos_tabla)

# Funciones para abrir las ventanas
def abrirVentanaAgregar():
    ventana_agregar = Toplevel(root)
    ventana_agregar.title("Agregar libro")

    # Se ponen los inputs para agregar la información
    label_titulo = Label(ventana_agregar, text="Titulo").grid(row=1, column=1)
    input_titulo = Entry(ventana_agregar)
    input_titulo.grid(row=1, column=2)

    label_autor = Label(ventana_agregar, text="Autor").grid(row=2, column=1)
    input_autor = Entry(ventana_agregar)
    input_autor.grid(row=2, column=2)

    label_genero = Label(ventana_agregar, text="Genero").grid(row=3, column=1)
    input_genero = Entry(ventana_agregar)
    input_genero.grid(row=3, column=2)

    label_publicacion = Label(ventana_agregar, text="Publicacion").grid(row=4, column=1)
    input_publicacion = Entry(ventana_agregar)
    input_publicacion.grid(row=4, column=2)

    def guardar():
        libro = Libro(input_titulo.get(), input_autor.get(), input_genero.get(), input_publicacion.get())
        biblioteca.agregarLibro(libro)

        # Después de guardar el libro, actualizamos los datos de la tabla
        actualizar_tabla()

    boton_agregar = Button(ventana_agregar, text="Agregar", command=guardar)
    boton_agregar.grid(row=5, column=1, columnspan=2)

# Agregar libro (Boton que abre otra ventana)
boton_agregar = Button(frame_botones, text="Agregar libro", command=abrirVentanaAgregar)
boton_agregar.grid(row=1, column=1)

#! Buscar libros
#! Reservar libro
#! Cancelar reserva de libro
#! Editar información de libro
#! Eliminar libro

# Salir
boton_salir = Button(frame_botones, text="Salir", command=lambda: root.destroy())
boton_salir.grid(row=1, column=2)

root.mainloop()
#     print("Eliminar libro\n")

#     if not biblioteca.libros:
#         print("No hay libros registrados\n")
#         return
    
#     titulo = input("Introduce el nombre del libro a eliminar: ")
#     biblioteca.eliminarLibro(titulo)