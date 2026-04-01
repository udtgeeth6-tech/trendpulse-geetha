#Perform analysis
import pandas as pd

def analyze_data():
    df = pd.read_csv("trending_coins_cleaned.csv")

    print("\nTop 5 Coins:")
    print(df.head())

    print("\nAverage Market Rank:")
    print(df['market_cap_rank'].mean())

    print("\nHighest BTC Price Coin:")
    print(df.loc[df['price_btc'].idxmax()])

if __name__ == "__main__":
    analyze_data()
