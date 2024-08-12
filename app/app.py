from flask import Flask
from prometheus_client import make_wsgi_app, Counter, Gauge
from werkzeug.middleware.dispatcher import DispatcherMiddleware
import psutil

app = Flask(__name__)

# Add Prometheus WSGI middleware to route /metrics requests
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app()
})

# Define metrics
REQUEST_COUNT = Counter('request_count', 'App Request Count')
CPU_USAGE = Gauge('cpu_usage', 'CPU Usage Percentage')
MEMORY_USAGE = Gauge('memory_usage', 'Memory Usage Percentage')
DISK_USAGE = Gauge('disk_usage', 'Disk Usage Percentage')

def fetch_system_metrics():
    """Fetch and update system metrics."""
    CPU_USAGE.set(psutil.cpu_percent(interval=1))
    MEMORY_USAGE.set(psutil.virtual_memory().percent)
    DISK_USAGE.set(psutil.disk_usage('/').percent)

@app.route('/')
def hello():
    # Increment the request counter
    REQUEST_COUNT.inc()
    # Update system metrics
    fetch_system_metrics()
    return "Hello, World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
