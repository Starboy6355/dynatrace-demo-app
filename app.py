# app.py
# Simple Flask app designed for Dynatrace monitoring/troubleshooting demos

from flask import Flask
import logging

app = Flask(__name__)

# Configure logger to write logs into a file (for log monitoring)
logging.basicConfig(filename="app.log", level=logging.INFO,
                    format="%(asctime)s %(levelname)s: %(message)s")

@app.route("/")
def home():
    app.logger.info("Visited home endpoint.")
    return "Hello from Dynatrace Demo App!"

@app.route("/error")
def error():
    app.logger.error("Intentional error triggered!")
    # Simulate an error that will show up in Dynatrace/traces
    raise Exception("This is a test exception for troubleshooting!")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
