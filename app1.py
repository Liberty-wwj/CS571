from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <form method="post">
            City in USA: <input type="text" name="city">
            State in USA: <input type="text" name="state">
            <input type="submit" value="Submit">
        </form>
    '''

@app.route('/', methods=['POST'])
def get_zipcode():
    city = request.form['city']
    state = request.form['state']
    result = requests.get(f'https://api.zippopotam.us/us/{state}/{city}').json()
    # https://api.zippopotam.us/us/ca/milpitas
    zip_codes = [place['post code'] for place in result['places']]
    try:
        return f"Zipcode for {city}: {zip_codes[0]}"
    except KeyError:
        return f"No zipcode found for {city}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
