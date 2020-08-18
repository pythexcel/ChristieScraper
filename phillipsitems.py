
import requests

from bs4 import BeautifulSoup

import csv

from phillipsbot import PhillipsBot

from selenium import webdriver

import time

from config import CHROME_DRIVER_PATH,ScrollRange

def PhillipsItems(Make=None,Model=None):
    if Make and Model is not None:
        for pagenumber in range(1,100):
            print("[+] Success! Phillips Scrap Bot Starting!")
            SearchUrl = "https://www.phillips.com/search/"+str(pagenumber)+"/?search="+Make+"%20"+Model
            page = requests.get(SearchUrl)
            data = page.content
            htmldata = BeautifulSoup(data, "html.parser")
            file = open(Make+Model+'.csv', 'a', newline ='')
            writer = csv.writer(file)
            count = 0
            with file:
                for ul in htmldata.find_all('div',{"class":"image"}):
                    anchor = ul.find('a')
                    scrap_url = anchor.get('href')
                    
                    try:
                        status = PhillipsBot(Url=scrap_url,Make=Make,Model=Model,writer=writer)
                    except Exception:
                        pass
                    
                    if status == False:
                        count = count + 1
                        print("Make and Model Non stop not matched in string count =",count)
                        if count == 10:
                            print("Make and Model Non stop not matched limit reached to 10 Quit scraper")
                            break
                    if status == True:
                        count = 0
                    
                nexturl = htmldata.select(".current-page+ a")
                
                if nexturl:
                    if int(nexturl[0].text) < pagenumber:
                        print("Quit")
                        print("[+] Phillips data Scrap Done check csv file in current directory......>>>>>>>")
                        quit()
                    else:
                        pass
                if not nexturl:
                    print("Quit")
                    print("[+] Phillips data Scrap Done check csv file in current directory......>>>>>>>")
                    quit()
                print("[+] Phillips data Scrap Done check csv file in current directory......>>>>>>>")
    else:
        raise Exception("=====>Make and Model not should be None<=====")