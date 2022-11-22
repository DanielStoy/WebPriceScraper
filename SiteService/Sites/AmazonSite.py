from .WebSite import WebSite
from .WebSite import SiteType

class AmazonSite(WebSite):
    url = "" 
    type = [SiteType.Common] 
    classNameForPrice = "a-price" 
    siteName = "Amazon"
    averagePrice = 0
    amountOfPrices = 0
    headers = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})

    def SetupURL(self, searchTerm, lowPricePoint, highPricePoint):
        self.url = "https://www.amazon.com/s?k="
        terms = searchTerm.split()
        searchTermRefined = ""
        if(len(terms) == 1):
            searchTermRefined = searchTerm
        else:
            for i in range(len(terms)):
                if( i == len(terms) - 1):
                    searchTermRefined += terms[i]
                else:
                    searchTermRefined += terms[i] +'+'
        endOfUrl = "&crid=1LKMCMIE7U4H&qid=1669045617&rnid=2661611011&sprefix=%2Caps%2C76&ref=sr_nr_p_36_5"
        if(lowPricePoint != ""):
            searchTermRefined += "&rh=p_36%3A"
            lowPricePoint += "00"
            highPricePoint += "00"
            searchTermRefined += lowPricePoint + "-" + highPricePoint
        self.url+= searchTermRefined + endOfUrl

    #parses a single price based on rules for the site
    def ParsePrice(self, price):
        splitPrice = price.split('$')
        if len(splitPrice) > 2:
            price = splitPrice[1]
        return price