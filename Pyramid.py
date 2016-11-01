from wsgiref.simple_server import make_server
from pyramid.response import Response
from pyramid.config import Configurator
from jinja2 import Environment, FileSystemLoader,Template

env = Environment(loader=FileSystemLoader('HTML'))

def AboutMe(request):
    template = env.get_template('/About/aboutme.html').render(link="""<a href="/index.html">Index!</a>""",
                                                              head="""<h1>HeyHey, Here about me</h1>""")
    return Response(template)
def Index(request):
    template = env.get_template('index.html').render(link="""<a href="/about/aboutme.html">About me!</a>""",
                                                     head="""<h1>Sweet index</h1>""")
    return Response(template)

if __name__ == '__main__':
    configurator=Configurator()
    configurator.add_route("aboutme",'/about/aboutme.html')
    configurator.add_view(AboutMe,route_name='aboutme')
    configurator.add_route('index', '/index.html')
    configurator.add_view(Index, route_name='index')
    app=configurator.make_wsgi_app()
    server = make_server('0.0.0.0', 8000, app)
    server.serve_forever()

