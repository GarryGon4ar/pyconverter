from render import render_template
from task import download

def index(request, response):
	if request.method == "POST":
		url = request.POST.get('url')
		uri = download(url)
		print(uri)
		response.status_code = 303
		response.headerlist = [('Location', uri)]
		return response
	data = render_template("index.html")
	response.text = data 
	return response

def check_jinja(request, response):
	data = render_template('check.html', title="Boorsok")
	response.text = data

