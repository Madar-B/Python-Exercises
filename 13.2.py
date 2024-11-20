from flask import Flask, jsonify, abort

app = Flask(__name__)

# Статическая база данных для примера
airports = {
    "EFHK": {"Name": "Helsinki Vantaa Airport", "Municipality": "Helsinki"},
    "EGLL": {"Name": "London Heathrow Airport", "Municipality": "London"},
    "KJFK": {"Name": "John F. Kennedy International Airport", "Municipality": "New York"}
}

@app.route('/kenttä/<string:icao>', methods=['GET'])
def get_airport(icao):
    # Проверяем, есть ли код ICAO в базе данных
    airport = airports.get(icao.upper())
    if not airport:
        abort(404, description="Airport not found")

    # Возвращаем данные в формате JSON
    return jsonify({"ICAO": icao.upper(), **airport})

if __name__ == '__main__':
    app.run(debug=True)
