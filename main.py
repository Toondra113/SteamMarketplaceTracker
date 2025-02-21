import requests

#Search Marketplace for items
def get_skin_price(skin_name):
    url = f"https://steamcommunity.com/market/priceoverview/?currency=1&appid=730&market_hash_name={skin_name}"
    #URL for TF2 Marketplace API
    url = f"https://steamcommunity.com/market/priceoverview/?currency=<CURRENCY_ID>&appid=440&market_hash_name={skin_name}"
    #the json file that the url returns
    response = requests.get(url).json()
    #Search the item's json file for the lowest_price object and return the value
    return(response['lowest_price'])


while True:
    answer = input("Name Your Skin: ")