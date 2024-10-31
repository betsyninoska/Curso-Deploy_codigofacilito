#primer servidor en python
from wsgiref.simple_server import make_server
from jinja2 import Environment
from jinja2 import FileSystemLoader



#Encargada de responder las peticiones que harán los clientes
def application(environ, start_response):
    headers=[('Content-type', 'Text/html; charset=utf-8')]
    start_response('200 OK',headers)
    env=Environment(loader=FileSystemLoader("templates"))
    template= env.get_template('index.html')
    html= template.render(
        {
            'title': 'Servidor Python',
            'name': 'Cody'

        }
    )

    return [bytes(html,'utf8')]
#recibe 3 argumentos
#Donde se va a ejecutar
#Puerto con el que estara a la escucha 8000
#lo que respondera a la que sera application

server = make_server('localhost', 8000, application)
server.serve_forever()