from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import os
app = Flask(__name__)
import get_weather
import my_yelp
import all_amazon

# app.run(debug=True)

@app.route("/")
def index():
    name = request.values.get('name')
    return render_template('index.html', name=name)

@app.route('/about')
def about():
    name = request.values.get('name')
    return render_template('about.html', name=name)

@app.route('/yelp')
def yelp():
    address = request.values.get('address')
    term = request.values.get('term')
    businesses = None
    if address and term:
        businesses = my_yelp.yelp_lookup(address, term)
    return render_template('yelp.html', businesses=businesses)

@app.route('/amazon')
def amazon():
    search_term = request.values.get('search-term')
    csvfile = None
    if search_term:
        csvfile = all_amazon.alookup(search_term)
        print(csvfile)
    return render_template('amazon.html', csvfile=csvfile)

@app.route('/weather')
def weather():
    address = request.values.get('address')
    forecast = None
    if address:
        forecast = get_weather.weather(address)
    return render_template('weather.html', forecast=forecast)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
