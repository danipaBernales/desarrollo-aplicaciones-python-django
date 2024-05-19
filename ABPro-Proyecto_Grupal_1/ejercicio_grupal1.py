"""
Levantaremos un servidor con Python, para que imprima el mensaje “Bienvenidos a TeLoVendo” en un navegador. Realícelo solo utilizando Python.
"""

from http.server import BaseHTTPRequestHandler, HTTPServer

class MiManejador(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        mensaje = "<html><head><title>TeLoVendo</title></head><body><h1>Bienvenidos a TeLoVendo</h1></body></html>"
        self.wfile.write(mensaje.encode("utf-8"))
def ejecutar_servidor():
    direccion = ("", 8000)
    servidor = HTTPServer(direccion, MiManejador)
    print("Servidor corriendo en http://localhost:8000")
    
    servidor.serve_forever()

if __name__ == "__main__":
    ejecutar_servidor()

"""
Ahora cree un entorno virtual e instalen Django. Verifiquen la versión de Python y Django.

PS C:\Users\Daniela Paz> python --version
Python 3.12.2
PS C:\Users\Daniela Paz> python -m django --version
5.0.4

django-admin startproject telovendo


Esta vez utilizaremos la arquitectura que nos brinda Django, para luego complejizar la aplicación. En esta
primera instancia desarrollaremos una vista, basándonos en la documentación de Django en la página
web de Django Project
"""

from django.http import HttpResponse

def index(request):
    return HttpResponse("Bienvenidos a TeLoVendo")

"""
Identifique los diferentes archivos creados por Django al crear un proyecto y una aplicación. Describa en
palabras simples la utilidad de cada script.

Archivos y Directorios en una Aplicación
    1. <nombre_aplicación>/ (directorio de la aplicación):
        __init__.py:
        Indica a Python que este directorio debe ser tratado como un paquete.
        admin.py:
        Registro de modelos para el panel de administración de Django. Permite administrar modelos a través de la interfaz de administración.
        apps.py:
        Configuración de la aplicación. Define la configuración de la aplicación para el proyecto.
        models.py:
        Define los modelos de datos, es decir, las estructuras de las tablas de la base de datos.
        views.py:
        Contiene las vistas, que son funciones o clases que manejan las solicitudes HTTP y devuelven respuestas HTTP.
        migrations/:
        Directorio que contiene archivos de migración. Las migraciones son cambios a la estructura de la base de datos (añadir campos, crear tablas, etc.).
        tests.py:
        Define las pruebas para la aplicación. Se utiliza para escribir tests unitarios y asegurar que el código funcione correctamente.
        urls.py (puede ser creado manualmente):
        Define el mapeo de URLs a vistas específicas dentro de la aplicación. Ayuda a modularizar las URLs del proyecto.
        templates/ (puede ser creado manualmente):
        Contiene las plantillas HTML que se utilizan para renderizar las vistas.
        static/ (puede ser creado manualmente):
        Directorio para archivos estáticos como CSS, JavaScript e imágenes que no cambian frecuentemente.
"""