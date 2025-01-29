from datetime import datetime
from pydantic import BaseModel


class ProjektasSchema(BaseModel):
    id: int
    manufacturer: str
    model: str
    engine_size: float
    power_output: float
    price: float
    priceVAT: float
    horse_power: float
    created_at: datetime

    class Config:
        from_attributes = True
