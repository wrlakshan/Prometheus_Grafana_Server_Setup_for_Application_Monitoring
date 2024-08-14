
# Project Setup Guide

## Python and Virtual Environment Setup

### 1. Install `virtualenv`
Use `pip` to install the `virtualenv` package:
```bash
pip install virtualenv
```

### 2. Check Python Version
Verify your Python version with:
```bash
python3 --version
```

### 3. Create a Virtual Environment
Create a new virtual environment named `env`:
```bash
python3 -m venv env
```

### 4. Activate the Virtual Environment
Activate the virtual environment:
```bash
source env/bin/activate
```

### 5. Export Installed Packages
Export a list of all installed packages to `requirements.txt`:
```bash
pip freeze > requirements.txt
```

### 6. Install Packages from `requirements.txt`
Install all packages listed in `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 7. Deactivate the Virtual Environment
When you are done, deactivate the virtual environment:
```bash
deactivate
```

## Docker and Service Monitoring Setup

### 8. Build and Run Docker Containers
Build and start Docker containers:
```bash
docker-compose up --build
docker compose up --build
```

### 9. Run Docker Containers in Detached Mode
Run containers in the background:
```bash
docker-compose up -d
docker compose up --build
```

## Accessing Applications and Tools

### 10. Flask Application
Access the Flask application at:
[http://localhost:8000](http://localhost:8000)

### 11. Prometheus Monitoring Tool
Access Prometheus at:
[http://localhost:9090](http://localhost:9090)

### 12. Grafana
Login to Grafana at:
[http://localhost:3000](http://localhost:3000)
Default credentials are `admin` for both username and password.


### 9. Reestart the running Docker Container
Restart containers to effect the chnges:
```bash
docker-compose restart grafana
```
