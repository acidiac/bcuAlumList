#
#

from bs4 import BeautifulSoup
import urllib3
import pandas as pd 


def getUrl (url):
    http = urllib3.PoolManager()
    response  = http.request('GET', url)
    if response.status == 200:
        return response 
    else :
        return False

