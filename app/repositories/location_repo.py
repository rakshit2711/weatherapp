from app.db.db_config import get_db
from sqlalchemy import func, and_
from typing import Optional
from app.models.models import Country, State, City
import json

def get_cities_by_country(country:str):
    db = get_db()
    base_condition = func.lower(Country.country_name) == func.lower(country)
    res = db.query(City).join(State).join(Country).filter(base_condition).all();
    res = convert_to_city_state_country(res);
    res = json.dumps(res)
    db.close_all()
    return res

def get_cities_by_state(country: str, state: str):
    db = get_db()
    base_condition = func.lower(Country.country_name) == func.lower(country) 
    base_condition = and_(base_condition, func.lower(State.state_name) == func.lower(state))
    res = db.query(City).join(State).join(Country).filter(base_condition).all();
    res = convert_to_city_state_country(res);
    res = json.dumps(res)
    db.close_all()
    return res


def get_city(country: str, city: str):
    db = get_db()
    base_condition = func.lower(Country.country_name) == func.lower(country)
    base_condition = and_(base_condition, func.lower(City.city_name) == func.lower(city))
    res = db.query(City).join(State).join(Country).filter(base_condition).all();
    res = convert_to_city_state_country(res);
    res = json.dumps(res)
    db.close_all()
    return res

def get_location_like(loc_name: str):
    db = get_db()
    res = db.query(City).join(State).join(Country).filter(func.lower(City.city_name).like(f"%{loc_name.lower()}%")).all();
    res = convert_to_city_state_country(res)
    db.close_all()
    return res

def convert_to_city_state_country(res):
    list_of_city_state_country = []
    for city in res:
        list_of_city_state_country.append({"city":city.city_name,"state":city.state.state_name,"country":city.state.country.country_name})
    return list_of_city_state_country

