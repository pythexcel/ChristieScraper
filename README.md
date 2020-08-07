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
 



##### Extra setup for selenium to scrap sothebys

* step 1 -> pip install selenium
* step 2 -> we need cromedriver for run selenium
  *  For ubuntu 18.04 i have added chromedriver in repo.
  * You can download chromedriver according to your os version and for chorme version = https://sites.google.com/a/chromium.org/chromedriver/downloads
  * After download chormedriver extract and copy path of cromedriver
  * paste chormedriver path in config.py "CHROME_DRIVER_PATH="/home/ChristieScraper/chromedriver" like this
* step 2 -> Next just one more thing need to setup.
  * As in www.sothebys.com data comes dynamically on page scroll so i added a scroll range functionality to handel this.
  * In config file there is a parameter "ScrollRange" you need to set accordingly how many times you want to scroll currently its 20.
* After that you can run simply 
 * `python3 main.py -m "VACHERON" -d "CONSTANTIN"`
 * `python3 main.py -m "RICHARD" -d "MILLE"`