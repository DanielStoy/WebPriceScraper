import requests
from bs4 import BeautifulSoup
from .SitePriceAverager import FindAverageSitePrice

#parses the main site for the price class
#and returns a list of prices
def ParseSitesForPrice(sites):
    for site in sites:
        page = requests.get(site.url, headers=site.headers)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find_all(class_=site.classNameForPrice)
        resultsText = []
        for result in results:
            resultsText.append(result.text)
        site = FindAverageSitePrice(site, resultsText)

    return sites