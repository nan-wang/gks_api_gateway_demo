import json
from flask import Response

SMOOTHIES = [
    {
        "id": 1,
        "name": "Sun Detox",
        "composition": "Mango, Carots, Ginger",
        "health_score": "5",
        "price": "5",
    },
    {
        "id": 2,
        "name": "Solaru Sunday",
        "composition": "Orange, Lime, Bubble",
        "health_score": "5",
        "price": "5",
    },
    {
        "id": 3,
        "name": "Alojito",
        "composition": "Aloe Vera, Mint, Lime",
        "health_score": "5",
        "price": "6",
    }

]

def listSmoothies(request):

    return Response(response = json.dumps(SMOOTHIES), status = 200)
