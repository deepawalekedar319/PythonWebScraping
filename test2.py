# importing the packages 
from bs4 import BeautifulSoup
import requests


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

	# looping and fetching the data
	for h in soup.find_all('h2',class_='newsHdng'):
		news_title = h.find('a').contents[0]
	
		if news_title not in news_list:
			news_list.append(news_title)


	# Opening file to write the fetched data into the file
	outFile = open('output.txt','a')

	# writing all the fetched data into the file
	for eachItem in news_list:
		outFile.write(eachItem)
		print(eachItem)
		print("\n")
		outFile.write("\n\n") # New line for every new item
		print(eachItem)
	# Closing the file
	outFile.close()

# Calling the getTheNewsItems(-) for fetcing the first top 10 pages data
for rotator in range(1,11):
	getTheNewsItems(rotator)	# Calling