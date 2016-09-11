from os import environ
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
from geopy.geocoders import Nominatim
import forecastio

# Weather function
def weather(address):
    api_key = environ["API_KEY"]
    # alternative: -- This won't flag an api_key error
    # api_key = environ.get("API_KEY")
    geolocator = Nominatim()
    location = geolocator.geocode(address)
    latitude = location.latitude
    longitude = location.longitude
    forecast = forecastio.load_forecast(api_key, latitude, longitude).currently()
    return "{} and {}° at {}".format(forecast.summary, forecast.temperature, address)
