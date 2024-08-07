from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
import pandas as pd
def load_data_to_database():
    load_dotenv()
    location_dim= pd.read_csv('data/processed/location_dim.csv')

    fact_pollution=pd.read_csv('data/processed/fact_pollution.csv')

    # persiste dans la base de données
    db_url = os.getenv("DB_URL")
    engine = create_engine(db_url)

    location_dim.to_sql('location_dim', con=engine, if_exists='replace', index=False)
    
    fact_pollution.to_sql('fact_pollution', con=engine, if_exists='replace', index=False)
    print("Data loaded to database")
    pass




