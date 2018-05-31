import json
import time
import requests
import requests_cache
from config import Config

requests_cache.install_cache('dgcr_cache', backend='sqlite', expire_after=None)

def pull_json(url):
    response = requests.get(url)
    now = time.ctime(int(time.time()))
    print("Time: {} / Used Cache: {}".format(now, response.from_cache))
    response.raise_for_status()
    return json.loads(response.text)

def gmaps_geolocator(city, state):
    url = Config.GGL_URL.format(place=city, state=state, key=Config.GGL_KEY)
    geometry_data = pull_json(url)
    place_latitude = geometry_data['results'][0]['geometry']['location']['lat']
    place_longitude = geometry_data['results'][0]['geometry']['location']['lng']
    return place_latitude, place_longitude

def zip_gmaps(zip):
    url = Config.ZGGL_URL.format(zip=zip, key=Config.GGL_KEY)
    geometry_data = pull_json(url)
    place_latitude = geometry_data['results'][0]['geometry']['location']['lat']
    place_longitude = geometry_data['results'][0]['geometry']['location']['lng']
    return place_latitude, place_longitude

def get_dgcr(city, state, prox):
    lat, lng = gmaps_geolocator(city, state)
    url = Config.DGCR_URL.format(key=Config.DGCR_KEY, lat=lat, lng=lng, prox=prox, sig=Config.DGCR_SIG)
    dgcr_data = pull_json(url)
    return dgcr_data

def zip_dgcr(zip, prox):
    lat, lng = zip_gmaps(zip)
    url = Config.DGCR_URL.format(key=Config.DGCR_KEY, lat=lat, lng=lng, prox=prox, sig=Config.DGCR_SIG)
    dgcr_data = pull_json(url)
    return dgcr_data