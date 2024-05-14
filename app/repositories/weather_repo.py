import requests
from app.models.weather import Weather
from app.repositories.location_repo import *

import dataclasses, json

BASE_URL = r"http://api.weatherapi.com/v1/"
API_KEY = r"16220d660b5a436587230918240605"


def get_weather_by_zip(zip_code: int):
    response = requests.get(BASE_URL+f"current.json?key={API_KEY}&q={zip_code}")
    res= response.json()
    return res
    

def get_weather(city:str):
    response = requests.get(BASE_URL+f"current.json?key={API_KEY}&q={city}")
    res= response.json()
    return res
