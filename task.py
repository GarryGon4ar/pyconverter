import youtube_dl

def download(url):
	ydl_opts = {'format': 'bestaudio',}
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		info = ydl.extract_info(url, download=False)
		return info['formats'][0]['url']
