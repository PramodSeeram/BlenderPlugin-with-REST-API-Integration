from flask import Flask, request, jsonify
import time
from database import create_db, add_item, remove_item, update_quantity, get_inventory

app = Flask(__name__)


create_db()

@app.route('/transform', methods=['POST'])
def receive_transform():
    time.sleep(10)
    data = request.json
    if 'name' not in data or 'location' not in data or 'rotation' not in data or 'scale' not in data:
        return jsonify({"error": "Missing required data"}), 400
    print("Received Transform Data:", data)
    return jsonify({"message": "Transform received successfully!"}), 200

@app.route('/translation', methods=['POST'])
def receive_translation():
    time.sleep(10)
    data = request.json
    if 'name' not in data or 'location' not in data:
        return jsonify({"error": "Missing required data"}), 400
    print("Received Translation Data:", {"name": data['name'], "location": data['location']})
    return jsonify({"message": "Translation received successfully!"}), 200

@app.route('/rotation', methods=['POST'])
def receive_rotation():
    time.sleep(10)
    data = request.json
    if 'name' not in data or 'rotation' not in data:
        return jsonify({"error": "Missing required data"}), 400
    print("Received Rotation Data:", {"name": data['name'], "rotation": data['rotation']})
    return jsonify({"message": "Rotation received successfully!"}), 200

@app.route('/scale', methods=['POST'])
def receive_scale():
    time.sleep(10)
    data = request.json
    if 'name' not in data or 'scale' not in data:
        return jsonify({"error": "Missing required data"}), 400
    print("Received Scale Data:", {"name": data['name'], "scale": data['scale']})
    return jsonify({"message": "Scale received successfully!"}), 200

@app.route('/file-path', methods=['GET'])
def get_file_path():
    project_path = request.args.get('projectpath')
    if project_path == 'true':
        return jsonify({"project_path": "/path/to/project/folder"}), 200
    return jsonify({"file_path": "/path/to/file.blend"}), 200

@app.route('/add-item', methods=['POST'])
def add_item_endpoint():
    data = request.json
    name = data.get('name')
    quantity = data.get('quantity')
    if not name or not quantity:
        return jsonify({"error": "Name and quantity are required"}), 400
    add_item(name, quantity)
    return jsonify({"message": "Item added successfully!"}), 200

@app.route('/remove-item', methods=['POST'])
def remove_item_endpoint():
    data = request.json
    name = data.get('name')
    if not name:
        return jsonify({"error": "Name is required"}), 400
    remove_item(name)
    return jsonify({"message": "Item removed successfully!"}), 200

@app.route('/update-quantity', methods=['POST'])
def update_quantity_endpoint():
    data = request.json
    name = data.get('name')
    quantity = data.get('quantity')
    if not name or not quantity:
        return jsonify({"error": "Name and quantity are required"}), 400
    update_quantity(name, quantity)
    return jsonify({"message": "Quantity updated successfully!"}), 200

@app.route('/inventory', methods=['GET'])
def inventory():
    items = get_inventory()
    return jsonify({"inventory": items}), 200

if __name__ == "__main__":
    app.run(debug=True, port=8000)
