from SiteService.Sites.KayJewlersSite import KayJewlersSite
from SiteService.Sites.WebSite import SiteType
from SiteService.SiteFactory import GenerateSiteList
from SiteService.SiteParser import ParseSitesForPrice

sites = GenerateSiteList(SiteType.Jewelery, "ring", "50", "200")

for site in sites:
    print(site.url)

sites = ParseSitesForPrice(sites)

for site in sites:
    print(site.siteName)
    print("Average Price: " + str(site.averagePrice))
    print("Amount of prices: " + str(site.amountOfPrices))