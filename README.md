## **Blender Plugin with REST API Integration**

The **Blender Plugin with REST API Integration** project connects a **Blender plugin** to a **Flask server** via REST API, enabling users to manipulate object transformations (position, rotation, scale) and manage an inventory system. The data is stored in an **SQLite database** for efficient retrieval and management.

This app is perfect for professionals, 3D artists, developers, or anyone who works with Blender and needs to automate or manage object transforms and inventory data seamlessly.

### **Features**

- **Seamless Integration**: Manage Blender objects' transformations (position, rotation, scale) effortlessly.
- **REST API-Powered**: Interact with the Flask server using endpoints like `/transform`, `/translation`, `/rotation`, and `/scale`.
- **Inventory Management**: Add, remove, and update items with a dedicated **inventory UI** built with **PyQt5**.
- **User-Friendly Interface**: Simple UI for sending object data and managing inventory.
- **Real-Time Data Interaction**: Instant response for object transformations and inventory management.

This project simplifies data handling for Blender users and provides a seamless workflow for 3D model management, transformation tracking, and inventory systems.

---

### **How to get Started?**

#### **1. Clone the GitHub repository**
```bash
git clone https://github.com/PramodSeeram/BlenderPlugin-with-REST-API-Integration.git
```

#### **2. Install the required dependencies**

Create a virtual environment and install the necessary libraries:
```bash
pip install -r requirements.txt
```

#### **3. Run the App**

##### **Flask Server**
1. First, run the Flask server to handle the requests:
```bash
python server.py
```
This will start the server at **http://127.0.0.1:8000**.

##### **Blender Plugin (UI)**
1. Open **Blender**, navigate to the **Scripting tab**, and run the **`blender_ui.py`** script. 
2. The UI will appear in the **3D Viewport** under the **Tools** tab.

##### **Inventory UI (PyQt5)**
1. Install **PyQt5**:
```bash
pip install PyQt5
```
2. Run the **inventory UI**:
```bash
python inventory_ui.py
```
3. Use the PyQt application to interact with the inventory and perform CRUD operations.

---

### **Repository Link**
- [BlenderPlugin-with-REST-API-Integration GitHub](https://github.com/PramodSeeram/BlenderPlugin-with-REST-API-Integration.git)
