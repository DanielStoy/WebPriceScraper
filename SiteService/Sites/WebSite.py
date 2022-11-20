from enum import Enum

#Different site types
class SiteType(Enum):
    Common = 1, #sites like amazon where many different objects can be found. These are used in every search
    Jewelery = 2 #sites like kay jewlers where jewlery can be found

#Sites are the areas that we want to parse
class WebSite:
    url = "" #base url of the site
    type = [] #type of site, sites can be multiple types
    classNameForPrice = "" #class name to search the html for

    #setup the url to do search
    #search term is the object we want to search for
    #low price point is the lower end of the price
    #high price point is the upper end of the price
    def SetupURL(self, searchTerm, lowPricePoint, highPricePoint):
        pass

    #parses the price and removes all the useless stuff except for the thing we actually need
    def ParsePrice(self, prices):
        pass

        