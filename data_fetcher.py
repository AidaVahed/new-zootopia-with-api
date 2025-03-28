import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv('API_KEY')

print(API_KEY)

API_URL = "https://api.api-ninjas.com/v1/animals?name="


def fetch_data(animal_name):
    """
    Fetches the animal data from the API for a given animal name.
    Returns a list of animals, where each animal is a dictionary with the expected format.
    If no data is found, returns an empty list.
    """
    headers = {"X-Api-Key": API_KEY}

    try:
        response = requests.get(API_URL + animal_name, headers=headers)
        response.raise_for_status()

        data = response.json()

        if isinstance(data, list) and data:
            return data
        else:
            return []

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return []
