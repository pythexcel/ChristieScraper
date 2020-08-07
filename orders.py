import requests

from bs4 import BeautifulSoup

from scrap import ScraperBot

import csv




def ChristiesItems(Make=None,Model=None):
    if Make and Model is not None:
        print("[+] Success! Scrap Bot Starting!")
        SearchUrl = "https://www.christies.com/lotfinder/searchresults.aspx?sc_lang=en&lid=1&action=search&searchfrom=header&entry="+Make+"%20"+Model
        SoldLotsUrl = SearchUrl+"&searchtype=p&pg=all"
        page = requests.get(SoldLotsUrl)
        data = page.content
        htmldata = BeautifulSoup(data, "html.parser")
        file = open(Make+Model+'.csv', 'w', newline ='')
        count = 0
        with file:
            header = ['Month','Day','Year','Value','PublicationYear','Make','Model','Source','Link']
            writer = csv.DictWriter(file, fieldnames = header) 
            writer.writeheader() 
            for ul in htmldata.find_all('div',{"class":"gridView"}):
                for li in ul.find_all('div',{"class":"image-overlay-box"}):
                    anchor = li.find('a')
                    scrap_url = anchor.get('href')
                    status = ScraperBot(Url=scrap_url,Make=Make,Model=Model,writer=writer)
                    if status == False:
                        count = count + 1
                        print("Make and Model Non stop not matched in string count =",count)
                        if count == 10:
                            print("Make and Model Non stop not matched limit reached to 10 Quit scraper")
                            break
                    if status == True:
                        count = 0
            print("[+] Christies data Scrap Done check csv file in current directory......>>>>>>>")
    else:
        raise Exception("=====>Make and Model not should be None<=====")