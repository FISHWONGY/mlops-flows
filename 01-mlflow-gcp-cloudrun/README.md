# 🚀 mlflow-gcp-cloudrun
This is a simple example of how to deploy MLflow on GCP Cloud Run.

A detailed blog post on this project can be found [here](https://fishwongy.github.io/).

## Table of Contents

- [📖 Description](#-Description)
- [🔑 Key Features](#-key-features-)
- [🎯 Purpose](#-purpose-)
- [🛠️ Usage Scenarios](#-usage-scenarios-)
- [📋 Prerequisites](#-prerequisites-)
- [📁 Folder Structure](#-folder-structure-)
- [📦Installation](#-installation-)
- [✨ Usage ](#-usage-)

## 📖 Description
The `mlflow-gcp-cloudrun` project demonstrates a streamlined approach to deploying MLflow, a popular open-source platform for managing the end-to-end machine learning lifecycle, on Google Cloud Platform's Cloud Run service. This setup allows for easy scaling and management of MLflow instances, providing a robust solution for teams looking to leverage MLflow's capabilities in a cloud-native environment.

### 🔑 Key Features

- **Simplified Deployment**: Utilizes GCP Cloud Run for hassle-free deployment and scaling of MLflow.
- **Secure Authentication**: Includes examples of secure authentication mechanisms for accessing MLflow's UI and API.
- **Containerized Application**: Leverages Docker for creating lightweight, portable, and consistent environments for MLflow.
- **Automated Workflows**: Integrates with Skaffold and Poetry for streamlined development, testing, and deployment workflows.

### 🎯 Purpose

This project aims to provide a template for machine learning teams and individuals looking to deploy MLflow in a cloud environment efficiently. By abstracting away the complexities of cloud deployment, it enables users to focus more on their core ML tasks rather than infrastructure management.

### 🛠️ Usage Scenarios

- **ML Experiment Tracking**: Easily track experiments, log parameters, and visualize results using MLflow deployed on Cloud Run.
- **Model Management**: Leverage MLflow for model versioning, staging, and production rollouts in a cloud environment.
- **Collaboration**: Share insights and collaborate with team members by providing a centralized MLflow server accessible from anywhere.

This project is ideal for data scientists, ML engineers, and DevOps professionals looking for a quick and reliable way to deploy MLflow on GCP Cloud Run.

### 📋 Prerequisites
- Python 3.11
- poetry
- skaffold

### 📁 Folder Structure
```md
.
├── Dockerfile
├── README.md
├── app
│   ├── __init__.py
│   ├── get_secret.py
│   └── mlflow_auth.py
├── deploy
│   └── production
│       └── service.yaml
├── entry-point.sh
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
```bash
poetry run -p prodcution
```
