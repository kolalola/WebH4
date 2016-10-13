# -*- coding: utf-8 -*-
from wsgiref.simple_server import make_server
from jinja2 import Environment, FileSystemLoader,Template



env = Environment(loader=FileSystemLoader('HTML'))


# WSGI function that handles HTTP requests to our application
def application(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/html; charset=utf-8')])
    template = None
    if (environ['PATH_INFO'] == '/index.html'):

        template = env.get_template('index.html').render(link="""<a href="/About/aboutme.html">About me!</a>""",
                                                         head="""<h1>Sweet index</h1>""")
    elif (environ['PATH_INFO'] == '/About/aboutme.html'):
        template = env.get_template('/About/aboutme.html').render(link="""<a href="/index.html">Index!</a>""",
                                                                  head="""<h1>HeyHey, Here about me</h1>""")

    return [template.encode('utf-8')]

if __name__ == '__main__':
    httpd = make_server('', 8000, application)
    httpd.serve_forever()