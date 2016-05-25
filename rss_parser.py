"""Gets the torrent RSS feed and parses it."""

import re
import requests
import html

def getRss():
    try:
        feed = requests.get('https://www.nyaa.se/?page=rss&user=64513')
        text = html.unescape(feed.text)

        try:
            titles=re.findall(r'<title>\[HorribleSubs\] (.*?).mkv</title>', text)
            links=re.findall(r'<link>(.*?)</link>', text)
			return (titles[0], links[1])
			
		except Exception as e:
			print(str(e))	
		
	except Exception as e:
		print(str(e))
