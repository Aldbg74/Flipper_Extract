from flask import Flask, request

app = Flask(__name__)

@app.route('/receive', methods=['POST'])
def receive_data():
    data = request.json
    if data:
        print(f"Data received: {data}")
        return {"status": "success", "message": "Data received"}, 200
    else:
        return {"status": "error", "message": "No data received"}, 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
