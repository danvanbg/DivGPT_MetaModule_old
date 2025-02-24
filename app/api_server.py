# api_server.py
from flask import Flask, request, jsonify

app = Flask(__name__)

# Примерни данни
logs = []

@app.route('/get_new_data', methods=['GET'])
def get_new_data():
    return jsonify(logs), 200

@app.route('/add_log', methods=['POST'])
def add_log():
    log_entry = request.json
    logs.append(log_entry)
    return jsonify({"message": "Log added successfully!"}), 200

@app.route('/process_data', methods=['POST'])
def process_data():
    data = request.json.get('data', {})
    # Тук може да добавите логика за обработка на данни и взаимодействие с ChatGPT
    return jsonify({"message": "Data processed successfully!", "processed_data": data}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
