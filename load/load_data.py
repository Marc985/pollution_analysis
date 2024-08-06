from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
import pandas as pd
def load_data_to_database():
    load_dotenv()
    demographic=pd.read_csv('Demographic_Data.csv')
    geographic=pd.read_csv('Geographic_Data.csv')
    location_dim= pd.concat([demographic,geographic],axis=1)

    # Supprimer les colonnes redondantes en gardant la première occurrence
    location_dim = location_dim.loc[:, ~location_dim.columns.duplicated()]

    # Renommer les colonnes pour les rendre plus explicites
    location_dim.rename(columns={'Location':'location'},inplace=True)
    fact_pollution=pd.read_csv('transformed_pollution_data.csv')
   

    #creer la table de fait
    fact_pollution=fact_pollution.merge(location_dim['location'],on='location',how='left')

    # persiste dans la base de données
    db_url = os.getenv("DB_URL")
    engine = create_engine(db_url)

    location_dim.to_sql('location_dim', con=engine, if_exists='replace', index=False)
    
    fact_pollution.to_sql('fact_pollution', con=engine, if_exists='replace', index=False)
    print("Data loaded to database")
    pass


