from fastapi import APIRouter, Query
from typing import Optional
from app.repositories import weather_repo
weather_router =APIRouter()

@weather_router.get("/fetch_weather/{city}")
def fetch_weather(city: str):
    
    return weather_repo.get_weather( city)

# Commented out due to unavailability for zip code
# @weather_router.get("/weather/country/{zipcode}")
# def fetch_weather_zip(zipcode: int):
    
#     return weather_repo.get_weather_by_zip(zipcode)
