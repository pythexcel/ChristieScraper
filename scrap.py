import argparse, os

import requests

from bs4 import BeautifulSoup

import csv


def ScraperBot(Url=None,Make=None,Model=None,writer=None):
    page = requests.get(Url)
    soup = BeautifulSoup(page.text)

    ModelData = soup.select("#main_center_0_lblLotSecondaryTitle")
    DateData = soup.select("#main_center_0_lblSaleDate")
    ValueData = soup.select("#main_center_0_lblPriceRealizedPrimary")

    ModelList = [model.text for model in ModelData]
    DateList = [date.text for date in DateData]
    ValueList = [value.text for value in ValueData]
    Make = Make
    Model = Model
    Source = "Christie's"
    Link = Url

    if ModelList:
        if Make.lower() and Model.lower() in ModelList[0].lower():

            yeardata = ModelYear(ModelList=ModelList)

            Day,Month,Year = DateDetails(DateList=DateList)

            try:
                writer.writerow({"Month":Month,"Day":Day,"Year":Year,"Value":ValueList[0] if ValueList else None,"PublicationYear":yeardata,"Make":Make,"Model":Model,"Source":Source,"Link":Link}) 
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