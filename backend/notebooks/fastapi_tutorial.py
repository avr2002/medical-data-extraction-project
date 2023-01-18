from fastapi import FastAPI
from enum import Enum

'''
http REST protocol:
    GET method: used to Read Data
    POST: Create data
    PUT: Update data
    DELETE: delete data
'''

# @app.get("/hello")
# async def hello():
#     return "Welcome to FastAPI"

# @app.get("/hello/{name}")
# async def hello(name):
#     return f"Welcome to FastAPI tutorial {name}"


app = FastAPI()


# Enum is used if you have fixed categories of class
class AvailableCuisines(str, Enum):
    indian = "indian"
    american = "american"
    italian = "italian"


food_items = {
    'indian': ["Samosa", "Papdi Chaat"],
    'american': ["Hot Dog", "Apple Pie"],
    'italian': ["Ravioli", "Pizza"]
}


@app.get("/get_items/{cuisine}")
async def hello(cuisine: AvailableCuisines):

    # So, instead of writing below if condition for generating error or for validating our i/p value, we can use
    # FastAPIs auto validation feature using the above way show by using enum and making a class for available cuisines

    # if cuisine not in food_items.keys():
    #      return f"Supported cuisines are - {list(food_items.keys())}"

    return food_items.get(cuisine)


coupon_code = {
    1: '10%',
    2: '20%',
    3: '30%'
}

@app.get("/get_coupon/{code}")
async def get_discount(code: int):
    return {'discount_amount': coupon_code.get(code)}
