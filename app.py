from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    client_ip = request.remote_addr
    connection_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{connection_time}] Client connected: IP address {client_ip}")
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
