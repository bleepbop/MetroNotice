import requests

from fastapi import APIRouter

from ..secrets import API_KEY_SERVICE


router = APIRouter()

headers = {'api_key': API_KEY_SERVICE}

'''
@router.get('/bus')
async def get_bus_prediction():
    response = requests.get('https://api.wmata.com/Bus.svc/json/jBusPositions', headers=headers)
    return response.json()
'''

@router.get('/rail')
async def get_rail_prediction():
    response = requests.get('https://api.wmata.com/StationPrediction.svc/json/GetPrediction/all', headers=headers)
    return response.json()
