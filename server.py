from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/transform', methods=['POST'])
def receive_transform():
    data = request.json
    print("Received Transform Data:", data)
    return jsonify({"message": "Transform received successfully!"})

@app.route('/translation', methods=['POST'])
def receive_translation():
    data = request.json
    print("Received Translation Data:", {"name": data['name'], "location": data['location']})
    return jsonify({"message": "Translation received successfully!"})

@app.route('/rotation', methods=['POST'])
def receive_rotation():
    data = request.json
    print("Received Rotation Data:", {"name": data['name'], "rotation": data['rotation']})
    return jsonify({"message": "Rotation received successfully!"})

@app.route('/scale', methods=['POST'])
def receive_scale():
    data = request.json
    print("Received Scale Data:", {"name": data['name'], "scale": data['scale']})
    return jsonify({"message": "Scale received successfully!"})

if __name__ == "__main__":
    app.run(debug=True, port=8000)
