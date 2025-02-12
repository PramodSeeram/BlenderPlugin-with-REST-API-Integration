import sys
import sqlite3
import requests
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QLabel

DATABASE = 'inventory.db'
SERVER_URL = 'http://127.0.0.1:8000'

class ServerWorker(QThread):
    result = pyqtSignal(str)

    def __init__(self, endpoint, data):
        super().__init__()
        self.endpoint = endpoint
        self.data = data
        self._is_running = True

    def run(self):
        try:
            response = requests.post(f'{SERVER_URL}{self.endpoint}', json=self.data)
            if response.status_code == 200:
                self.result.emit(response.json().get('message', 'Success'))
            else:
                self.result.emit(f"Error: {response.json().get('error', 'Unknown error')}")
        except Exception as e:
            self.result.emit(f"Failed to connect to server: {str(e)}")

    def stop(self):
        self._is_running = False
        self.quit()
        self.wait()

class InventoryApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Inventory Management")
        self.setGeometry(100, 100, 600, 400)

        self.table = QTableWidget(self)
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(['Item Name', 'Quantity'])
        self.load_inventory()

        self.name_input = QLineEdit(self)
        self.quantity_input = QLineEdit(self)

        self.add_button = QPushButton("Add Item", self)
        self.remove_button = QPushButton("Remove Item", self)
        self.update_button = QPushButton("Update Quantity", self)
        self.purchase_button = QPushButton("Purchase Item", self)
        self.return_button = QPushButton("Return Item", self)

        self.add_button.clicked.connect(self.add_item)
        self.remove_button.clicked.connect(self.remove_item)
        self.update_button.clicked.connect(self.update_item)
        self.purchase_button.clicked.connect(self.purchase_item)
        self.return_button.clicked.connect(self.return_item)

        layout = QVBoxLayout()
        layout.addWidget(self.table)

        input_layout = QHBoxLayout()
        input_layout.addWidget(QLabel("Item Name:"))
        input_layout.addWidget(self.name_input)
        input_layout.addWidget(QLabel("Quantity:"))
        input_layout.addWidget(self.quantity_input)

        layout.addLayout(input_layout)
        layout.addWidget(self.add_button)
        layout.addWidget(self.remove_button)
        layout.addWidget(self.update_button)
        layout.addWidget(self.purchase_button)
        layout.addWidget(self.return_button)

        self.setLayout(layout)

    def load_inventory(self):
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        c.execute('SELECT name, quantity FROM items')
        items = c.fetchall()
        conn.close()

        self.table.setRowCount(len(items))

        for row, (name, quantity) in enumerate(items):
            self.table.setItem(row, 0, QTableWidgetItem(name))
            self.table.setItem(row, 1, QTableWidgetItem(str(quantity)))

    def add_item(self):
        name = self.name_input.text()
        quantity = self.quantity_input.text()

        if not name or not quantity.isdigit():
            return

        data = {'name': name, 'quantity': int(quantity)}
        self.send_request('/add-item', data)

    def remove_item(self):
        name = self.name_input.text()

        if not name:
            return

        data = {'name': name}
        self.send_request('/remove-item', data)

    def update_item(self):
        name = self.name_input.text()
        quantity = self.quantity_input.text()

        if not name or not quantity.isdigit():
            return

        data = {'name': name, 'quantity': int(quantity)}
        self.send_request('/update-quantity', data)

    def purchase_item(self):
        name = self.name_input.text()

        if not name:
            return

        data = {'name': name, 'quantity': -1}
        self.send_request('/update-quantity', data)

    def return_item(self):
        name = self.name_input.text()

        if not name:
            return

        data = {'name': name, 'quantity': 1}
        self.send_request('/update-quantity', data)

    def send_request(self, endpoint, data):
        self.worker = ServerWorker(endpoint, data)
        self.worker.result.connect(self.handle_server_response)
        self.worker.start()

    def handle_server_response(self, response):
        print(response)
        self.load_inventory()

    def closeEvent(self, event):
        """Ensure the thread is properly stopped when closing the application."""
        if hasattr(self, 'worker'):
            self.worker.stop()  # Stop the thread gracefully
        event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = InventoryApp()
    window.show()
    sys.exit(app.exec_())
