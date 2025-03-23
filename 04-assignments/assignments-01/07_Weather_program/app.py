import requests

from pprint import pprint
from dotenv import load_dotenv
import os
load_dotenv()
# API_KEY = os.getenv('WEATHER_API_KEY')

API_KEY = '1b36e300b1c8f0d27fb73e2261b33b09'

city = input('Enter the city: ')

base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'

weather_data = requests.get(base_url).json()

pprint(weather_data)