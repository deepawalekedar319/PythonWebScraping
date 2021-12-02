#from autoscraper import AutoScraper
import re,urllib
import urllib.request
newsUrl =["https://www.ndtv.com/india/page-1"]
for s in newsUrl:
	print("Searching...")
	u=urllib.request.urlopen(s)
	text=u.read()
	title=re.findall("<a>.*</a>",str(text),re.IGNORECASE)
	print(title[0])
	