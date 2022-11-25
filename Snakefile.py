
import platform
import sys
import eel
from SiteService.Sites.WebSite import SiteType
from SiteService.SiteFactory import GenerateSiteList
from SiteService.SiteParser import ParseSitesForPrice

@eel.expose
def getTypes():
    typeNames = []
    for type in list(SiteType):
        if type.name != "Common":
            typeNames.append(type.name)
    return typeNames

@eel.expose
def getAveragePrices(priceLow, priceHigh, searchTerm, typeNames):
    types = []
    for typeName in typeNames:
        types.append(SiteType[typeName])
    sites = GenerateSiteList(types, searchTerm, priceLow, priceHigh)
    sites = ParseSitesForPrice(sites)
    returnSites = []
    for site in sites:
        returnSites.append({
            "name": site.siteName,
            "averagePrice": site.averagePrice,
            "amountOfPrices": site.amountOfPrices
        })
    return returnSites


def start_eel(develop):
    if develop:
        directory = 'src'
        app = 'chrome'
        page = {'port': 3000}
    else:
        directory = 'build'
        app = 'chrome-app'
        page = 'index.html'

    eel.init(directory, ['.tsx', '.ts', '.jsx', '.js', '.html'])

    eel_kwargs = dict(
        host='localhost',
        port=8080,
        size=(500, 800),
    )
    try:
        eel.start(page, mode=app, **eel_kwargs)
    except EnvironmentError:
        # If Chrome isn't found, fallback to Microsoft Edge on Win10 or greater
        if sys.platform in ['win32', 'win64'] and int(platform.release()) >= 10:
            eel.start(page, mode='edge', **eel_kwargs)
        else:
            raise


if __name__ == '__main__':
    import sys

    # Pass any second argument to enable debugging
    start_eel(develop=len(sys.argv) == 2)