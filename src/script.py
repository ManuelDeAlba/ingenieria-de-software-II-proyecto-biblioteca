import tkinter as tk
import customtkinter as ctk

from tkinter.messagebox import showerror, showinfo
from PIL import Image as PILImage, ImageTk as PILImageTk

from utils import *
from Biblioteca import *
from Libro import *
from Tabla import *

biblioteca = Biblioteca()

ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configure window
        self.title("Biblioteca")
        self.geometry(f"{1100}x{580}")

        # Creamos la tabla del inicio
        libros = biblioteca.obtenerCamposLibros()
        datos_tabla = [[str(x + 1), *y] for x, y in enumerate(libros)]
        self.tabla = Tabla(self, TITULOS, datos_tabla, TAMANOS)
        self.tabla.grid(column=1, row=0)
        
        # Configure grid layout (4x4)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure(0, weight=1)

        # Create sidebar frame with widgets
        self.sidebar_frame = ctk.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=7, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="Biblioteca", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = ctk.CTkButton(self.sidebar_frame, command=self.abrirVentanaAgregar, text="Agregar Libro")
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = ctk.CTkButton(self.sidebar_frame, command=self.abrirVentanaBuscar, text="Buscar Libro")
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = ctk.CTkButton(self.sidebar_frame, command=self.abrirVentanaReservar, text="Reservar Libro")
        self.sidebar_button_3.grid(row=5, column=0, padx=20, pady=10)
        self.sidebar_button_4 = ctk.CTkButton(self.sidebar_frame, command=self.abrirVentanaCancelar, text="Cancelar Libro")
        self.sidebar_button_4.grid(row=6, column=0, padx=20, pady=10)
        self.sidebar_button_5 = ctk.CTkButton(self.sidebar_frame, command=self.abrirVentanaEditar, text="Editar Libro")
        self.sidebar_button_5.grid(row=3, column=0, padx=20, pady=10)
        self.sidebar_button_6 = ctk.CTkButton(self.sidebar_frame, command=self.abrirVentanaEliminar, text="Borrar Libro")
        self.sidebar_button_6.grid(row=4, column=0, padx=20, pady=10)
        self.sidebar_button_7 = ctk.CTkButton(self.sidebar_frame, command=self.salir, text="Salir")
        self.sidebar_button_7.grid(row=7, column=0, padx=20, pady=10)
        
        self.appearance_mode_label = ctk.CTkLabel(self.sidebar_frame, text="Tema:", anchor="w")
        self.appearance_mode_label.grid(row=8, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"], command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=9, column=0, padx=20, pady=(10, 10))
        self.appearance_mode_optionemenu.set("System")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)
        
    def actualizar_tabla(self):
        libros = biblioteca.obtenerCamposLibros()
        datos_tabla = [[str(x + 1), *y] for x, y in enumerate(libros)]
        self.tabla.actualizar(datos_tabla)

    def generarTablaLibros(self, titulos, libros, ventana):
        info = []
        for indice, libro in enumerate(libros):
            datos_libro = libro.toCSV()
            info.append([str(indice + 1), *datos_libro])

        tabla_encontrados = Tabla(ventana, titulos, info, TAMANOS)

        return tabla_encontrados
        
    def abrirVentanaAgregar(self):
        ventana_agregar = ctk.CTkToplevel(self)
        ventana_agregar.title("Agregar libro")
        ventana_agregar.after(10, ventana_agregar.lift) # Se muestra la ventana por encima de la anterior

        # Se ponen los inputs para agregar la información
        label_titulo = ctk.CTkLabel(ventana_agregar, text="Titulo").grid(row=1, column=1)
        input_titulo = ctk.CTkEntry(ventana_agregar)
        input_titulo.grid(row=1, column=2)

        label_autor = ctk.CTkLabel(ventana_agregar, text="Autor").grid(row=2, column=1)
        input_autor = ctk.CTkEntry(ventana_agregar)
        input_autor.grid(row=2, column=2)

        label_genero = ctk.CTkLabel(ventana_agregar, text="Genero").grid(row=3, column=1)
        input_genero = ctk.CTkEntry(ventana_agregar)
        input_genero.grid(row=3, column=2)

        label_publicacion = ctk.CTkLabel(ventana_agregar, text="Publicacion").grid(row=4, column=1)
        input_publicacion = ctk.CTkEntry(ventana_agregar)
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

        boton_agregar = ctk.CTkButton(ventana_agregar, text="Agregar", command=guardar, width=15)
        boton_agregar.grid(row=5, column=1, padx=10, pady=10)
        boton_cancelar = ctk.CTkButton(ventana_agregar, text="Cancelar", command=lambda: ventana_agregar.destroy(), width=15)
        boton_cancelar.grid(row=5, column=2, padx=10, pady=10)
        
    def abrirVentanaBuscar(self):
        ventana_buscar = ctk.CTkToplevel(self)
        ventana_buscar.title("Buscar libro")
        ventana_buscar.after(10, ventana_buscar.lift) # Se muestra la ventana por encima de la anterior

        # Tipo de busqueda
        label_tipo = ctk.CTkLabel(ventana_buscar, text="Tipo").grid(row=0, column=0,)
        combobox_tipo = ctk.CTkComboBox(ventana_buscar,
                            values=["Titulo", "Autor", "Genero", "Publicacion", "Estado"],
                            state="readonly", width=160)
        combobox_tipo.grid(row=0, column=1)
        combobox_tipo.set("Titulo") #Colocamos por default la casilla de Titulo
        
        label_contenido = ctk.CTkLabel(ventana_buscar, text="Contenido").grid(row=1, column=0)
        input_contenido = ctk.CTkEntry(ventana_buscar)
        input_contenido.grid(row=1, column=1)

        def buscar():
            encontrados = biblioteca.buscarLibros(combobox_tipo.get(), input_contenido.get())

            if len(encontrados) > 0:
                # Si se encontraron libros, se crea una tabla y se abre una ventana
                ventana_encontrados = ctk.CTkToplevel(ventana_buscar)
                ventana_encontrados.title("Libros encontrados")
                ventana_encontrados.after(10, ventana_encontrados.lift) # Se muestra la ventana por encima de la anterior
                
                tabla_encontrados = self.generarTablaLibros(TITULOS, encontrados, ventana_encontrados)
                tabla_encontrados.pack()

                boton_salir = ctk.CTkButton(ventana_encontrados, text="Salir", command=ventana_encontrados.destroy).pack()
            else:
                showerror(title="No se encontraron libros", message="No se encontraron libros")
                ventana_buscar.deiconify()

        boton_aceptar = ctk.CTkButton(ventana_buscar, text="Buscar", command=buscar, width=15)
        boton_aceptar.grid(row=2, column=0, padx=10, pady=10)
        boton_cancelar = ctk.CTkButton(ventana_buscar, text="Cancelar", command=ventana_buscar.destroy, width=15)
        boton_cancelar.grid(row=2, column=1, padx=10, pady=10)
        
    def abrirVentanaReservar(self):
        ventana_reservar = ctk.CTkToplevel(self)
        ventana_reservar.title("Reservar libro")
        ventana_reservar.after(10, ventana_reservar.lift) # Se muestra la ventana por encima de la anterior

        # Input para poner el nombre del libro a reservar
        label_titulo = ctk.CTkLabel(ventana_reservar, text="Titulo").grid(row=0, column=0)
        input_titulo = ctk.CTkEntry(ventana_reservar)
        input_titulo.grid(row=0, column=1)

        def buscar():
            encontrados = biblioteca.buscarLibros("titulo", input_titulo.get())

            if len(encontrados) > 0:
                # Si se encontraron libros, se crea una tabla y se abre una ventana
                ventana_encontrados = ctk.CTkToplevel(ventana_reservar)
                ventana_encontrados.title("Libros encontrados")
                ventana_encontrados.after(10, ventana_encontrados.lift) # Se muestra la ventana por encima de la anterior
                
                tabla_encontrados = self.generarTablaLibros(TITULOS, encontrados, ventana_encontrados)
                tabla_encontrados.pack()

                # Input para introducir el indice del libro que se quiere reservar
                frame_botones = ctk.CTkFrame(ventana_encontrados)
                frame_botones.pack()
                
                label_indice = ctk.CTkLabel(frame_botones, text="Indice:")
                label_indice.grid(row=0, column=0)
                input_indice = ctk.CTkEntry(frame_botones)
                input_indice.grid(row=0, column=1)

                def reservar():
                    # Se reserva el libro con el indice seleccionado
                    error = biblioteca.reservarLibro(encontrados[int(input_indice.get()) - 1])

                    # Si la funcion devuelve algo, se muestra el error
                    if error:
                        showinfo(title=error, message=error)

                    ventana_encontrados.destroy()
                    self.actualizar_tabla()

                boton_reservar = ctk.CTkButton(frame_botones, text="Reservar", command=reservar, width=15)
                boton_reservar.grid(row=1, column=0, padx=10, pady=10)
                boton_cancelar = ctk.CTkButton(frame_botones, text="Cancelar", command=ventana_encontrados.destroy, width=15)
                boton_cancelar.grid(row=1, column=1, padx=10, pady=10)
            else:
                showerror(title="No se encontraron libros", message="No se encontraron libros")
                ventana_reservar.deiconify()

        boton_aceptar = ctk.CTkButton(ventana_reservar, text="Buscar", command=buscar, width=15)
        boton_aceptar.grid(row=1, column=0, padx=10, pady=10)
        boton_cancelar = ctk.CTkButton(ventana_reservar, text="Cancelar", command=ventana_reservar.destroy, width=15)
        boton_cancelar.grid(row=1, column=1, padx=10, pady=10)
        
    def abrirVentanaCancelar(self):
        ventana_cancelar = ctk.CTkToplevel(self)
        ventana_cancelar.title("Cancelar reserevación de libro")
        ventana_cancelar.after(10, ventana_cancelar.lift) # Se muestra la ventana por encima de la anterior

        # Input para poner el nombre del libro a cancelar
        label_titulo = ctk.CTkLabel(ventana_cancelar, text="Titulo").grid(row=0, column=0)
        input_titulo = ctk.CTkEntry(ventana_cancelar)
        input_titulo.grid(row=0, column=1)

        def buscar():
            encontrados = biblioteca.buscarLibros("titulo", input_titulo.get())

            if len(encontrados) > 0:
                # Si se encontraron libros, se crea una tabla y se abre una ventana
                ventana_encontrados = ctk.CTkToplevel(ventana_cancelar)
                ventana_encontrados.title("Libros encontrados")
                ventana_encontrados.after(10, ventana_encontrados.lift) # Se muestra la ventana por encima de la anterior
                
                tabla_encontrados = self.generarTablaLibros(TITULOS, encontrados, ventana_encontrados)
                tabla_encontrados.pack()

                # Input para introducir el indice del libro que se quiere cancelar
                frame_botones = ctk.CTkFrame(ventana_encontrados)
                frame_botones.pack()
                
                label_indice = ctk.CTkLabel(frame_botones, text="Indice:")
                label_indice.grid(row=0, column=0)
                input_indice = ctk.CTkEntry(frame_botones)
                input_indice.grid(row=0, column=1)

                def cancelar():
                    # Se cancela el libro con el indice seleccionado
                    error = biblioteca.cancelarReservacion(encontrados[int(input_indice.get()) - 1])

                    # Si la funcion devuelve algo, se muestra el error
                    if error:
                        showinfo(title=error, message=error)

                    ventana_encontrados.destroy()
                    self.actualizar_tabla()

                boton_cancelar = ctk.CTkButton(frame_botones, text="Cancelar reservación", command=cancelar)
                boton_cancelar.grid(row=1, column=0, padx=10, pady=10)
                boton_cancelar = ctk.CTkButton(frame_botones, text="Cancelar", command=ventana_encontrados.destroy)
                boton_cancelar.grid(row=1, column=1, padx=10, pady=10)
            else:
                showerror(title="No se encontraron libros", message="No se encontraron libros")
                ventana_cancelar.deiconify()

        boton_aceptar = ctk.CTkButton(ventana_cancelar, text="Buscar", command=buscar, width=15)
        boton_aceptar.grid(row=1, column=0, padx=10, pady=10)
        boton_cancelar = ctk.CTkButton(ventana_cancelar, text="Cancelar", command=ventana_cancelar.destroy, width=15)
        boton_cancelar.grid(row=1, column=1,padx=10, pady=10)
        
    def abrirVentanaEditar(self):
        ventana_editar = ctk.CTkToplevel(self)
        ventana_editar.title("Editar libro")
        ventana_editar.after(10, ventana_editar.lift) # Se muestra la ventana por encima de la anterior

        label_titulo = ctk.CTkLabel(ventana_editar, text="Titulo").grid(row=0, column=0)
        input_titulo = ctk.CTkEntry(ventana_editar)
        input_titulo.grid(row=0, column=1)

        def buscar():
            encontrados = biblioteca.buscarLibros("titulo", input_titulo.get())

            if len(encontrados) > 0:
                # Si se encontraron libros, se crea una tabla y se abre una ventana
                ventana_encontrados = ctk.CTkToplevel(ventana_editar)
                ventana_encontrados.title("Libros encontrados")
                ventana_encontrados.after(10, ventana_encontrados.lift) # Se muestra la ventana por encima de la anterior
                
                tabla_encontrados = self.generarTablaLibros(TITULOS, encontrados, ventana_encontrados)
                tabla_encontrados.pack()

                # Input para introducir el indice del libro que se quiere cancelar
                frame_botones = ctk.CTkFrame(ventana_encontrados)
                frame_botones.pack()
                
                label_indice = ctk.CTkLabel(frame_botones, text="Indice:")
                label_indice.grid(row=0, column=0)
                input_indice = ctk.CTkEntry(frame_botones)
                input_indice.grid(row=0, column=1)

                def editar():
                    ventana_editar_libro = ctk.CTkToplevel(ventana_encontrados)
                    ventana_editar_libro.title("Editar libro")
                    ventana_editar_libro.after(10, ventana_editar_libro.lift) # Se muestra la ventana por encima de la anterior

                    libroSeleccionado = encontrados[int(input_indice.get()) - 1]

                    # Se ponen los inputs para editar la información
                    label_titulo = ctk.CTkLabel(ventana_editar_libro, text="Titulo").grid(row=1, column=0)
                    input_titulo = ctk.CTkEntry(ventana_editar_libro)
                    input_titulo.insert(0, libroSeleccionado.titulo)
                    input_titulo.grid(row=1, column=1)

                    label_autor = ctk.CTkLabel(ventana_editar_libro, text="Autor").grid(row=2, column=0)
                    input_autor = ctk.CTkEntry(ventana_editar_libro)
                    input_autor.insert(0, libroSeleccionado.autor)
                    input_autor.grid(row=2, column=1)

                    label_genero = ctk.CTkLabel(ventana_editar_libro, text="Genero").grid(row=3, column=0)
                    input_genero = ctk.CTkEntry(ventana_editar_libro)
                    input_genero.insert(0, libroSeleccionado.genero)
                    input_genero.grid(row=3, column=1)

                    label_publicacion = ctk.CTkLabel(ventana_editar_libro, text="Publicacion").grid(row=4, column=0)
                    input_publicacion = ctk.CTkEntry(ventana_editar_libro)
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

                    boton_aceptar = ctk.CTkButton(ventana_editar_libro, text="Aceptar", command=aceptar, width=15)
                    boton_aceptar.grid(row=5, column=0, padx=10, pady=10)
                    boton_cancelar = ctk.CTkButton(ventana_editar_libro, text="Cancelar", command=ventana_editar_libro.destroy, width=15)
                    boton_cancelar.grid(row=5, column=1, padx=10, pady=10)

                boton_cancelar = ctk.CTkButton(frame_botones, text="Editar", command=editar, width=15)
                boton_cancelar.grid(row=1, column=0, padx=10, pady=10)
                boton_cancelar = ctk.CTkButton(frame_botones, text="Cancelar", command=ventana_encontrados.destroy, width=15)
                boton_cancelar.grid(row=1, column=1, padx=10, pady=10)
            else:
                showerror(title="No se encontraron libros", message="No se encontraron libros")
                ventana_editar.deiconify()

        boton_buscar = ctk.CTkButton(ventana_editar, text="Buscar", command=buscar, width=15)
        boton_buscar.grid(row=5, column=0, padx=10, pady=10)
        boton_cancelar = ctk.CTkButton(ventana_editar, text="Cancelar", command=ventana_editar.destroy, width=15)
        boton_cancelar.grid(row=5, column=1, padx=10, pady=10)
    
    def abrirVentanaEliminar(self):
        ventana_eliminar = ctk.CTkToplevel(self)
        ventana_eliminar.title("Eliminar libro")
        ventana_eliminar.after(10, ventana_eliminar.lift) # Se muestra la ventana por encima de la anterior

        # Input para poner el nombre del libro a eliminar
        label_titulo = ctk.CTkLabel(ventana_eliminar, text="Titulo").grid(row=0, column=0)
        input_titulo = ctk.CTkEntry(ventana_eliminar)
        input_titulo.grid(row=0, column=1)

        # Hace la búsqueda de las opciones de libros a eliminar
        def buscar():
            encontrados = biblioteca.buscarLibros("titulo", input_titulo.get())

            if len(encontrados):
                # Se abre otra ventana con todos los libros encontrados
                ventana_encontrados = ctk.CTkToplevel(ventana_eliminar)
                ventana_encontrados.title("Libros encontrados")
                ventana_encontrados.after(10, ventana_encontrados.lift) # Se muestra la ventana por encima de la anterior

                tabla_encontrados = self.generarTablaLibros(TITULOS, encontrados, ventana_encontrados)
                tabla_encontrados.pack()

                # Input para introducir el indice del libro que se quiere borrar
                frame_botones = ctk.CTkFrame(ventana_encontrados)
                frame_botones.pack()
                
                label_indice = ctk.CTkLabel(frame_botones, text="Indice:")
                label_indice.grid(row=0, column=0)
                input_indice = ctk.CTkEntry(frame_botones)
                input_indice.grid(row=0, column=1)

                def borrar():
                    # Se borra el libro con el indice seleccionado
                    biblioteca.eliminarLibro(encontrados[int(input_indice.get()) - 1])

                    ventana_encontrados.destroy()
                    self.actualizar_tabla()

                boton_borrar = ctk.CTkButton(frame_botones, text="Borrar", command=borrar, width=15)
                boton_borrar.grid(row=1, column=0, padx=10, pady=10)
                boton_cancelar = ctk.CTkButton(frame_botones, text="Cancelar", command=ventana_encontrados.destroy, width=15)
                boton_cancelar.grid(row=1, column=1, padx=10, pady=10)
            else:
                showerror(title="Libro no encontrado", message="Libro no encontrado")
                ventana_eliminar.deiconify() # Para evitar que con el error se minimice la ventana

        boton_aceptar = ctk.CTkButton(ventana_eliminar, text="Buscar", command=buscar, width=15)
        boton_aceptar.grid(row=1, column=0, padx=10, pady=10)
        boton_cancelar = ctk.CTkButton(ventana_eliminar, text="Cancelar", command=ventana_eliminar.destroy, width=15)
        boton_cancelar.grid(row=1, column=1, padx=10, pady=10)

    def salir(self):
        self.destroy()
        main()

class Login(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Ventana login
        self.title("Biblioteca | Inicio de sesión")
        self.geometry("500x500") # Tamaño de imagen
        self.resizable(width=False, height=False) # Evita redimensionar y fallos en imagen

        # Fondo
        fondo = PILImage.open(imgLogin)
        fondo = ctk.CTkImage(light_image=fondo, size=(500, 500))
        label = ctk.CTkLabel(self, image=fondo, text="").place(x=0, y=0)
        titulo = ctk.CTkLabel(self, text="Biblioteca", font=("Arial", 20, "normal")).place(x=210, y=130)

        # Variables
        self.usuario = StringVar()
        self.contrasena = StringVar()

        # Inputs
        entrada = ctk.CTkEntry(self, textvariable=self.usuario, width=200)
        entrada.place(x=150, y=200)
        entrada2 = ctk.CTkEntry(self, textvariable=self.contrasena, show="*", width=200)
        entrada2.place(x=150, y=250)

        # Botones inicio sesión
        boton = ctk.CTkButton(self, text="Entrar", cursor="hand2", command=self.login, width=200)
        boton.place(x=150, y=345)
        boton1 = ctk.CTkButton(self, text="Salir", cursor="hand2", command=self.cerrarLogin, width=200)
        boton1.place(x=150, y=410)
        self.mainloop()

    def login(self):
        nombre = self.usuario.get()
        contra = self.contrasena.get()
        if nombre == USUARIO and contra == CONTRASENA:
            self.correcta()
        else:
            self.incorrecta()

    def correcta(self):
        # Se destruye la ventana del login para abrir la principal
        self.cerrarLogin()

        root = App()
        root.mainloop()

    def incorrecta(self):
        self.withdraw()
        window = ctk.CTkToplevel()
        window.title("Biblioteca | Error al iniciar sesión")
        window.geometry("500x500") # Tamaño de imagen
        window.resizable(width=False, height=False) # Evita redimensionar y fallos en imagen
        
        texto = ctk.CTkLabel(window, text="Revise sus credenciales para acceder", font=("Arial", 20, "normal")).place(relwidth=1, relheight=1)

        def regreso():
            window.withdraw()
            self.deiconify()

        # Boton regresar
        boton = ctk.CTkButton(window, text="Intentar de nuevo", command=regreso, cursor="hand2")
        boton.place(x=180, y=390)
        window.mainloop()

    def cerrarLogin(self):
        self.destroy()

def main():
    login = Login()
    login.mainloop()

if __name__ == "__main__":
    main()