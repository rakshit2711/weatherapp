from fastapi import APIRouter, Query, Request,Response
from typing import Optional

from fastapi.responses import HTMLResponse
from app.repositories import location_repo

from fastapi.templating import Jinja2Templates

location_router =APIRouter()
templates = Jinja2Templates(directory="templates")

@location_router.get("/location/country/{country}")
async def get_location_by_country(country: str):
    cities=location_repo.get_cities_by_country(country)
    context ={"cities" : cities }
    return context

@location_router.get("/location/country/{country}/state/{state}")
async def get_location_by_state(country: str,state: str):
    cities = location_repo.get_cities_by_state(country,state)
    context ={"cities" : cities }
    return context


@location_router.get("/location/country/{country}/city/{city}")
async def get_location_by_city(country: str,city:str):
    cities = location_repo.get_city(country,city)
    context ={"cities" : cities }
    return context
    

@location_router.get("/location/location_like/{loc_name}",response_class=HTMLResponse)
async def get_location_like(request: Request,loc_name: str):
    cities = location_repo.get_location_like(loc_name)
    context ={"request": request,"cities" : cities }
    
    return templates.TemplateResponse("table.html", context=context)
