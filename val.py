from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    # Get the first 150 Pokémon from the API
    response = requests.get("https://valorant-api.com/v1/weapons")
    data = response.json()
    weapons_list = data['results']

    weapons = []

    for weapon in weapons_list:
        url = weapon['url']
        parts = url.strip("/").split("/")
        id = parts[-1]
