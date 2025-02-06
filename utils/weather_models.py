from pydantic import BaseModel, ConfigDict
from typing import List, Dict, Any, Optional

class WeatherDescription(BaseModel):
    id: int
    main: str
    description: str
    icon: str

    model_config = ConfigDict(extra="forbid")

class MainWeatherData(BaseModel):
    temp: float
    feels_like: float
    temp_min: float
    temp_max: float
    pressure: int
    humidity: int
    sea_level: Optional[int] = None  # Now optional
    grnd_level: Optional[int] = None  # Now optional

    model_config = ConfigDict(extra="forbid")

class WeatherResponse(BaseModel):
    coord: Dict[str, float]
    weather: List[WeatherDescription]
    main: MainWeatherData
    visibility: int
    wind: Dict[str, Any]
    clouds: Dict[str, int]
    dt: int
    sys: Dict[str, Any]
    timezone: int
    id: int
    name: str
    cod: int
    base: str

    model_config = ConfigDict(extra="forbid")
