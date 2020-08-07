
import requests

from bs4 import BeautifulSoup

import csv

from selenium import webdriver

import time

from sothebyscrap import SothebyScraperBot

from selenium.webdriver import DesiredCapabilities

from config import CHROME_DRIVER_PATH,ScrollRange

def SothebysItems(Make=None,Model=None):
    if Make and Model is not None:
        print("[+] Success! Sothybys Scrap Bot Starting!")

        SearchUrl = "https://www.sothebys.com/en/search-results.html?query="+Make+"%20"+Model
        SoldLotsUrl = SearchUrl+"&timeframe=past&refinementList%5Btype%5D%5B0%5D=Lot"

        try:
            driver = webdriver.Chrome(CHROME_DRIVER_PATH)
        except Exception as err:
            print("error :",str(err))
        driver.get(SoldLotsUrl,)
        time.sleep(5)
        productsdata = []
        for rangenumber in range(0,int(ScrollRange)):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
        page = driver.page_source
        soup = BeautifulSoup(page, 'html.parser')
        for ul in soup.find_all('div',{"class":"Card"}):
            media = ul.find_all('div',{"class":"Card-media"})[0] if ul.find_all('div',{"class":"Card-media"}) else None
            anchor = media.find('a')
            scrap_url = anchor.get('href')
            date = ul.find_all('div',{"class":"Card-details"})[0] if ul.find_all('div',{"class":"Card-details"}) else None
            if date is not None:
                datedata = date.text
                properdate = datedata.split("|")[0]
                properdate = properdate.strip()
                properdatechecking = properdate.split(" ")
                if len(properdatechecking) != 3:
                    properdate = None
                if len(properdatechecking[0]) not in range(1,3):
                    properdate = None
                if len(properdatechecking[-1]) not in range(1,5):
                    properdate = None
            else:
                properdate = None
            jsonp = {"url":scrap_url,"date":properdate}
            if jsonp not in productsdata:
                productsdata.append(jsonp)
        print("fetching sothebys products links----")
        driver.quit()

        file = open(Make+Model+'.csv', 'a', newline ='')
        writer = csv.writer(file)
        count = 0
        with file:
            for linkdata in productsdata:
                scrap_url = linkdata['url']
                dates  = linkdata['date']
                status = SothebyScraperBot(Url=scrap_url,Make=Make,Model=Model,writer=writer,dates=[dates] if dates is not None else None)
                if status == False:
                    count = count + 1
                    print("Make and Model Non stop not matched in string count =",count)
                    if count == 10:
                        print("Make and Model Non stop not matched limit reached to 10 Quit scraper")
                        quit()
                if status == True:
                    count = 0
            print("[+] All Data Scrap Done check csv file in current directory......>>>>>>>")






