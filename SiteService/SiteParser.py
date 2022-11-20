import requests
from bs4 import BeautifulSoup

def ParseSitesForPrice(sites):
    prices = []
    for site in sites:
        page = requests.get(site.url)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find_all(class_=site.classNameForPrice)
        resultsText = []
        for result in results:
            resultsText.append(result.text)

        resultsText = site.ParsePrice(resultsText)
        prices.append(resultsText)
    return prices