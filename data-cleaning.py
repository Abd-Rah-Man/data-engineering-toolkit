# data cleaning script

# Import necessary libraries
import pandas as pd

def wrangle(filepath):
    # Load the dataset
    df = pd.read_csv(filepath)

    # Remove missing rows
    df.dropna(inplace=True)

    # Convert price_usd to float
    df['price_usd'] = df['price_usd'].str.replace('$', '').str.replace(',', '').astype(float)

    return df