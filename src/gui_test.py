import tkinter
import tkinter.messagebox
import customtkinter

from tkinter.messagebox import showerror, showinfo

from Biblioteca import *
from Libro import *
from Tabla import *

biblioteca = Biblioteca()
#from script import abrirVentanaAgregar

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Proyecto Biblioteca")
        self.geometry(f"{1100}x{580}")

        libros = biblioteca.obtenerLibros()
        datos_tabla = [["Indice: " + str(x + 1), *y] for x, y in enumerate(libros)]
        
        self.tabla = Tabla(self, datos_tabla)
        self.tabla.grid(column=1, row=0)

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=7, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Proyecto Biblioteca", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.abrirVentanaAgregar, text="Agregar Libro")
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.abrirVentanaBuscar, text="Buscar Libro")
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=self.abrirVentanaReservar, text="Reservar Libro")
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, command=self.abrirVentanaCancelar, text="Cancelar Libro")
        self.sidebar_button_4.grid(row=4, column=0, padx=20, pady=10)
        self.sidebar_button_5 = customtkinter.CTkButton(self.sidebar_frame, command=self.abrirVentanaEditar, text="Editar Libro")
        self.sidebar_button_5.grid(row=5, column=0, padx=20, pady=10)
        self.sidebar_button_6 = customtkinter.CTkButton(self.sidebar_frame, command=self.abrirVentanaEliminar, text="Borrar Libro")
        self.sidebar_button_6.grid(row=6, column=0, padx=20, pady=10)
        self.sidebar_button_7 = customtkinter.CTkButton(self.sidebar_frame, command=lambda: self.destroy(), text="Salir")
        self.sidebar_button_7.grid(row=7, column=0, padx=20, pady=10)
        
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Tema:", anchor="w")
        self.appearance_mode_label.grid(row=8, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=9, column=0, padx=20, pady=(10, 10))

        # create main entry and button
        """self.entry = customtkinter.CTkEntry(self, placeholder_text="CTkEntry")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")"""

        # set default values
        self.appearance_mode_optionemenu.set("Dark")
        #self.textbox.insert("0.0", "CTkTextbox\n\n" + "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.\n\n" * 20)

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def sidebar_button_event(self):
        print("sidebar_button click")
        
    def actualizar_tabla(self):
        libros = biblioteca.obtenerLibros()
        datos_tabla = [["Indice: " + str(x + 1), *y] for x, y in enumerate(libros)]
        self.tabla.actualizar(datos_tabla)
        
    def abrirVentanaAgregar(self):
        ventana_agregar = customtkinter.CTkToplevel(self)
        ventana_agregar.title("Agregar libro")
        ventana_agregar.attributes('-topmost', 'true')

        # Se ponen los inputs para agregar la información
        label_titulo = customtkinter.CTkLabel(ventana_agregar, text="Titulo").grid(row=1, column=1)
        input_titulo = customtkinter.CTkEntry(ventana_agregar)
        input_titulo.grid(row=1, column=2)

        label_autor = customtkinter.CTkLabel(ventana_agregar, text="Autor").grid(row=2, column=1)
        input_autor = customtkinter.CTkEntry(ventana_agregar)
        input_autor.grid(row=2, column=2)

        label_genero = customtkinter.CTkLabel(ventana_agregar, text="Genero").grid(row=3, column=1)
        input_genero = customtkinter.CTkEntry(ventana_agregar)
        input_genero.grid(row=3, column=2)

        label_publicacion = customtkinter.CTkLabel(ventana_agregar, text="Publicacion").grid(row=4, column=1)
        input_publicacion = customtkinter.CTkEntry(ventana_agregar)
        input_publicacion.grid(row=4, column=2)

        def guardar():
            libro = Libro(input_titulo.get(), input_autor.get(), input_genero.get(), input_publicacion.get())
            biblioteca.agregarLibro(libro)

            input_titulo.delete(0, END)
            input_autor.delete(0, END)
            input_genero.delete(0, END)
            input_publicacion.delete(0, END)

            # Después de guardar el libro, actualizamos los datos de la tabla
            self.actualizar_tabla()

        boton_agregar = customtkinter.CTkButton(ventana_agregar, text="Agregar", command=guardar, width=15)
        boton_agregar.grid(row=5, column=1, padx=10, pady=10)
        boton_cancelar = customtkinter.CTkButton(ventana_agregar, text="Cancelar", command=lambda: ventana_agregar.destroy(), width=15)
        boton_cancelar.grid(row=5, column=2, padx=10, pady=10)
        
    def abrirVentanaBuscar(self):
        ventana_buscar = customtkinter.CTkToplevel(self)
        ventana_buscar.title("Buscar libro")
        ventana_buscar.attributes('-topmost', 'true')

        # Tipo de busqueda
        label_tipo = customtkinter.CTkLabel(ventana_buscar, text="Tipo").grid(row=0, column=0,)
        combobox_tipo = customtkinter.CTkComboBox(ventana_buscar,
                            values=["Titulo", "Autor", "Genero", "Publicacion", "Estado"],
                            state="readonly", width=160)
        combobox_tipo.grid(row=0, column=1)
        label_contenido = customtkinter.CTkLabel(ventana_buscar, text="Contenido").grid(row=1, column=0)
        input_contenido = customtkinter.CTkEntry(ventana_buscar)
        input_contenido.grid(row=1, column=1)

        def buscar():
            encontrados = biblioteca.buscarLibros(combobox_tipo.get(), input_contenido.get())

            if len(encontrados) > 0:
                # Si se encontraron libros, se crea una tabla y se abre una ventana
                ventana_encontrados = customtkinter.CTkToplevel(ventana_buscar)
                ventana_encontrados.title("Libros encontrados")
                ventana_encontrados.attributes('-topmost','true')
                
                # Por cada libro, se obtiene su información y se le agrega el indice
                info = []
                for indice, libro in enumerate(encontrados):
                    datos_libro = libro.obtenerInformacion().split("\n")
                    info.append(["Indice: " + str(indice + 1), *datos_libro])

                tabla_encontrados = Tabla(ventana_encontrados, info).pack()

                boton_salir = customtkinter.CTkButton(ventana_encontrados, text="Salir", command=ventana_encontrados.destroy).pack()
            else:
                showerror(title="No se encontraron libros", message="No se encontraron libros")
                ventana_buscar.deiconify()

        boton_aceptar = customtkinter.CTkButton(ventana_buscar, text="Buscar", command=buscar, width=15)
        boton_aceptar.grid(row=2, column=0, padx=10, pady=10)
        boton_cancelar = customtkinter.CTkButton(ventana_buscar, text="Cancelar", command=ventana_buscar.destroy, width=15)
        boton_cancelar.grid(row=2, column=1, padx=10, pady=10)
        
    def abrirVentanaReservar(self):
        ventana_reservar = customtkinter.CTkToplevel(self)
        ventana_reservar.title("Reservar libro")
        ventana_reservar.attributes('-topmost', 'true')

        # Input para poner el nombre del libro a reservar
        label_titulo = customtkinter.CTkLabel(ventana_reservar, text="Titulo").grid(row=0, column=0)
        input_titulo = customtkinter.CTkEntry(ventana_reservar)
        input_titulo.grid(row=0, column=1)

        def buscar():
            encontrados = biblioteca.buscarLibros("titulo", input_titulo.get())

            if len(encontrados) > 0:
                # Si se encontraron libros, se crea una tabla y se abre una ventana
                ventana_encontrados = customtkinter.CTkToplevel(ventana_reservar)
                ventana_encontrados.title("Libros encontrados")
                ventana_encontrados.attributes('-topmost','true')
                
                # Por cada libro, se obtiene su información y se le agrega el indice
                info = []
                for indice, libro in enumerate(encontrados):
                    datos_libro = libro.obtenerInformacion().split("\n")
                    info.append(["Indice: " + str(indice + 1), *datos_libro])

                tabla_encontrados = Tabla(ventana_encontrados, info).pack()

                # Input para introducir el indice del libro que se quiere reservar
                frame_botones = customtkinter.CTkFrame(ventana_encontrados)
                frame_botones.pack()
                
                label_indice = customtkinter.CTkLabel(frame_botones, text="Indice:")
                label_indice.grid(row=0, column=0)
                input_indice = customtkinter.CTkEntry(frame_botones)
                input_indice.grid(row=0, column=1)

                def reservar():
                    # Se reserva el libro con el indice seleccionado
                    error = biblioteca.reservarLibro(encontrados[int(input_indice.get()) - 1])

                    # Si la funcion devuelve algo, se muestra el error
                    if error:
                        showinfo(title=error, message=error)

                    ventana_encontrados.destroy()
                    self.actualizar_tabla()

                boton_reservar = customtkinter.CTkButton(frame_botones, text="Reservar", command=reservar, width=15)
                boton_reservar.grid(row=1, column=0, padx=10, pady=10)
                boton_cancelar = customtkinter.CTkButton(frame_botones, text="Cancelar", command=ventana_encontrados.destroy, width=15)
                boton_cancelar.grid(row=1, column=1, padx=10, pady=10)
            else:
                showerror(title="No se encontraron libros", message="No se encontraron libros")
                ventana_reservar.deiconify()

        boton_aceptar = customtkinter.CTkButton(ventana_reservar, text="Buscar", command=buscar, width=15)
        boton_aceptar.grid(row=1, column=0, padx=10, pady=10)
        boton_cancelar = customtkinter.CTkButton(ventana_reservar, text="Cancelar", command=ventana_reservar.destroy, width=15)
        boton_cancelar.grid(row=1, column=1, padx=10, pady=10)
        
    def abrirVentanaCancelar(self):
        ventana_cancelar = customtkinter.CTkToplevel(self)
        ventana_cancelar.title("Cancelar reserevación de libro")
        ventana_cancelar.attributes('-topmost','true')

        # Input para poner el nombre del libro a cancelar
        label_titulo = customtkinter.CTkLabel(ventana_cancelar, text="Titulo").grid(row=0, column=0)
        input_titulo = customtkinter.CTkEntry(ventana_cancelar)
        input_titulo.grid(row=0, column=1)

        def buscar():
            encontrados = biblioteca.buscarLibros("titulo", input_titulo.get())

            if len(encontrados) > 0:
                # Si se encontraron libros, se crea una tabla y se abre una ventana
                ventana_encontrados = customtkinter.CTkToplevel(ventana_cancelar)
                ventana_encontrados.title("Libros encontrados")
                ventana_encontrados.attributes('-topmost','true')
                
                # Por cada libro, se obtiene su información y se le agrega el indice
                info = []
                for indice, libro in enumerate(encontrados):
                    datos_libro = libro.obtenerInformacion().split("\n")
                    info.append(["Indice: " + str(indice + 1), *datos_libro])

                tabla_encontrados = Tabla(ventana_encontrados, info).pack()

                # Input para introducir el indice del libro que se quiere cancelar
                frame_botones = customtkinter.CTkFrame(ventana_encontrados)
                frame_botones.pack()
                
                label_indice = customtkinter.CTkLabel(frame_botones, text="Indice:")
                label_indice.grid(row=0, column=0)
                input_indice = customtkinter.CTkEntry(frame_botones)
                input_indice.grid(row=0, column=1)

                def cancelar():
                    # Se cancela el libro con el indice seleccionado
                    error = biblioteca.cancelarReservacion(encontrados[int(input_indice.get()) - 1])

                    # Si la funcion devuelve algo, se muestra el error
                    if error:
                        showinfo(title=error, message=error)

                    ventana_encontrados.destroy()
                    self.actualizar_tabla()

                boton_cancelar = customtkinter.CTkButton(frame_botones, text="Cancelar reservación", command=cancelar)
                boton_cancelar.grid(row=1, column=0, padx=10, pady=10)
                boton_cancelar = customtkinter.CTkButton(frame_botones, text="Cancelar", command=ventana_encontrados.destroy)
                boton_cancelar.grid(row=1, column=1, padx=10, pady=10)
            else:
                showerror(title="No se encontraron libros", message="No se encontraron libros")
                ventana_cancelar.deiconify()

        boton_aceptar = customtkinter.CTkButton(ventana_cancelar, text="Buscar", command=buscar, width=15)
        boton_aceptar.grid(row=1, column=0, padx=10, pady=10)
        boton_cancelar = customtkinter.CTkButton(ventana_cancelar, text="Cancelar", command=ventana_cancelar.destroy, width=15)
        boton_cancelar.grid(row=1, column=1,padx=10, pady=10)
        
    def abrirVentanaEditar(self):
        ventana_editar = customtkinter.CTkToplevel(self)
        ventana_editar.title("Editar libro")
        ventana_editar.attributes('-topmost','true')

        label_titulo = customtkinter.CTkLabel(ventana_editar, text="Titulo").grid(row=0, column=0)
        input_titulo = customtkinter.CTkEntry(ventana_editar)
        input_titulo.grid(row=0, column=1)

        def buscar():
            encontrados = biblioteca.buscarLibros("titulo", input_titulo.get())

            if len(encontrados) > 0:
                # Si se encontraron libros, se crea una tabla y se abre una ventana
                ventana_encontrados = customtkinter.CTkToplevel(ventana_editar)
                ventana_encontrados.title("Libros encontrados")
                ventana_encontrados.attributes('-topmost','true')
                
                
                # Por cada libro, se obtiene su información y se le agrega el indice
                info = []
                for indice, libro in enumerate(encontrados):
                    datos_libro = libro.obtenerInformacion().split("\n")
                    info.append(["Indice: " + str(indice + 1), *datos_libro])

                tabla_encontrados = Tabla(ventana_encontrados, info).pack()

                # Input para introducir el indice del libro que se quiere cancelar
                frame_botones = customtkinter.CTkFrame(ventana_encontrados)
                frame_botones.pack()
                
                label_indice = customtkinter.CTkLabel(frame_botones, text="Indice:")
                label_indice.grid(row=0, column=0)
                input_indice = customtkinter.CTkEntry(frame_botones)
                input_indice.grid(row=0, column=1)

                def editar():
                    ventana_editar_libro = customtkinter.CTkToplevel(ventana_encontrados)
                    ventana_editar_libro.title("Editar libro")
                    ventana_editar_libro.attributes("-topmost",'true')

                    libroSeleccionado = encontrados[int(input_indice.get()) - 1]

                    # Se ponen los inputs para editar la información
                    label_titulo = customtkinter.CTkLabel(ventana_editar_libro, text="Titulo").grid(row=1, column=0)
                    input_titulo = customtkinter.CTkEntry(ventana_editar_libro)
                    input_titulo.insert(0, libroSeleccionado.titulo)
                    input_titulo.grid(row=1, column=1)

                    label_autor = customtkinter.CTkLabel(ventana_editar_libro, text="Autor").grid(row=2, column=0)
                    input_autor = customtkinter.CTkEntry(ventana_editar_libro)
                    input_autor.insert(0, libroSeleccionado.autor)
                    input_autor.grid(row=2, column=1)

                    label_genero = customtkinter.CTkLabel(ventana_editar_libro, text="Genero").grid(row=3, column=0)
                    input_genero = customtkinter.CTkEntry(ventana_editar_libro)
                    input_genero.insert(0, libroSeleccionado.genero)
                    input_genero.grid(row=3, column=1)

                    label_publicacion = customtkinter.CTkLabel(ventana_editar_libro, text="Publicacion").grid(row=4, column=0)
                    input_publicacion = customtkinter.CTkEntry(ventana_editar_libro)
                    input_publicacion.insert(0, libroSeleccionado.publicacion)
                    input_publicacion.grid(row=4, column=1)

                    def aceptar():
                        nuevaInformacion = {
                            "titulo": input_titulo.get(),
                            "autor": input_autor.get(),
                            "genero": input_genero.get(),
                            "publicacion": input_publicacion.get()
                        }

                        biblioteca.editarLibro(libroSeleccionado, nuevaInformacion)

                        # Después de editar el libro, actualizamos los datos de la tabla
                        self.actualizar_tabla()
                        ventana_encontrados.destroy()
                        ventana_editar_libro.destroy()

                    boton_aceptar = customtkinter.CTkButton(ventana_editar_libro, text="Aceptar", command=aceptar, width=15)
                    boton_aceptar.grid(row=5, column=0, padx=10, pady=10)
                    boton_cancelar = customtkinter.CTkButton(ventana_editar_libro, text="Cancelar", command=ventana_editar_libro.destroy, width=15)
                    boton_cancelar.grid(row=5, column=1, padx=10, pady=10)

                boton_cancelar = customtkinter.CTkButton(frame_botones, text="Editar", command=editar, width=15)
                boton_cancelar.grid(row=1, column=0, padx=10, pady=10)
                boton_cancelar = customtkinter.CTkButton(frame_botones, text="Cancelar", command=ventana_encontrados.destroy, width=15)
                boton_cancelar.grid(row=1, column=1, padx=10, pady=10)
            else:
                showerror(title="No se encontraron libros", message="No se encontraron libros")
                ventana_editar.deiconify()

        boton_buscar = customtkinter.CTkButton(ventana_editar, text="Buscar", command=buscar, width=15)
        boton_buscar.grid(row=5, column=0, padx=10, pady=10)
        boton_cancelar = customtkinter.CTkButton(ventana_editar, text="Cancelar", command=ventana_editar.destroy, width=15)
        boton_cancelar.grid(row=5, column=1, padx=10, pady=10)
    
    def abrirVentanaEliminar(self):
        ventana_eliminar = customtkinter.CTkToplevel(self)
        ventana_eliminar.title("Eliminar libro")
        ventana_eliminar.attributes('-topmost','true')

        # Input para poner el nombre del libro a eliminar
        label_titulo = customtkinter.CTkLabel(ventana_eliminar, text="Titulo").grid(row=0, column=0)
        input_titulo = customtkinter.CTkEntry(ventana_eliminar)
        input_titulo.grid(row=0, column=1)

        # Hace la búsqueda de las opciones de libros a eliminar
        def buscar():
            encontrados = biblioteca.buscarLibros("titulo", input_titulo.get())

            if len(encontrados):
                # Se abre otra ventana con todos los libros encontrados
                ventana_encontrados = customtkinter.CTkToplevel(ventana_eliminar)
                ventana_encontrados.title("Libros encontrados")
                ventana_encontrados.attributes('-topmost','true')

                # Tabla con los libros encontrados
                info = []
                for indice, libro in enumerate(encontrados):
                    datos_libro = libro.obtenerInformacion().split("\n")
                    info.append(["Indice: " + str(indice + 1), *datos_libro])
                
                tabla = Tabla(ventana_encontrados, info)
                tabla.pack()

                # Input para introducir el indice del libro que se quiere borrar
                frame_botones = customtkinter.CTkFrame(ventana_encontrados)
                frame_botones.pack()
                
                label_indice = customtkinter.CTkLabel(frame_botones, text="Indice:")
                label_indice.grid(row=0, column=0)
                input_indice = customtkinter.CTkEntry(frame_botones)
                input_indice.grid(row=0, column=1)

                def borrar():
                    # Se borra el libro con el indice seleccionado
                    biblioteca.eliminarLibro(encontrados[int(input_indice.get()) - 1])

                    ventana_encontrados.destroy()
                    self.actualizar_tabla()

                boton_borrar = customtkinter.CTkButton(frame_botones, text="Borrar", command=borrar, width=15)
                boton_borrar.grid(row=1, column=0, padx=10, pady=10)
                boton_cancelar = customtkinter.CTkButton(frame_botones, text="Cancelar", command=ventana_encontrados.destroy, width=15)
                boton_cancelar.grid(row=1, column=1, padx=10, pady=10)
            else:
                showerror(title="Libro no encontrado", message="Libro no encontrado")
                ventana_eliminar.deiconify() # Para evitar que con el error se minimice la ventana

        boton_aceptar = customtkinter.CTkButton(ventana_eliminar, text="Buscar", command=buscar, width=15)
        boton_aceptar.grid(row=1, column=0, padx=10, pady=10)
        boton_cancelar = customtkinter.CTkButton(ventana_eliminar, text="Cancelar", command=ventana_eliminar.destroy, width=15)
        boton_cancelar.grid(row=1, column=1, padx=10, pady=10)


if __name__ == "__main__":
    root = App()
    root.mainloop()