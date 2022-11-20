from SiteService.Sites.KayJewlersSite import KayJewlersSite
from SiteService.Sites.WebSite import SiteType
from SiteService.SiteFactory import GenerateSiteList
from SiteService.SiteParser import ParseSitesForPrice

sites = GenerateSiteList(SiteType.Jewelery, "orange necklace", "50", "200")

for site in sites:
    print(site.url)

prices = ParseSitesForPrice(sites)

print(prices)