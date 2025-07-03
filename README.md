# Flask Note App on Kubernetes (Minikube)

This is a simple Flask-based note-taking app deployed using Docker and Kubernetes via Minikube. It allows users to submit and view text notes.

## 📦 Project Structure

├── Dockerfile
├── app
│ ├── app.py
│ └── notes.txt
├── k8s
│ ├── deployment.yaml
│ ├── service.yaml
│ └── volume.yaml


## 🚀 Features

- Submit notes via a web form
- View saved notes
- Persistent storage using hostPath
- Kubernetes deployment with NodePort service

## 🐳 Docker

The app is containerized using a `Dockerfile` that:

- Uses `python:3.10-slim`
- Installs Flask
- Copies the `app` folder
- Runs `app.py` on port 5000

## ☸️ Kubernetes

Three YAML files are used:

- `deployment.yaml`: Deploys the pod and mounts `/tmp/notes` to `/app/notes.txt`
- `service.yaml`: Exposes the app via NodePort
- `volume.yaml`: Ensures the host directory is available

## 🧪 How to Run (Locally with Minikube)

```bash
# 1. Start Minikube
minikube start

# 2. Ensure /tmp/notes exists inside the Minikube VM
minikube ssh
sudo mkdir -p /tmp/notes
sudo touch /tmp/notes/notes.txt
exit

# 3. Build Docker image inside Minikube
eval $(minikube docker-env)
docker build -t note-app:latest .

# 4. Apply Kubernetes configs
kubectl apply -f k8s/volume.yaml
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml

# 5. Port forward to view the app
kubectl port-forward svc/note-app-service 5000:5000

# 6. Visit the app
open http://localhost:5000

