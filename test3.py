# importing the packages 
from bs4 import BeautifulSoup
import requests
import csv

# Used to easily read the HTML that we scraped
def getTheNewsItems(counter):


	# Creates a header
	headers = {'User-agent':'Google Chrome'}
	

	# Requests the WebPage
	newsUrl = 'https://www.ndtv.com/india/page-'+str(counter)
	request = requests.get(newsUrl,headers=headers)
	html = request.content	
	

	# Creates some soup
	soup = BeautifulSoup(html,'html.parser')

	# List declaration for appending the data
	news_list = []

	# Finds all the headers in News Home
	for h in soup.find_all('div',class_='news_Itm-cont'):
		news_title = h.find('a').contents[0]
		if news_title not in news_list:
			news_list.append(news_title)
		
		# Fetching the author or posted by
		post = h.find('span',class_='posted-by')
		newPost = post.find('a').contents[0]
		news_list.append(newPost)
			
		# Fetching the content 	
		cont = h.find('p',class_='newsCont')
		news_list.append(cont.get_text())


	# Opening file to write the fetched data into the file
	outFile = open('output.csv','a')
	outFileText = open('output.txt','a')

	# writing all the fetched data into the file
	for eachItem in news_list:
		outFile.write(eachItem)
		outFileText.write(eachItem)
		outFile.write("\n") # New line for every new item
		outFileText.write("\n") # New line for every new item
	
	#print(news_list)
	# Closing the file
	outFile.close()
	outFileText.close()

# Calling the getTheNewsItems(-) for fetcing the first top 10 pages data
for rotator in range(1,11):
	getTheNewsItems(rotator)	# Calling