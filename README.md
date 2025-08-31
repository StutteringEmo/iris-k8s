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

-----

# Build and run locally with Docker
## Step-by-Step Setup (PowerShell Example)

### Go to project folder
```bash
cd iris_k8s
```

### Build Docker image
```bash
docker build -t iris-model:1.0 .
```

### Run container locally
```bash
docker run -p 8000:8000 iris-model:1.0
```

- Open http://localhost:8000 in your browser.

---

## Installing Minikube (Windows Example)
If you don’t already have Minikube installed, follow these steps:

1. Go to the official installation guide: https://minikube.sigs.k8s.io/docs/start/?arch=%2Fwindows%2Fx86-64%2Fstable%2F.exe+download
2. Choose your operating system. For Windows (x86-64), you can follow the PowerShell method:
```bash
New-Item -Path 'c:\' -Name 'minikube' -ItemType Directory -Force
$ProgressPreference = 'SilentlyContinue'; Invoke-WebRequest -OutFile 'c:\minikube\minikube.exe' -Uri 'https://github.com/kubernetes/minikube/releases/latest/download/minikube-windows-amd64.exe'
```
3. Then add Minikube to PATH (run PowerShell as Administrator):
```bash
$oldPath = [Environment]::GetEnvironmentVariable('Path', [EnvironmentVariableTarget]::Machine)
if ($oldPath.Split(';') -notcontains 'C:\minikube') {
    [Environment]::SetEnvironmentVariable('Path', "$oldPath;C:\minikube", [EnvironmentVariableTarget]::Machine)
}
```
-- (Reopen PowerShell after this step so minikube is recognized)

---

## Running on Kubernetes (Minikube)
1. Start Minikube
```bash
minikube start --driver=docker
```
2. Load Docker image into Minikube
```bash
minikube image load iris-model:1.0
```
3. Apply Kubernetes manifests
```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```
4. Access the service
```bash
minikube service iris-svc --url
```

-----

## Results

### Web App Prediction
<img width="478" height="313" alt="image" src="https://github.com/user-attachments/assets/0b23795b-f033-43bf-8554-aca520246cf4" />


### Kubernetes Pods
<img width="975" height="141" alt="image" src="https://github.com/user-attachments/assets/17431e3f-9b0a-4d5a-bdc2-b2be9c2dcc9c" />


### Scaling Replicas
<img width="975" height="157" alt="image" src="https://github.com/user-attachments/assets/e110eb3f-b473-4a37-b1e3-f55321f9ec9f" />

