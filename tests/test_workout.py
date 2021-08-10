from workout import __version__
from workout.models import Food, Nutrient, Serving, NutritionalValue, FoodNutrient


def test_version():
    assert __version__ == '0.1.0'

def test_create_food_nutrient():
    apple = Food(name="apple")
    vitc = Nutrient(name="Vitamin C", description="Vitamin C description")
    serving = Serving(size=1, units="dimensionless")
    nv = NutritionalValue(
            food=apple,
            nutrient=vitc,
            value=10,
            units="mg",
            serving=serving)
    assert nv

def test_reverse_lookup_nutrient():
    '''needs persistence'''
    pass

        
