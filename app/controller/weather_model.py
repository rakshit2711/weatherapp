from fastapi import APIRouter
from 

weather_router =APIRouter()

@weather_router.get("/weather")
def get_weather_by_city(city:str):
    weathe
    return {"city":city}