import re
import webbrowser
from webob import Request, Response
from jinja2 import Template, FileSystemLoader, Environment
import youtube_dl

cars = [
    {'name': 'Audi', 'price': 23000}, 
    {'name': 'Skoda', 'price': 17300}, 
    {'name': 'Volvo', 'price': 44300}, 
    {'name': 'Volkswagen', 'price': 21300}
]

def render(template_name, **kwargs):
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)
    template = env.get_template(template_name)
    return template.render(**kwargs)

def download(url):
	ydl_opts = {'format': 'bestaudio',}
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		info = ydl.extract_info(url, download=False)
		return info['formats'][0]['url']

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
	if request.method == "POST":
		url = request.POST.get('url')
		uri = download(url)
		response.status_code = 303
		response.headerlist = [('Location', uri)]
		return response
	data = render("index.html")
	response.text = data 
	return response

def check_jinja(request, response):
	data = render('index.html', title="Boorsok")
	response.text = data

urls = [
    (r'^$', index),
    (r'about/?$', hello),
    (r'check/?$', check_jinja),
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