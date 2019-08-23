import youtube_dl
from celery import Celery
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# from handler import get_env_variable
import os 
from decouple import config

app = Celery("task", broker="redis://localhost:6379/0")



def send_email(receiver_email, link):
	port = config('PORT')
	smtp_server = config('SMTP_SERVER')
	sender_email = config('SENDER_EMAIL')
	password = config('PASSWORD')
	message = MIMEMultipart("alternative")
	message["Subject"] = "Download link"
	message["From"] = sender_email
	message["To"] = receiver_email
	text = """  Hi,
				How are you?
				Real Python has many great tutorials:
				""" + link
	# html = """	<html>
 #  					<body>
 #    					<p>Hi,<br>How are you?<br>
 #       					<a href="http://www.realpython.com">Real Python</a> has many great tutorials.
 #       					</p>
 #  						</body>
	# 				</html>
	# 	    """		
	part1 = MIMEText(text, "plain")
	# part2 = MIMEText(html, "html")
	message.attach(part1)
	# message.attach(part2)
	context = ssl.create_default_context()
	with smtplib.SMTP_SSL(smtp_server, 465, context=context) as server:
		server.login(sender_email, password)
		server.sendmail(sender_email, receiver_email, message.as_string())


@app.task
def download(url, receiver_email):
	ydl_opts = {
			'format': 'bestaudio',
			'outtmpl': 'media/%(title)s.%(ext)s',
        	'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192', 
            }]}
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		info = ydl.extract_info(url)
		filename = info['title']
		link = ('http://127.0.0.1:8080' + '/media/' + filename).replace(" ", "%20") + '.mp3'
		send_email(receiver_email, link)




# celery worker -A celery_blog -l info -c 5