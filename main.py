# Import necessary libraries
import pandas as pd

# data cleaning
def wrangle(filepath):
    # Load the dataset
    df = pd.read_csv(filepath)

    # Remove missing rows
    df.dropna(inplace=True)

    # Convert price_usd to float
    df['price_usd'] = df['price_usd'].str.replace('$', '').str.replace(',', '').astype(float)

    return df


# data transformation

def transform(df):
    df['price_per_m2'] = round(df['price_usd'] / df['area_m2'],2)
    df.sort_values('price_per_m2', ignore_index=True)

    return df

def etl():
    df = wrangle('mexico-real-estate-1.csv')
    df = transform(df)
    return df   

if __name__ == "__main__":
    df = etl()
    print(df)