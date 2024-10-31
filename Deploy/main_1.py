#primer servidor en python
from wsgiref.simple_server import make_server

#Encargada de responder las peticiones que harán los clientes
def application(env, start_response):
    headers=[('Content-type', 'Text/plano')]
    start_response('200 OK',headers)
    return ['Hola mundo desde mi servidor en Python'.encode('utf_8')]
#recibe 3 argumentos
#Donde se va a ejecutar
#Puerto con el que estara a la escucha 8000
#lo que respondera a la que sera application

server = make_server('localhost', 8000, application)
server.serve_forever()