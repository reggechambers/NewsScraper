#dependencies
import requests
from bs4 import BeautifulSoup

#url to scrape from
url = "https://www.washingtonpost.com/technology/2020/09/25/privacy-check-blacklight"

#URL request and parser
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')

#Selecting and formatting data 
title = soup.select('[data-qa="headline-text"]')[0].text


#Print results
print(title)



