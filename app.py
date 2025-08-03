from flask import Flask
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
import os


app = Flask(__name__)
c = Counter('hit_counter', 'Hits to the root endpoint')

@app.route('/')
def home():
    c.inc()
    return os.getenv("MESSAGE", "Hello from trainee project!")

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

@app.route('/health')
def health():
    return "OK"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
