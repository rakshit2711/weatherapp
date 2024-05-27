from fastapi import FastAPI, Request,Response
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.controller import weather_controller
from app.controller import location_controller
from sqlalchemy.orm import Session
from fastapi import FastAPI

app = FastAPI()

app.include_router(weather_controller.weather_router)
app.include_router(location_controller.location_router)
# app.state.limiter = limiter

# app.add_exception_handler(ArithmeticError,)

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/health")
def read_root():
    return Response("Server is running")


@app.get("/",response_class=HTMLResponse)
def index(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("index.html", context=context)


@app.get("/weather/{city}",response_class=HTMLResponse)
def weather(request: Request,city:str):
    cities = weather_controller.fetch_weather(city)
    
    context = {"request": request,"cities" : cities}

    return templates.TemplateResponse("weather.html", context=context)



@app.get("/about",response_class=HTMLResponse)
def weather(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("about.html", context=context)
