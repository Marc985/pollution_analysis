import pandas as pd
import numpy as np
import datetime
from dotenv import load_dotenv
import os

def clean_and_transform_data(input_filename='data/raw/pollution_data.csv', output_filename='data/processed/transformed_pollution_data.csv'):
    df = pd.read_csv(input_filename)

    df.fillna({
        'aqi': -1,
        'pm2_5': -1,
        'pm10': -1,
        'o3': -1,
        'no2': -1,
        'so2': -1,
        'co': -1
    }, inplace=True)

    df['date'] = pd.to_datetime(df['date'], unit='s',utc=True).dt.strftime('%Y-%m-%d')

    df.drop_duplicates(inplace=True)

    def get_pollution_level(aqi):
        if aqi == 1:
            return 'Good'
        elif aqi == 2:
            return 'Fair'
        elif aqi == 3:
            return 'Moderate'
        elif aqi == 4:
            return 'Poor'
        elif aqi == 5:
            return 'Very Poor'

    df['pollution_level'] = df['aqi'].apply(get_pollution_level)

    df.to_csv(output_filename, index=False)

    create_star_modal()
    pass


def create_star_modal():
    load_dotenv()
    demographic=pd.read_csv('data/raw/Demographic_Data.csv')
    geographic=pd.read_csv('data/raw/Geographic_Data.csv')
    location_dim= pd.concat([demographic,geographic],axis=1)

    # Supprimer les colonnes redondantes en gardant la première occurrence
    location_dim = location_dim.loc[:, ~location_dim.columns.duplicated()]

    # Renommer les colonnes pour les rendre plus explicites
    location_dim.rename(columns={'Location':'location'},inplace=True)

    fact_pollution=pd.read_csv('data/processed/transformed_pollution_data.csv')
    #creer la table de fait
    fact_pollution=fact_pollution.merge(location_dim['location'],on='location',how='left')

    location_dim.to_csv('data/processed/location_dim.csv',index=False)
    fact_pollution.to_csv('data/processed/fact_pollution.csv',index=False)
    pass

