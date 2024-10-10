from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Ruta principal
@app.route('/', methods=['GET', 'POST'])
def index():
    pokemon_data = None
    if request.method == 'POST':
        pokemon_name = request.form['pokemon'].lower()
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}')
        if response.status_code == 200:
            pokemon_data = response.json()
        else:
            pokemon_data = None

    return render_template('index.html', pokemon=pokemon_data)

if __name__ == '__main__':
    app.run(debug=True)
