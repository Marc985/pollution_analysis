import pandas as pd
import numpy as np


def clean_and_transform_data(input_filename='pollution_data.csv', output_filename='transformed_pollution_data.csv'):
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

    df['date'] = pd.to_datetime('today').normalize()

    df['pm2_5_level'] = pd.cut(df['pm2_5'], bins=[0, 12, 35, 55, np.inf], labels=['Good', 'Moderate', 'Unhealthy', 'Very Unhealthy'])
    df['pm10_level'] = pd.cut(df['pm10'], bins=[0, 50, 150, 250, np.inf], labels=['Good', 'Moderate', 'Unhealthy', 'Very Unhealthy'])

    def get_pollution_level(aqi):
        if aqi <= 50:
            return 'Good'
        elif aqi <= 100:
            return 'Moderate'
        elif aqi <= 150:
            return 'Unhealthy'
        else:
            return 'Very Unhealthy'

    df['pollution_level'] = df['aqi'].apply(get_pollution_level)

    df.to_csv(output_filename, index=False)
    return df


