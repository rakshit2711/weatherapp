import json
from app.models.models import Country, State, City
from app.db.db_config import get_db
# Opening JSON file
def read_json_file():
    f = open(r"C:\Users\raksh\OneDrive\Desktop\countries+states+cities.json", encoding="utf8")
    
    data = json.load(f)
    for country in data:
        import_json_data(country)


def import_json_data(country_data):
    # Create the country object from JSON data
    
    db =get_db()
    country = Country(
        country_name=country_data["name"],
        country_code=country_data["iso3"],
        capital=country_data["capital"],
        region=country_data["region"],
        subregion=country_data["subregion"],
    )
    # Add the country to the session
    
    print(country)
    db.add(country)
    db.commit()
    db.refresh(country)
    
    print(country)
    # Insert states and cities
    if "states" in country_data:
        for state_data in country_data["states"]:
            state = State(
                state_name=state_data["name"],
                state_code=state_data["state_code"],
                country=country,  # Associate with the country
            )
            
            db.add(state)
            db.commit()
            db.refresh(state)
            print(state)
            
            if "cities" in state_data:
                for city_data in state_data["cities"]:
                    city = City(
                        city_name=city_data["name"],
                        state=state,  # Associate with the state
                    )
                    
                    db.add(city)
                    db.commit()
                    db.refresh(city)
                    print(city)
