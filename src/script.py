from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import showerror

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
datos_tabla = [["Indice: " + str(x + 1), *y] for x, y in enumerate(libros)]
tabla = Tabla(root, datos_tabla)
tabla.pack()

# Frame para poner los botones con las acciones
frame_botones = Frame(root)
frame_botones.pack(pady=10)

# Para obtener la lista actualizada de libros y mostrarlos
def actualizar_tabla():
    libros = biblioteca.obtenerLibros()
    datos_tabla = [["Indice: " + str(x + 1), *y] for x, y in enumerate(libros)]
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

        input_titulo.delete(0, END)
        input_autor.delete(0, END)
        input_genero.delete(0, END)
        input_publicacion.delete(0, END)

        # Después de guardar el libro, actualizamos los datos de la tabla
        actualizar_tabla()

    boton_agregar = Button(ventana_agregar, text="Agregar", command=guardar)
    boton_agregar.grid(row=5, column=1)
    boton_cancelar = Button(ventana_agregar, text="Cancelar", command=lambda: ventana_agregar.destroy())
    boton_cancelar.grid(row=5, column=2)

def abrirVentanaBuscar():
    ventana_buscar = Toplevel(root)
    ventana_buscar.title("Buscar libro")

    # Tipo de busqueda
    label_tipo = Label(ventana_buscar, text="Tipo").grid(row=1, column=1)
    combobox_tipo = Combobox(ventana_buscar,
                        values=["Titulo", "Autor", "Genero", "Publicacion", "Estado"],
                        state="readonly")
    combobox_tipo.grid(row=1, column=2)
    label_contenido = Label(ventana_buscar, text="Contenido").grid(row=2, column=1)
    input_contenido = Entry(ventana_buscar)
    input_contenido.grid(row=2, column=2)

    def buscar():
        encontrados = biblioteca.buscarLibros(combobox_tipo.get(), input_contenido.get())

        if len(encontrados) > 0:
            # Si se encontraron libros, se crea una tabla y se abre una ventana
            ventana_encontrados = Toplevel(ventana_buscar)
            ventana_encontrados.title("Libros encontrados")
            
            # Por cada libro, se obtiene su información y se le agrega el indice
            info = []
            for indice, libro in enumerate(encontrados):
                datos_libro = libro.obtenerInformacion().split("\n")
                info.append(["Indice: " + str(indice + 1), *datos_libro])

            tabla_encontrados = Tabla(ventana_encontrados, info).pack()

            boton_salir = Button(ventana_encontrados, text="Salir", command=ventana_encontrados.destroy).pack()
        else:
            showerror(title="No se encontraron libros", message="No se encontraron libros")
            ventana_buscar.deiconify()

    boton_aceptar = Button(ventana_buscar, text="Buscar", command=buscar)
    boton_aceptar.grid(row=3, column=1)
    boton_cancelar = Button(ventana_buscar, text="Cancelar", command=ventana_buscar.destroy)
    boton_cancelar.grid(row=3, column=2)

def abrirVentanaEliminar():
    ventana_eliminar = Toplevel(root)
    ventana_eliminar.title("Eliminar libro")

    # Input para poner el nombre del libro a eliminar
    label_titulo = Label(ventana_eliminar, text="Titulo").grid(row=1, column=1)
    input_titulo = Entry(ventana_eliminar)
    input_titulo.grid(row=1, column=2)

    # Hace la búsqueda de las opciones de libros a eliminar
    def aceptar():
        encontrados = biblioteca.buscarLibros("titulo", input_titulo.get())

        if len(encontrados):
            # Se abre otra ventana con todos los libros encontrados
            ventana_encontrados = Toplevel(ventana_eliminar)
            ventana_encontrados.title("Libros encontrados")

            # Tabla con los libros encontrados
            info = []
            for indice, libro in enumerate(encontrados):
                datos_libro = libro.obtenerInformacion().split("\n")
                info.append(["Indice: " + str(indice + 1), *datos_libro])
            
            tabla = Tabla(ventana_encontrados, info)
            tabla.pack()

            # Input para introducir el indice del libro que se quiere borrar
            frame_botones = Frame(ventana_encontrados)
            frame_botones.pack()
            
            label_indice = Label(frame_botones, text="Indice:")
            label_indice.grid(row=0, column=0)
            input_indice = Entry(frame_botones)
            input_indice.grid(row=0, column=1)

            def borrar():
                # Se borra el libro con el indice seleccionado
                biblioteca.eliminarLibro(encontrados[int(input_indice.get()) - 1])

                ventana_encontrados.destroy()
                actualizar_tabla()

            boton_borrar = Button(frame_botones, text="Borrar", command=borrar)
            boton_borrar.grid(row=1, column=0)
            boton_cancelar = Button(frame_botones, text="Cancelar", command=ventana_encontrados.destroy)
            boton_cancelar.grid(row=1, column=1)
        else:
            showerror(title="Libro no encontrado", message="Libro no encontrado")
            ventana_eliminar.deiconify() # Para evitar que con el error se minimice la ventana

    boton_aceptar = Button(ventana_eliminar, text="Aceptar", command=aceptar)
    boton_aceptar.grid(row=2, column=1)
    boton_cancelar = Button(ventana_eliminar, text="Cancelar", command=ventana_eliminar.destroy)
    boton_cancelar.grid(row=2, column=2)

# Agregar libro (Boton que abre otra ventana)
boton_agregar = Button(frame_botones, text="Agregar libro", command=abrirVentanaAgregar)
boton_agregar.grid(row=1, column=1)

# Buscar libros
boton_buscar = Button(frame_botones, text="Buscar libro", command=abrirVentanaBuscar)
boton_buscar.grid(row=1, column=2)

#! Reservar libro
#! Cancelar reserva de libro
#! Editar información de libro
# Eliminar libro
boton_eliminar = Button(frame_botones, text="Borrar libro", command=abrirVentanaEliminar)
boton_eliminar.grid(row=1, column=3)

# Salir
boton_salir = Button(frame_botones, text="Salir", command=lambda: root.destroy())
boton_salir.grid(row=1, column=4)

root.mainloop()
#     print("Eliminar libro\n")

#     if not biblioteca.libros:
#         print("No hay libros registrados\n")
#         return
    
#     titulo = input("Introduce el nombre del libro a eliminar: ")
#     biblioteca.eliminarLibro(titulo)