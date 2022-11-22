from .WebSite import WebSite
from .WebSite import SiteType

#kay jewlers site used for jewlery
class KayJewlersSite(WebSite):
    type = [SiteType.Jewelery]
    classNameForPrice = "price"
    siteName = "Kay Jewlers"
    averagePrice = 0
    amountOfPrices = 0
    headers = None

    def SetupURL(self, searchTerm, lowPricePoint, highPricePoint):
        terms = searchTerm.split()
        self.url = "https://www.kay.com/search?q="
        searchTermRefined = ""

        if(len(terms) == 1):
            searchTermRefined = searchTerm
        else:
            for i in range(len(terms)):
                if( i == len(terms) - 1):
                    searchTermRefined += terms[i]
                else:
                    searchTermRefined += terms[i] +'+'
        endOfUrl = ""

        if(lowPricePoint != ""):
            searchTermRefined += ":_relevance_Ascending:nowPriceValue_usd_double:" + highPricePoint + ".." + lowPricePoint
            endOfUrl = "&searchStore=&storePickup=false&sameDayDelivery=false"
        else:
            endOfUrl = "&gbapi_org=ue&gbapiv2=false"

        self.url += searchTermRefined + endOfUrl
    
    def ParsePrice(self, price):
        priceSplit = price.split('(')
        if(len(priceSplit) == 1):
            price = price.replace('$', '')
        else:
            price = priceSplit[0].replace('$', '')
        price = price.split()
        
        return price[0]
