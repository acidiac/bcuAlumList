#
#

from bs4 import BeautifulSoup
import requests
import pandas as pd 


def getUrl (url):
    headers= { 'User-Agent' : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36" }
    response  = requests.get(url, headers = headers)
    if response.status_code == 200:
        return response
    else :
        return False
    
def parsePage(url):
    response = getUrl(url)
    return BeautifulSoup (response.content, "html.parser")


people = parsePage("https://www.linkedin.com/search/results/people/?keywords=bangalore%20central%20college&origin=FACETED_SEARCH")
print(people)

# refer : https://ferodia.github.io/linkedin-data-scraping-with-beautifulsoup
'''
<div class="search-result__info pt3 pb4 ph0">
<a data-control-id="P++zgsvQT6Olsl8eiuxLIQ==" 
    data-control-name="search_srp_result" 
    href="/in/alexander-castelino-603a5920/" id="ember5343" 
    class="search-result__result-link ember-view">      
    
'''