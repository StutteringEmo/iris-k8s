# Iris Flower Prediction with Kubernetes

This project deploys a machine learning model (Iris dataset classifier) using:
- Flask for the web interface
- Docker for containerization
- Kubernetes (Minikube) for deployment and scaling

## Features
- Input flower measurements via a web form
- Model predicts the Iris species (Setosa, Versicolor, Virginica)
- Scalable deployment with Kubernetes replicas

## Files
- `app.py` → Flask app
- `Dockerfile` → container build instructions
- `requirements.txt` → Python dependencies
- `file_iris.pkl` → trained ML model
- `templates/` → HTML frontend
- `k8s/` → Kubernetes deployment & service YAMLs

## Running Locally
```bash
docker build -t iris-model:1.0 .
docker run -p 8000:8000 iris-model:1.0
```

## Running on Kubernetes (Minikube)
```bash
minikube start --driver=docker
minikube image load iris-model:1.0
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
minikube service iris-svc --url
```

## Results

### Web App Prediction
<img width="478" height="313" alt="image" src="https://github.com/user-attachments/assets/0b23795b-f033-43bf-8554-aca520246cf4" />


### Kubernetes Pods
<img width="975" height="141" alt="image" src="https://github.com/user-attachments/assets/17431e3f-9b0a-4d5a-bdc2-b2be9c2dcc9c" />


### Scaling Replicas
<img width="975" height="157" alt="image" src="https://github.com/user-attachments/assets/e110eb3f-b473-4a37-b1e3-f55321f9ec9f" />

