import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import util.generic as utl

class Aplicacion:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("UNITECNAR - APP")
        self.root.attributes('-fullscreen', False)
        self.root.geometry("1200x700")
        self.root.configure(bg="#E8F6F3")

        # Menú lateral
        self.menu_frame = tk.Frame(self.root, bg="#212529", width=200)
        self.menu_frame.pack(side="left", fill="y")

        # Contenido principal
        self.content_frame = tk.Frame(self.root, bg="#E8F6F3")
        self.content_frame.pack(side="right", expand=True, fill="both")

        # Cabecera
        self.header = tk.Label(
            self.root, text="Sebastianyangie.com", font=("Arial", 12),
            bg="#212529", fg="white", anchor="e", padx=10
        )
        self.header.place(relx=0, rely=0, relwidth=1, height=30)

        # Imagen de perfil
        perfil_img = utl.leer_imagen("imagenes/profile_3135715.png", (80, 80))
        perfil_label = tk.Label(self.menu_frame, image=perfil_img, bg="#212529")
        perfil_label.image = perfil_img
        perfil_label.pack(pady=50)

        # Opciones del menú
        opciones = [
            ("INICIO", self.mostrar_inicio),
            ("Perfil", self.mostrar_perfil),
            ("Imagen", self.mostrar_imagen),
            ("Información", self.mostrar_informacion),
            ("Configuración", self.mostrar_configuracion),
            ("CERRAR SESIÓN", self.cerrar_sesion),
        ]

        for opcion, comando in opciones:
            btn = tk.Button(
                self.menu_frame, text=opcion, bg="#212529", fg="white", 
                relief="flat", font=("Arial", 12), anchor="w", 
                padx=20, command=comando
            )
            btn.pack(fill="x", pady=5)

        # Inicializa mostrando la sección "Inicio"
        self.mostrar_inicio()

        self.root.mainloop()

    def limpiar_contenido(self):
        """Elimina todos los widgets del área de contenido."""
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def mostrar_inicio(self):
        """Muestra la sección de Inicio."""
        self.limpiar_contenido()
        inicio_label = tk.Label(self.content_frame, text="Inicio", font=("Arial", 24), bg="#E8F6F3")
        inicio_label.pack(pady=20)
        hola_mundo_label = tk.Label(self.content_frame, text="hola profi", font=("Arial", 18), bg="#E8F6F3")
        hola_mundo_label.pack(pady=10)

    def mostrar_perfil(self):
        """Muestra la sección de Perfil."""
        self.limpiar_contenido()
        perfil_label = tk.Label(self.content_frame, text="Perfil", font=("Arial", 24), bg="#E8F6F3")
        perfil_label.pack(pady=20)
        perfil_info_label = tk.Label(self.content_frame, text="Información del perfil", font=("Arial", 18), bg="#E8F6F3")
        perfil_info_label.pack(pady=10)

    def mostrar_imagen(self):
        """Muestra la sección de Imagen."""
        self.limpiar_contenido()
        imagen_label = tk.Label(self.content_frame, text="Imagen", font=("Arial", 24), bg="#E8F6F3")
        imagen_label.pack(pady=20)
        imagen_info_label = tk.Label(self.content_frame, text="Información de la imagen", font=("Arial", 18), bg="#E8F6F3")
        imagen_info_label.pack(pady=10)

    def mostrar_informacion(self):
        """Muestra la sección de Información."""
        self.limpiar_contenido()
        informacion_label = tk.Label(self.content_frame, text="Información", font=("Arial", 24), bg="#E8F6F3")
        informacion_label.pack(pady=20)
        informacion_info_label = tk.Label(
            self.content_frame, 
            text="Integrantes: \nsebastian andres sena \nAngie Milena julio", 
            font=("Arial", 18), bg="#E8F6F3"
        )
        informacion_info_label.pack(pady=10)

    def mostrar_configuracion(self):
        """Muestra la sección de Configuración."""
        self.limpiar_contenido()
        configuracion_label = tk.Label(self.content_frame, text="Configuración", font=("Arial", 24), bg="#E8F6F3")
        configuracion_label.pack(pady=20)
        configuracion_info_label = tk.Label(self.content_frame, text="Opciones de configuración", font=("Arial", 18), bg="#E8F6F3")
        configuracion_info_label.pack(pady=10)

    def cerrar_sesion(self):
        """Cierra la aplicación después de una confirmación."""
        respuesta = messagebox.askyesno("Cerrar sesión", "¿Estás seguro de que deseas cerrar sesión?")
        if respuesta:
            self.root.destroy()

# Inicializar la aplicación
if __name__ == "__main__":
    app = Aplicacion()
