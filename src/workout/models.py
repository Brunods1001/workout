import os
from pydantic import BaseModel
from typing import Optional, Any
from pint import UnitRegistry, Quantity

ureg = UnitRegistry()
path_units = "./units.txt"
if os.path.exists(path_units):
    ureg.load_definitions(path_units)

class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None

class User(BaseModel):
    name: str

class Nutrient(BaseModel):
    name: str
    description: str

class Food(BaseModel):
    name: str

class Serving(BaseModel):
    size: float
    units: str
    quantity: Optional[Quantity] = None
    def __init__(self, **data: Any):
        super().__init__(**data)
        self.quantity = self.size * getattr(ureg, self.units)
    class Config:
        arbitrary_types_allowed = True

class NutritionalValue(BaseModel):
    food: Food
    nutrient: Nutrient
    value: float
    units: str
    serving: Serving
    quantity: Optional[Quantity] = None
    def __init__(self, **data: Any):
        super().__init__(**data)
        units = getattr(ureg, self.units)
        self.quantity = self.value * units

    class Config:
        arbitrary_types_allowed = True

class FoodNutrient(BaseModel):
    food: Food
    value: NutritionalValue
