import requests

def extract_flights_data():
    url = 'https://opensky-network.org/api/states/all'

    response=requests.get(url)

    data=response.json()

    flight_list=data['states']
    
    return flight_list