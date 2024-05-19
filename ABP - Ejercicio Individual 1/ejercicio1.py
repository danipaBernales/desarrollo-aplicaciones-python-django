from http.server import BaseHTTPRequestHandler, HTTPServer


"""
¿Qué facilidades nos proporciona Django?

Django es un framework todo en uno, que permite desarrollar aplicaciones web de forma rápida y eficiente.
La mayoría de las aplicaciones web tienen varias funciones comunes, como la autenticación, la recuperación de información de una base de datos y la administración de cookies. Los desarrolladores tienen que codificar una funcionalidad similar en cada aplicación web que escriban. Django facilita su trabajo al agrupar las diferentes funciones en una gran colección de módulos reutilizables, llamada marco de aplicación web. Los desarrolladores utilizan el marco web de Django para organizar y escribir su código de manera más eficiente y reducir significativamente el tiempo de desarrollo web.


Con relación al levantamiento de un servidor. ¿Existe una forma de realizarlo con Python y sin Django?
¿Qué desventajas nos trae este tipo de proyectos sin Django?

Si, porque Python es un lenguaje de propósito general y corre en todos los ámbitos y plataformas para generar cualquier aplicación, por tanto permite programar en els ervidor por si mismo gracias a la librería http.server.

La desventaja es que no es funcional. Se pueden utilizar otros frameworks porque al no utilizar uno, hay que escribir todo el código desde cero. Por lo tanto es probable que tome mucho tiempo. 
"""
class HttpRequest(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"<h1>Hola, Soy un servidor</h1>")

def run(server_class=HTTPServer, handler_class=HttpRequest, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print("Servidor levantado mediante http.server")
    print(f"Server listening on port {port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
    
"""
Indague en la utilidad de django-admin startproject

Para crear un proyecto Django, primero se instala utilizando 'py -m pip install Django==5.0.6' en windows. Una vez instalado, se crea el directorio para almacenar los proyectos Django y luego se utiliza 'django-admin startproject <nombre_proyecto>' para inicializar un nuevo proyecto en ese directorio.

Entonces, la herramienta 'django-admin' se usa para crear la carpeta del proyecto, los ficheros de plantillas básicos y el script de gestión del proyecto y 'django-admin startproject' crea el nuevo proyecto con la estructura de carpetas/ficheros.
"""