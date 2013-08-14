import os
import urllib

def downloadFile(url, name):
	#print url
	image = urllib.URLopener()
	image.retrieve(url, name)

def run():
	counter = 1
	for counter in range(1, 250):
		response  = urllib.urlopen('http://xkcd.com/' + str(counter))
		html = response.read()
		start = 'Image URL (for hotlinking/embedding): '
		end = '\n'
		comicUrl = (html.split(start))[1].split(end)[0]
		downloadFile(comicUrl, 'xkcd' + str(counter) + '.jpg')

run()
