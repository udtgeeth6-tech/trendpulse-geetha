from numpy import show_runtime
#task1_data_collection.py
import requests
import pandas as pd

def fetch_data():
    url = "https://api.coingecko.com/api/v3/search/trending"
    response = requests.get(url)
    data = response.json()

    coins = data['coins']
    
    coin_list = []
    for coin in coins:
        item = coin['item']
        coin_list.append({
            "name": item['name'],
            "symbol": item['symbol'],
            "market_cap_rank": item['market_cap_rank'],
            "price_btc": item['price_btc']
        })

    df = pd.DataFrame(coin_list)
    df.to_csv("trending_coins_raw.csv", index=False)
    print("Data collected and saved!")
   
if __name__ == "__main__":
    fetch_data()
