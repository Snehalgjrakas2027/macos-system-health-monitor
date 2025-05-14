import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, Response
from monitor.system_metrics import get_metrics

app = Flask(__name__)

@app.route("/metrics")
def metrics():
    data = get_metrics()
    output = ""
    for key, value in data.items():
        output += f"{key} {value}\n"
    return Response(output, mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
