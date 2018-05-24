import json
import requests
from config import Config


def pull_json(url):
    response = requests.get(url)
    response.raise_for_status()
    json_data = json.loads(response.text)
    return json_data


def gmaps_geolocator(city, state):
    url = Config.GGL_URL.format(place=city, state=state, key=Config.GGL_KEY)
    geometry_data = pull_json(url)
    place_latitude = geometry_data['results'][0]['geometry']['location']['lat']
    place_longitude = geometry_data['results'][0]['geometry']['location']['lng']
    return place_latitude, place_longitude


def get_dgcr(city, state):
    lat, lng = gmaps_geolocator(city, state)
    url = Config.DGCR_URL.format(key=Config.DGCR_KEY, lat=lat, lng=lng, sig=Config.DGCR_SIG)
    dgcr_data = pull_json(url)
    return dgcr_data
