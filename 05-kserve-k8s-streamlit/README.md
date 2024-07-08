# kserve-k8s-streamlit

This is a simple example of how to use Streamlit for creating interactive web applications for productionise ML models using Vertex AI Endpoint serving and GCP CLoud Run.

## Table of Contents

- [📖 Description](#description-)
- [🔑 Key Features](#key-features-)
- [🎯 Purpose](#purpose-)
- [🛠️ Usage Scenarios](#usage-scenarios-)
- [📋 Prerequisites](#prerequisites-)
- [📁 Folder Structure](#folder-structure-)
- [📦Installation](#installation-)
- [✨ Deployment ](#deployment-)


### 📖 Description

This project provides an example for deploying machine learning models as web applications using Streamlit, Docker, and Google Cloud Platform (GCP) services, specifically Vertex AI and Cloud Run. It includes a basic Streamlit app that can be easily extended to include custom machine learning models and interfaces.

### 🔑 Key Features

- **Streamlit Integration**: Easy to create and customize interactive web UIs for ML models.
- **Docker Support**: Containerize the Streamlit app for easy deployment and scaling.
- **GCP Deployment**: Instructions and configuration for deploying to GCP Cloud Run, leveraging the managed infrastructure for auto-scaling and high availability.
- **Kubeflow Kserve**: Demonstrates how to serve ML models using KServe, allowing for easy integration into the Streamlit app.
- **Poetry for Dependency Management**: Utilizes Poetry to manage project dependencies, making it easy to replicate the environment.

### 🎯 Purpose

The purpose of this project is to provide a practical example of deploying a machine learning model as a web application. It aims to demonstrate:
- The ease of creating interactive web applications with Streamlit.
- Best practices for containerizing Python applications with Docker.
- The process of deploying applications to GKE.

### 🛠️ Usage Scenarios

- **Prototype Development**: As a starting point for developing more complex wine quality prediction systems.
- **Cloud Deployment Demonstration**: For learning how to deploy applications to the cloud using GCP.


### 📋 Prerequisites

- **Python 3.11+**: For Streamlit.
- **Docker**: For containerizing the application and deploying it to GCP Cloud Run.
- **Google Cloud Platform Account**: Necessary to access GCP Cloud Run and other GCP services.
- **Poetry**: For managing Python package dependencies.
- **Streamlit**: For creating the web interface.


### 📁 Folder Structure
```md
.
├── Dockerfile
├── README.md
├── app
│   ├── basic_auth.py
│   ├── gcp_secrets.py
│   ├── main.py
│   └── settings.py
├── deploy
│   ├── common
│   │   ├── config.yaml
│   │   ├── deployment.yaml
│   │   ├── kustomization.yaml
│   │   ├── service.yaml
│   │   └── serviceaccount.yaml
│   └── production
│       └── kustomization.yaml
├── deploy.sh
├── poetry.lock
├── pyproject.toml
└── skaffold.yaml

```

### 📦 Installation 
1. Clone the repository
```bash
git clone
```

2. Navigate into the project directory:
```bash
cd <project-name>
```

3. Install dependencies using Poetry:
```bash
poetry install
```

### ✨ Usage
For deployment, in order to pull the image from the Google Container Registry, you need to create/ make sure your node pool has the scopes `cloud-platform` and `storage-full`
You can do this by running the following command:

```bash
gcloud container node-pools create default-node-pool-new \
    --cluster=kubeflow  \
    --zone=us-central1-c \
    --scopes=cloud-platform,storage-full \        
    --num-nodes=2

```

Create a json key for accessing the GCP Artifacts Registry
```bash
gcloud iam service-accounts keys create key.json \                               
  --iam-account=svc@gcp-prj-id-123.iam.gserviceaccount.com
````

```bash
kubectl create secret docker-registry gar-json-key \                             
  --docker-server=us-central1-docker.pkg.dev \
  --docker-username=_json_key \
  --docker-password="$(cat key.json)" \
  --docker-email=user@email.com
```

Reference the secret in the `deployment.yaml` file as shown below:
```yaml
spec:
  serviceAccountName: default-editor
  imagePullSecrets:
  - name: gar-json-key
```

Also in `serviceaccount.yaml` file, 
```yaml
imagePullSecrets:
- name: gar-json-key
```

Ensure the service account has the role artifactregistry.reader
```bash
gcloud projects add-iam-policy-binding gcp-prj-id-123 \
    --member "serviceAccount:svc@gcp-prj-id-123.iam.gserviceaccount.com" \
    --role "roles/artifactregistry.reader"
```

```bash
gcloud artifacts repositories add-iam-policy-binding mlflow-gcp \                 
    --location=us-central1 \
    --member=serviceAccount:svc@gcp-prj-id-123.iam.gserviceaccount.com \
    --role="roles/artifactregistry.reader"
```

In the `deployment/common/deployment.yaml` file, ensure to specify using the node pool with the scopes `cloud-platform` and `storage-full` as shown below:

```yaml
nodeSelector:
  cloud.google.com/gke-nodepool: default-node-pool-new
```

To deply the application, run the following command:
```bash
poetry run -p prodcution
```
