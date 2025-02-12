from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/transform', methods=['POST'])
def receive_transform():
    data = request.json
    print("Received Transform Data:", data)
    return jsonify({"message": "Transform received successfully!"})

if __name__ == "__main__":
    app.run(debug=True, port=8000)
