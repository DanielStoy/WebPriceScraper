from statistics import mean

#sets up a site with the correct average price
def FindAverageSitePrice(site, prices):
    refinedPrices = []
    for price in prices:
        price = site.ParsePrice(price)
        try:
            price = float(price)
        except:
            price = 0
        refinedPrices.append(price)
    
    site.averagePrice = round(mean(refinedPrices), 2)
    site.amountOfPrices = len(refinedPrices)
    return site