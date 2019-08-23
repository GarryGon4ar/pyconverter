import re
from webob import Request, Response
from views import index, check_jinja, download_link

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


urls = [
    (r'^$', index),
    (r'check/?$', check_jinja),
    (r'^media/', download_link),
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


# Делаем предыдущее задание, но на асинхронной манере через отложенное выполнение. При этом мы выкачиваем только mp3 файл. Можно сделать через websocket. Код опубликовать на github
# Пользовательская история:
# Я зашел на сайт и оставил ссылку, по которой я хочу получить mp3 и email адрес, на который мне придет письмо. Закрыл страницу.

# Система в этот момент кодирует mp3 файл, кладет на файловую систему, генерирует ссылку на скачивание и генерирует письмо. Это письмо я получаю на свою почту, жму по ссылке скачать и качаю сконвертированный mp3 файл
# Технологии: redis, celery, ffmpeg, smtp

# Вопросы:
# Что такое redis?
# Что такое celery?
# Для чего нужно celery?
# Как работает celery?
# Как celery работает в связке с redis?
# Что такое worker в celery ?
# В каких типах данных передаются данные в worker’ов?
