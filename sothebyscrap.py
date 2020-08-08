import argparse, os

import requests

from bs4 import BeautifulSoup

import csv


def SothebyScraperBot(Url=None,Make=None,Model=None,writer=None,dates=None):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
    if ".html" in Url:
        page = requests.get(Url,headers=headers)
        soup = BeautifulSoup(page.text)
        datedata = soup.select(".dtstart")
        ModelData = soup.select(".lotdetail-subtitle")
        ModelList = [model.text for model in ModelData]
        if not ModelList:
            ModelData = soup.select(".lotdetail-guarantee")
            ModelList = [model.text for model in ModelData]
        ValueData = soup.find_all('span',{"class":"curr-convert"})[0] if soup.find_all('span',{"class":"curr-convert"}) else None
        
        datelist = [date.text for date in datedata]
        if ValueData is not None:
            dateval = ValueData.get('data-price')+" "+ValueData.get('data-orig-currency')
        else:
            dateval = None
        datelist = datelist[-1]
        dates = datelist.strip()
        dates = [dates]
    else:
        page = requests.get(Url,headers=headers)
        soup = BeautifulSoup(page.text)
        ModelData = soup.select(".css-1ikrrc9")
        ValueData = soup.select(".css-65xq9y , .css-1nkk3t4")

        ModelList = [model.text for model in ModelData]
        ValueList = [value.text for value in ValueData]

        val = ValueList if len(ValueList)>0 else None

        if val is not None:
            try:
                dateval = val[0]+" "+val[1]
            except:
                dateval = val[0]
        else:
            dateval = None

    Make = Make
    Model = Model
    Source="Sotheby's"
    Link = Url
    
    if ModelList:
        searchmodel = Model.lower()
        searchdata = searchmodel.replace(searchmodel,str(" "+searchmodel+" "))
        if Make.lower() and searchdata in ModelList[0].lower():
            yeardata = ModelYear(ModelList=ModelList)
            if yeardata is not None:
                yeardata = yeardata[:4]
            Day,Month,Year = DateDetails(DateList=dates)
            try:
                writer.writerow([Month,Day,Year,dateval,yeardata,Make,Model,Source,Link])
                print("Record inserted.....")
                return True
            except Exception:
                print("[-] Faild! Data missing!")
        else:
            return False
    else:
        pass


def ModelYear(ModelList=None):
    yeardata = None
    if ModelList:
        ModelData = ModelList[0]
        ModelData = ModelData.replace(u'\xa0', u' ')
        ModelData = ModelData.split(" ")
        nextIndex = None
        for data in range(0,len(ModelData)):
            listt = ["CIRCA","Circa","circa"]
            if ModelData[data] in listt:
                nextIndex = data + 1
                continue
            Mlistt = ["MANUFACTURED","Manufactured","manufactured"]
            if ModelData[data] in Mlistt:
                nextIndex = data + 2
                continue
        if nextIndex is not None:
            try:
                data = ModelData[nextIndex]
                yeardata = data.strip()
                if len(yeardata) == 4:
                    return yeardata
                else:
                    return yeardata
            except Exception:
                return None
        else:
            return yeardata
    else:
        return yeardata



def DateDetails(DateList=None):
    Day=None
    Month=None
    Year = None
    if DateList:
        date = DateList[0].split(" ")
        if date:
            if len(date)==3:
                Day = date[0] 
                Month= date[1]
                Year = date[2]
                MonthNumber = month_string_to_number(Month)
                return Day,MonthNumber,Year
            else:
                try:
                    Day = date[0]
                    Month= date[1]
                    Year = date[2]
                    MonthNumber = month_string_to_number(Month)
                    return Day,MonthNumber,Year
                except Exception:
                    return None,None,None
        else:
            return Day,Month,Year
    else:
        return Day,Month,Year



def month_string_to_number(string):
    m = {
        'jan': 1,
        'feb': 2,
        'mar': 3,
        'apr':4,
        'may':5,
        'jun':6,
        'jul':7,
        'aug':8,
        'sep':9,
        'oct':10,
        'nov':11,
        'dec':12
        }
    s = string.strip()[:3].lower()

    try:
        out = m[s]
        return out
    except:
        return None