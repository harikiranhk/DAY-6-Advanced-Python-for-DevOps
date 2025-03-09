# 🔹 Challenge 2: Build a simple Flask API with an endpoint that returns system health (CPU/memory usage).

from flask import Flask, jsonify
import psutil

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def system_health():
    """Returns system health metrics (CPU & Memory usage)"""
    health_data = {
        "cpu_usage": psutil.cpu_percent(interval=1),
        "memory_usage": psutil.virtual_memory().percent
    }
    return jsonify(health_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)