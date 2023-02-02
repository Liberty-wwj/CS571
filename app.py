from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <form method="post">
            Zip Code in USA: <input type="text" name="zipcode">
            <input type="submit" value="Submit">
        </form>
    '''

@app.route("/", methods=["POST"])
def get_weather():
    zip_code = request.form['zipcode'] 
    api_key = "83127daeecb54dcc8a2220846230202"
    weather_url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={zip_code}"
    weather_data = requests.get(weather_url).json()
#http://api.weatherapi.com/v1/current.json?key=83127daeecb54dcc8a2220846230202&q=95035
    if "error" in weather_data:
        return jsonify({"error": weather_data["error"]}), 400

    location = weather_data["location"]
    current = weather_data["current"]

    return jsonify({
        "location": location["name"],
        "region": location["region"],
        "country": location["country"],
        "temp_c": current["temp_c"],
        "condition": current["condition"]["text"],
        "icon": current["condition"]["icon"],
    })
    

if __name__ == "__main__":
    app.run(debug=True, port=5000)

