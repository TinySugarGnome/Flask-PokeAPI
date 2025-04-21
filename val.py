from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    # Fetch weapon data from Valorant API
    response = requests.get("https://valorant-api.com/v1/weapons")
    data = response.json()
    weapons_list = data['data']  

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

@app.route("/weapon/<weapon_id>")
def weapon_detail(weapon_id):
    response = requests.get(f"https://valorant-api.com/v1/weapons/{weapon_id}")
    if response.status_code != 200:
        return "Weapon not found", 404
    weapon = response.json().get('data', {})
    return render_template("weapon_detail.html", weapon=weapon)
app.run(debug=True)