# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 12:31:40 2019

@author: Glen Millard
"""

#scraping archive.org for magazines etc

import bs4 as bsoup
import urllib.request
import requests, bs4 ,selenium, os, datetime
from selenium import webdriver

#getting the list of URLS

sauce = urllib.request.urlopen('https://archive.org/details/heavy-metal-magazine').read()

soup = bsoup.BeautifulSoup(sauce,'lxml')

#for url in soup.find_all('a'):
#    print(url.get('href'))
    
start_point = soup.find('div',class_="ikind in")

#print(start_point.prettify())
#this is where all the mags start
#//*[@id="ikind--downloads"]

os.environ['MOZ_HEADLESS'] = '1' # keep Firefox headless - run in background
driver = webdriver.Firefox()

#create web connector
driver.get('https://archive.org/details/heavy-metal-magazine')

#find the downloads
downloads = driver.find_element_by_xpath('//*[@id="ikind--downloads"]')

#show them on the screen

print(downloads.text)
#print(downloads.find_element_by_link_text())

match = soup.find_all('div', class_="item-ia hov")

print(match)

print(soup.title.text)
#

# close things out correctly - don't leave any messes
# seems we need the last two or the Firefox executable stays running in the background.
driver.close()
driver.quit()
driver.stop_client()

#for paragraph in soup.find_all('p'):
#    print (paragraph.text)

#print(soup.find_all('heavy-metal-magazine'))
#print(sauce)
#parsing the URLS

#isolating the file names

#downloading the files
