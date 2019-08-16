from api import API
 
app = API()

@app.route("/")
def home(request, response):
    response.text = "Привет! Это ГЛАВНАЯ страница"
 
@app.route("/about") 
def about(request, response):
    response.text = "Привет! Это страница О НАС!"