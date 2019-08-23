from render import render_template
from tasks import download

def index(request, response):
	if request.method == "POST":
		url = request.POST.get('url')
		email = request.POST.get('email')
		download.delay(url, email)
		response.text = "Вам будет отправлено письмо на email"
		return response
	data = render_template("index.html")
	response.text = data 
	return response

def check_jinja(request, response):
	data = render_template('check.html', title="Boorsok")
	response.text = data

def download_link(request, response):
	pass
