from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
from geopy.geocoders import Nominatim
import json
from os import environ
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

# Prompts for user to enter their address
# address = input("What's your city? ")
# search_term = input("What are you looking for?")

# Function returns a dictionary of businesses based on user input
def yelp_lookup(address, search_term):
    auth = Oauth1Authenticator(
        consumer_key = environ["CONSUMER_KEY"],
        consumer_secret = environ["CONSUMER_SECRET"],
        token = environ["TOKEN"],
        token_secret = environ["TOKEN_SECRET"]
    )

    client = Client(auth)
    params = {
        'term': search_term,
        'lang':'en',
# Use the limit parameter to return the top 3 results for the search
        'limit': 3
    }
    response = client.search(address, **params)

# Create an empty list
    businesses = []
    for business in response.businesses:
        businesses.append({"business":business.name, 
            "phone":business.display_phone, 
            "address":business.location.display_address
        })
    return businesses

# businesses = yelp_lookup(address, search_term)

# print(businesses)


# for keys, value in businesses.items():
    # print("{} {}".format(keys, value))
    # print("%s : %s" % (keys, value))
    


# This prints dictionary but not is easy to read format
# print(json.dumps(businesses, indent=2))

# This didn't work to print dictionary
# for x in businesses:
#     print(x)
#     for y in businesses[x]:
#         print(y,":",businesses[x][y])
#         for z in businesses[x][y]:
#             print(z,":",businesses[x][y][z])

# for business in response.businesses:
# 		print(" {} Ph: {} at {}".format(business.name, business.display_phone, business.location.display_address))
