from autoscraper import AutoScraper
newsUrl = "https://www.ndtv.com/india/page-3"
dataToBeFetched = ["Parliament Winter Session 2021 Live Updates: Rajya Sabha Adjourned As Opposition Continue Protest Over MPs' Suspension","Edited by NDTV Newsdesk | Wednesday December 01, 2021, New Delhi","Twelve opposition MPs from Rajya Sabha have been suspended from Parliament's Winter Session and the opposition has condemned the suspension, saying it is against the rules."]
scraper = AutoScraper()
res = scraper.build(newsUrl,dataToBeFetched)
#print(res)
#res = scraper.get_result_similar(newsUrl,grouped=True)
print(res)
outFile = open('News.txt','a')
for i in res:
	outFile.write(i)
	outFile.write("\n")
	print(i,end="\n")
outFile.close();