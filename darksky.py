import requests
import os

from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get('DARKSKY_API_KEY')
base_url = f'https://api.darksky.net/forecast/{api_key}/'


def get_forecast(coord: tuple[float, float]):
    url = f'{base_url}{coord[0]},{coord[1]}'
    res = requests.get(url)

    return res.json()


def get_current_pressure(coord: tuple[float, float]) -> float:
    json = get_forecast(coord)
    pressure = json['currently']['pressure']

    return pressure
