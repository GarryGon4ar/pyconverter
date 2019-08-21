import re
import webbrowser
from webob import Request, Response
from jinja2 import Template, FileSystemLoader, Environment


# def render_from_template(directory, template_name, **kwargs):
#     loader = FileSystemLoader(directory)
#     env = Environment(loader=loader)
#     template = env.get_template(template_name)
#     return template.render(**kwargs)

def render(file_name, context=None):
    with open(file_name, 'r') as html_file:
        html = html_file.read()
        if context:
            template = Template(html)
            html = template.render(context)
        return html

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
	html= render("index.html")
	response.text = html
	# env = Environment(loader=FileSystemLoader('templates'))
	# template = env.get_template('index.html')
	return response
	# print(response)
	# return response


urls = [
    (r'^$', index),
    (r'about/?$', hello),
]

# uwsgi вызывает приложение application, сделал в форме класса, 
#так как когда вызываю функцию application не могу придумать как добавить обработку запроса
application = App()

# Необходимо
# написать веб приложение которое совместимо с uWSGI. А точнее сделать 4е
# задание только без использования каких либо фреймворков.Что в этом приложении должно быть:
# 1. URL диспатчер
# 2. ORM какая нибудь например SQLalchemy базу данных использовать MySQL
# 3. Должен быть файл с миграциями
# 4. Работа с темплейтами то есть должен быть подключен движок для темплейтов JINJA 2
# 5. Движок для темплейтов не просто так небходимо сделать какой нибудь отчет (какой придумаю позже)