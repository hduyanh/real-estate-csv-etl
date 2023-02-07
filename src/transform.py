import pandas as pd
from pathlib import Path
import warnings

warnings.filterwarnings('ignore')

def save_nan_to_csv(file_data):
    missing_values = file_data[file_data.isna().any(axis=1)]
    missing_values.fillna('missing data', inplace=True)
    filepath = Path(r'D:\Git\real-estate-csv-etl\data\processed\missing_values.csv')
    missing_values.to_csv(filepath)

def file_cleaner(file_data):
    df = file_data[~file_data.isna().any(axis=1)] # drop NaN
    df['Price'] = df['Price'].str.replace('$','').str.replace(',','').astype(float) # convert price to float
    df['Square meter'] = (df['Area (ft.)'] * 0.09290304).round(2) # convert feet to meter
    df['Price per meter'] = (df['Price'] / df['Square meter']).round(2) # calculate price/meter
    df['Sales ID'] = df['ID'].map(str) + df['Customer ID'] # generate sales ID
    df[['Year of sale', 'Month of sale', 'Y', 'M', 'D']] = df[['Year of sale', 'Month of sale', 'Y', 'M', 'D']].astype(int) # convert to integer
    return df