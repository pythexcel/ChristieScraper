# ChristieScraper



# Setup

* Install Python any version of python 3.6 + `https://www.python.org/downloads/`
* Clone scraper repo from git by cammand `git clone https://github.com/pythexcel/ChristieScraper.git`
* go into project directory.
* Install requirements by cammand `pip3 install -r requirements.txt`
* Run script with url `python3 main.py -m GREUBEL -d FORSEY`





Note: In example i used python3 because if multiple python installed
 ### Examples

 * `python3 main.py -m "tornek rayville" -d "tr-900"`
 
 * `python3 main.py -m "GREUBEL" -d "FORSEY"`
 
 * `python3 main.py -m "PATEK PHILIPPE" -d "tr-900"`

 * `python3 main.py -m "RICHARD" -d "MILLE"`

 * `python3 main.py -m "AUDEMARS" -d "PIGUET"`

 * `python3 main.py -m "VACHERON" -d "CONSTANTIN"`





# ChristieScraper

This is a script based on [this] Bs4.

### Prerequisites
* [Python3](https://www.python.org/)
* [BeautifulSoup](https://pypi.org/project/beautifulsoup4/)


### Usage

```
usage: main.py [-m] [--make MAKE] [-d] [--model MODEL]

```

##### Platforms

Linux: 
  * It works for linux by default you need to setup python version 3.6 +
  * Install BeautifulSoup and requests.

Note:
* Make: This is requred for the `-m` parameter for the run script.
* Model: This is requred for the `-d` parameter for the run script.
 

