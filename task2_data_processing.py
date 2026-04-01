#Clean and prepare data
import pandas as pd

def clean_data():
    df = pd.read_csv("trending_coins_raw.csv")

    # Handle missing values
    df = df.dropna()

    # Convert data types if needed
    df['market_cap_rank'] = df['market_cap_rank'].astype(int)

    # Sort by rank
    df = df.sort_values(by='market_cap_rank')

    df.to_csv("trending_coins_cleaned.csv", index=False)
    print("Data cleaned and saved!")
    
if __name__ == "__main__":
    clean_data()
