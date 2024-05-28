import requests


def get_coordinates(direction):
    url = 'https://maps.googleapis.com/maps/api/geocode/json'

    params = {
        'address': direction,
        'key': 'AIzaSyD3P92A-pN_zX_eTQREvP8HckRgFeMzTb0'
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:

        data = response.json()

        if data['status'] == 'OK':

            location = data['results'][0]['geometry']['location']
            latitud = location['lat']
            longitud = location['lng']
            return f'{latitud},{longitud}'
        else:
            return 0


def get_coordinates_and_location(direction):
    url = 'https://maps.googleapis.com/maps/api/geocode/json'

    params = {
        'address': direction,
        'key': 'AIzaSyD3P92A-pN_zX_eTQREvP8HckRgFeMzTb0'
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:

        data = response.json()

        if data['status'] == 'OK':

            location = data['results'][0]['geometry']['location']
            latitud = location['lat']
            longitud = location['lng']

            address_components = data['results'][0]['address_components']
            municipio = next(
                (component['long_name'] for component in address_components if 'locality' in component['types']), None)
            departamento = next(
                (component['long_name'] for component in address_components if 'administrative_area_level_1' in component['types']), None)
            coordinates = f'{latitud},{longitud}'
            return coordinates, municipio, departamento
        else:
            return None, None, None
    else:
        return None, None, None
