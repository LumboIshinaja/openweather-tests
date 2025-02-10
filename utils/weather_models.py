from pydantic import BaseModel, ConfigDict
from typing import List, Dict, Any, Optional

class WeatherDescriptionModel(BaseModel):
    id: int
    main: str
    description: str
    icon: str

    model_config = ConfigDict(extra="forbid")

class MainWeatherDataModel(BaseModel):
    temp: float
    feels_like: float
    temp_min: float
    temp_max: float
    pressure: int
    humidity: int
    sea_level: Optional[int] = None
    grnd_level: Optional[int] = None

    model_config = ConfigDict(extra="forbid")

class WeatherResponseModel(BaseModel):
    coord: Dict[str, float]
    weather: List[WeatherDescriptionModel]
    main: MainWeatherDataModel
    visibility: int
    wind: Dict[str, Any]
    clouds: Dict[str, int]
    rain: Optional[Dict[str, float]] = None
    dt: int
    sys: Dict[str, Any]
    timezone: int
    id: int
    name: str
    cod: int
    base: str

    model_config = ConfigDict(extra="forbid")
