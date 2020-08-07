import argparse, os

import requests

from bs4 import BeautifulSoup

import csv


def SothebyScraperBot(Url=None,Make=None,Model=None,writer=None,dates=None):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
    if ".html" in Url:
        page = requests.get(Url,headers=headers)
        soup = BeautifulSoup(page.text)
        ModelData = soup.select(".lotdetail-details-content .lotdetail-guarantee")
        ValueData = soup.find_all('span',{"class":"curr-convert"})[0] if soup.find_all('span',{"class":"curr-convert"}) else None
        ModelList = [model.text for model in ModelData]
        if ValueData is not None:
            dateval = ValueData.get('data-price')+" "+ValueData.get('data-orig-currency')
        else:
            dateval = None
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
    Source = "Sotheby’s"
    Link = Url
    
    if ModelList:
        if Make.lower() and Model.lower() in ModelList[0].lower():
            yeardata = ModelYear(ModelList=ModelList)
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
        ModelData = ModelList[0].split(" ")
        nextIndex = None
        for data in range(0,len(ModelData)):
            if ModelData[data] == "CIRCA":
                nextIndex = data + 1
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
                Day = date[0]+date[1]+date[2]
                Month= date[3]
                Year = date[4]
                MonthNumber = month_string_to_number(Month)
                return Day,MonthNumber,Year
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