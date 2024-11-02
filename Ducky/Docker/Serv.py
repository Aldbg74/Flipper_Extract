# server.py
# Alexis.D 2k24

from flask import Flask, request

app = Flask(__name__)

@app.route('/receive', methods=['POST'])
def receive_data():
    data = request.get_json()
    print("Data received:", data)
    return "Data received successfully", 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
