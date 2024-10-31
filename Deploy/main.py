#primer servidor en python
from wsgiref.simple_server import make_server
HTML= """<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Mi pagina de prueba</title>
  </head>
  <body>
   
  <h1> Hola mundo desde mi servidor en Python </h1>

  </body>
</html>"""

#Encargada de responder las peticiones que harán los clientes
def application(env, start_response):
    headers=[('Content-type', 'Text/html')]
    start_response('200 OK',headers)
    return [bytes(HTML,'utf8')]
#recibe 3 argumentos
#Donde se va a ejecutar
#Puerto con el que estara a la escucha 8000
#lo que respondera a la que sera application

server = make_server('localhost', 8000, application)
server.serve_forever()