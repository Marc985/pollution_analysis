import requests
import os
from dotenv import load_dotenv
import pandas as pd

def collect_and_save_data(lat, lon, location):
    load_dotenv()
    app_id = os.getenv("APP_ID")
    base_params = {
        "lat": lat,
        "lon": lon,
        "appid": app_id
    }
    response = requests.get("http://api.openweathermap.org/data/2.5/air_pollution", params=base_params)

    # Vérifier le code de statut HTTP
    if response.status_code != 200:
        print(f"Erreur lors de l'appel à l'API: {response.status_code}")
        response.raise_for_status()

    response_data = response.json()
    print("Réponse de l'API:", response_data)

    updatedResponse = combine_aqi_and_components_from_api(response_data, location)
    append_data_to_csv(updatedResponse)
    return updatedResponse



def combine_aqi_and_components_from_api(data, location):
    aqi = data["list"][0]["main"]
    components = data["list"][0]["components"]
    combined_data = {**aqi, **components}
    combined_data["location"] =location 
    return combined_data


def append_data_to_csv(data, filename='pollution_data.csv'):
    df=pd.DataFrame([data])
    if os.path.exists(filename):
        existing_df = pd.read_csv(filename)
        updated_df=pd.concat([existing_df,df],ignore_index=True)
    else:
        updated_df=df
    updated_df.to_csv(filename,index=False)
