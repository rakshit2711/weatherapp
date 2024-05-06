from fastapi import APIRouter

weather_router =APIRouter()

@weather_router.get("/weather")
def get_weather_by_city(city:str):
    
    return {"city":city}