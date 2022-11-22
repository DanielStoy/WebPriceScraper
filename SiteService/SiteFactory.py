from .Sites.KayJewlersSite import KayJewlersSite
from .Sites.AmazonSite import AmazonSite
from .Sites.WebSite import SiteType

sites = []
sites.append(KayJewlersSite())
sites.append(AmazonSite())

#factory to prepare the sites, searches for the type we want and prepares the search terms
#Common sites are always returned
def GenerateSiteList(sitetype, searchTerm, highPricePoint, lowPricePoint):
    sitesOfType = []
    for site in sites:
        if(sitetype in site.type or SiteType.Common in site.type):
            site.SetupURL(searchTerm, highPricePoint, lowPricePoint)
            sitesOfType.append(site)

    return sitesOfType

