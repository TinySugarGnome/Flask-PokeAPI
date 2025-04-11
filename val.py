from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    # Fetch weapon data from Valorant API
    response = requests.get("https://valorant-api.com/v1/weapons")
    data = response.json()
    weapons_list = data['data']  # This is correct

    weapons = []

    for weapon in weapons_list:
        weapon_id = weapon.get('uuid')
        name = weapon.get('displayName', 'Unknown Weapon')
        icon = weapon.get('displayIcon')

        weapons.append({
            'id': weapon_id,
            'name': name,
            'icon': icon
        })

    return render_template("index.html", weapons=weapons)