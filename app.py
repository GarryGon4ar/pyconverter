import re
from webob import Request, Response

class App:

	def __call__(self, environ, start_response):
		request = Request(environ)
		path = environ.get('PATH_INFO').lstrip('/')
		response = self.handle_request(request, path)
		return response(environ, start_response)


	def handle_request(self, request, path):
		response = Response()
		for regex, handler in urls:
			match = re.search(regex, path)
			if match is not None:
				handler(request, response)
				return response
		self.default_response(response)
		return response

	def default_response(self, response):
		response.status_code = 404
		response.text = "Not found."


def index(request, response):
    response.text = "Привет! Это ГЛАВНАЯ страница"

def hello(request, response):
    response.text = "Привет! Это страница О НАС!"


urls = [
    (r'^$', index),
    (r'about/?$', hello),
]

# uwsgi вызывает приложение application, сделал в форме класса, 
#так как когда вызываю функцию application не могу придумать как добавить обработку запроса
application = App()
