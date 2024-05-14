class Weather():
    def __init__(self,name: str = "",country: str = "",temp_c: float = 0.0,temp_f: float = 0.0,
        is_day: int = 0,condition_text: str = "",condition_icon: str = "",wind_mph: float = 0.0,
        wind_kph: float = 0.0,wind_degree: int = 0,wind_dir: str = "",pressure_mb: float = 0.0,
        pressure_in: float = 0.0,precip_mm: float = 0.0,precip_in: float = 0.0,humidity: int = 0,
        cloud: int = 0,feelslike_c: float = 0.0,feelslike_f: float = 0.0,vis_km: float = 0.0,
        vis_miles: float = 0.0,uv: float = 0.0,gust_mph: float = 0.0,gust_kph: float = 0.0,
    ):
        self.name = name
        self.country = country
        self.temp_c = temp_c
        self.temp_f = temp_f
        self.is_day = is_day
        self.condition_text = condition_text
        self.condition_icon = condition_icon
        self.wind_mph = wind_mph
        self.wind_kph = wind_kph
        self.wind_degree = wind_degree
        self.wind_dir = wind_dir
        self.pressure_mb = pressure_mb
        self.pressure_in = pressure_in
        self.precip_mm = precip_mm
        self.precip_in = precip_in
        self.humidity = humidity
        self.cloud = cloud
        self.feelslike_c = feelslike_c
        self.feelslike_f = feelslike_f
        self.vis_km = vis_km
        self.vis_miles = vis_miles
        self.uv = uv
        self.gust_mph = gust_mph
        self.gust_kph = gust_kph

    name: str
    country: str
    temp_c: float
    temp_f: float
    is_day: 0
    condition_text:str
    condition_icon:str
    wind_mph: float
    wind_kph: float
    wind_degree: int
    wind_dir: str
    pressure_mb: float
    pressure_in: float
    precip_mm: float
    precip_in: float
    humidity: int
    cloud: int
    feelslike_c: float
    feelslike_f: float
    vis_km: float
    vis_miles: float
    uv: float
    gust_mph: float
    gust_kph: float