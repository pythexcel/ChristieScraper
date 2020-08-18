import argparse, os

import requests

from bs4 import BeautifulSoup

import csv


def PhillipsBot(Url=None,Make=None,Model=None,writer=None):
    page = requests.get(Url)
    soup = BeautifulSoup(page.text)

    Manufacturer = soup.select("span:nth-child(1) text")
    Reference = soup.select("span:nth-child(3) text")
    Modelno = soup.select("span:nth-child(2) text")
    DateData = soup.select(".sale-title-banner span")
    ValueData = soup.select(".lot-detail-header__sold")

    ManufacturerList = [model.text for model in Manufacturer]
    ReferenceList = [model.text for model in Reference]
    ModelList = [model.text for model in Modelno]
    DateList = [date.text for date in DateData]
    ValueList = [value.text for value in ValueData]
    if ValueList:
        price = ValueList[0].strip().split(" ")[-1]
    else:
        price = None
    Make = Make
    Model = Model
    Source = "Phillips"
    Link = Url
    
    if ManufacturerList and ReferenceList:
        if Make.lower() in ManufacturerList[0].lower().strip():
            if Model.lower() in ReferenceList[0].lower().strip():
                yeardata = ModelYear(ModelList=ModelList)
                Day,Month,Year = DateDetails(DateList=DateList)
                try:
                    writer.writerow([Month,Day,Year,price,yeardata,Make,Model,Source,Link]) 
                    print("Record inserted.....")
                    return True
                except Exception:
                    print("[-] Faild! Data missing!")
            else:
                return False
        else:
            return False
    else:
        pass



def ModelYear(ModelList=None):
    yeardata = None
    if ModelList:
        ModelData = ModelList[0].strip().split(" ")
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
        if nextIndex is None:
            nextIndex = 0
        if nextIndex is not None:
            data = ModelData[nextIndex]
            yeardata = data.strip()
            if len(yeardata) == 4:
                return yeardata
            else:
                return yeardata
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
            if len(date[-3])==2:
                Day = date[-3] 
                Month= date[-2]
                Year = date[-1]
                MonthNumber = month_string_to_number(Month)
                return Day,MonthNumber,Year.strip()
            else:
                for rec in range(0,len(date)):
                    datechk = date[rec]
                    stat = datechk.isnumeric()
                    indx = None
                    if stat == True:
                        indx = rec
                        break
                if indx is not None:                    
                    if len(date[indx].strip()) == 4:
                        Day = date[indx-2]
                        Month= date[indx-1]
                        Year = date[indx]
                        MonthNumber = month_string_to_number(Month)
                        Days = Day.split("-")
                        if len(Days) > 1:
                            Day = Days[-1]
                        return Day,MonthNumber,Year.strip()
                    else:
                        Day = date[indx]
                        Month= date[indx+1]
                        Year = date[indx+2]
                        MonthNumber = month_string_to_number(Month)
                        Days = Day.split("-")
                        if len(Days) > 1:
                            Day = Days[-1]
                        return Day,MonthNumber,Year.strip()
                else:
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