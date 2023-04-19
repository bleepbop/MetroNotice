import requests

from fastapi import APIRouter

from secrets import API_KEY_SERVICE


router = APIRouter()

headers = {'api_key': API_KEY_SERVICE}


@router.get('/bus')
async def get_bus_incident():
    response = requests.get('https://api.wmata.com/Incidents.svc/json/BusIncidents', headers=headers)
    return response.json()


@router.get('/rail')
async def get_rail_incident():
    response = requests.get('https://api.wmata.com/Incidents.svc/json/Incidents', headers=headers)
    return response.json()


@router.get('/outages')
async def get_outages():
    response = requests.get('https://api.wmata.com/Incidents.svc/json/ElevatorIncidents', headers=headers)
    return response.json()
