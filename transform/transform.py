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
    return df


