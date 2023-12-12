

---

# MNIST Classifier with Flask and Kubernetes Deployment

This project demonstrates a simple MNIST digit classifier using a Flask web service and a Kubernetes deployment.

## Setup and Installation

### 1. Docker Setup

Make sure you have Docker installed on your machine. Build the Docker image for the Flask app.

```bash
cd /path/to/your/project
docker build -t my-flask-app .
```

### 2. Kubernetes Setup

Ensure that you have `kubectl` configured to connect to your Kubernetes cluster.

Deploy the MySQL service:

```bash
kubectl apply -f mysql-service.yaml
```

Deploy the MySQL Deployment:

```bash
kubectl apply -f mysql-deployment.yaml
```

Deploy the Flask app:

```bash
kubectl apply -f app-deployment.yaml
```

### 3. Accessing the App

After deployment, wait for the services to be ready. Access the app using the following command:

```bash
kubectl get services my-flask-app-service
```

Note the external IP. Open a web browser and go to `http://<external-ip>`.

## Usage

1. Visit the web page and upload an image of an MNIST digit.
2. The model will predict the digit, and the result will be displayed on the webpage.

## Local Development

For local development, you can run the Flask app without Docker. Install the required Python packages:

```bash
pip install -r requirements.txt
```

Run the Flask app:

```bash
python app1.py
```

Access the app at `http://localhost:5000`.

## Directory Structure

- `app1.py`: Flask web service script.
- `Dockerfile`: Docker configuration for the Flask app.
- `app-deployment.yaml`: Kubernetes Deployment configuration for the Flask app.
- `mysql-deployment.yaml`: Kubernetes Deployment configuration for MySQL.
- `mysql-service.yaml`: Kubernetes Service configuration for MySQL.

## Issues and Contributions

Feel free to open issues for any problems or suggestions. Contributions are welcome!

---