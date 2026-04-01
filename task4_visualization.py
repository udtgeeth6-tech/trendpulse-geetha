#Visualize trends
import pandas as pd
import matplotlib.pyplot as plt

def visualize_data():
    df = pd.read_csv("trending_coins_cleaned.csv")

    # Bar chart for market rank
    plt.figure()
    plt.bar(df['name'], df['market_cap_rank'])
    plt.title("Market Cap Rank of Trending Coins")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Line chart for BTC price
    plt.figure()
    plt.plot(df['name'], df['price_btc'], marker='o')
    plt.title("BTC Price Trend")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    visualize_data()
