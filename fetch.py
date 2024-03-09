import requests
from bs4 import BeautifulSoup, SoupStrainer

#pip install tinydb urllib3 xlsxwriter lxml


#soup = BeautifulSoup(html_doc, 'html.parser')

#to create file if needed
#open("output.txt","x")

outputFile = open("output.txt","w")
urlFile = open("url.txt","r")

urlArray = []

counter = 0

for url in urlFile:
	urlArray.append(url.rstrip())
	
for url in urlArray:
	page = requests.get(url)
	#soup = BeautifulSoup(page.text, "xml")
	#outputFile.write(soup)
	#print(soup)
	#outputFile.write(page.text)
	
	soup = BeautifulSoup(page.text, "lxml")
	results = soup.find_all("span")
	
	print(str(results[18]))
	
	#outputFile.write(str(results[19]))
	#outputFile.write("\n")
	
	#counter = counter + 1
	#print(counter)
	
