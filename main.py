# Import necessary libraries
import os
from dotenv import load_dotenv

from sqlalchemy import create_engine

import pandas as pd


# Data cleaning
def wrangle(filepath):
    # Load the dataset
    df = pd.read_csv(filepath)

    # Remove rows missing with missing value(s)
    df.dropna(inplace=True)

    # Convert price_usd to float
    df['price_usd'] = df['price_usd'].str.replace('$', '').str.replace(',', '').astype(float)

    return df

# Data transformation
def transform(df):
    df['price_per_m2'] = round(df['price_usd'] / df['area_m2'],2)
    df.sort_values('price_per_m2', ignore_index=True)

    return df

# Data Loading
def load(df, table_name, schema):
    load_dotenv()

    # Database connection
    connection_uri = os.getenv("CONNECTION_URI")
    print('Connecting to the database...')

    db_engine = create_engine(connection_uri)
    print('Connected to the database.')

    return df.to_sql(table_name, db_engine, schema=schema, if_exists='replace')  


def etl():
    # Data Cleaning and Transformation
    mexico_real_estate = wrangle('mexico-real-estate-1.csv')
    print("Done wrangling the data.")

    mexico_real_estate = transform(mexico_real_estate)
    print("Done transforming the data.")

    print("Loading data into the database...")
    load(mexico_real_estate, 'mexico_real_estate', 'public')

    print("Data loaded successfully into the database.")     


etl()
