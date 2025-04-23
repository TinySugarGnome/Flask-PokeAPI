

from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def index():
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

@app.route("/calculate_cost", methods=["POST"])
def calculate_cost():
    try:
        quantity = int(request.form["quantity"])
        weapon_id = request.form["weapon_id"] 
        weapon_cost = float(request.form["weapon_cost"])
        weapon_name = request.form["weapon_name"]

        # Calculate the total cost
        total_cost = quantity * weapon_cost

        # Render the result page
        return render_template("total_cost.html", 
                               weapon_name=weapon_name, 
                               quantity=quantity, 
                               total_cost=total_cost)
    except KeyError as e:
        return f"Missing form data: {str(e)}", 400
    except ValueError as e:
        return f"Invalid input: {str(e)}", 400
    
if __name__ == "__main__":
    app.run(debug=True)