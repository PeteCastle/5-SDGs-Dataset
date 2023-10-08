import requests
import pandas as pd

def get():
    # Get the data from the API
    url = 'https://unstats.un.org/sdgs/UNSDGAPIV5/v1/sdg/Goal/List'
    response = requests.get(url)

    # Convert the response to JSON format
    data = response.json()

    df = pd.DataFrame(data)
    df.to_csv('final/sdggoals.csv', index=False)
    return df
