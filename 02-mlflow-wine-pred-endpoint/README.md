# 🚀 mlflow-wine-pred-endpoint

This is a simple example of how to deploy prodcutionise a MLflow model to an API endpoint using FastAPI and GCP Cloud Run.

A detailed blog post on this project can be found [here](https://fishwongy.github.io/).

## Table of Contents

- [📖 Description](#description-)
- [🔑 Key Features](#key-features-)
- [🎯 Purpose](#purpose-)
- [🛠️ Usage Scenarios](#usage-scenarios-)
- [📋 Prerequisites](#prerequisites-)
- [📁 Folder Structure](#folder-structure-)
- [📦Installation](#installation-)
- [✨ Usage ](#usage-)

### 📖 Description

This project demonstrates the process of taking a machine learning model, specifically a wine quality prediction model built with MLflow, and deploying it as a scalable API service using FastAPI and Google Cloud Platform's Cloud Run service. The goal is to provide a practical example of how to bring a machine learning model into a production environment.

### 🔑 Key Features

- **MLflow Integration**: Utilizes MLflow for managing the machine learning lifecycle, including experimentation, reproducibility, and deployment.
- **FastAPI for API Development**: Leverages FastAPI to create a high-performance, asynchronous API service that serves our ML model predictions.
- **GCP Cloud Run Deployment**: Demonstrates how to containerize the FastAPI application and deploy it to GCP Cloud Run for scalable, serverless execution.

### 🎯 Purpose

The purpose of this project is to provide a clear and concise guide to deploying machine learning models in a production environment, emphasizing the use of modern tools and services like MLflow, FastAPI, and GCP Cloud Run. It aims to bridge the gap between machine learning development and operational deployment, enabling data scientists and developers to efficiently bring their models to users.

### 🛠️ Usage Scenarios

- **Wine Quality Prediction**: At its core, this project can be used to predict the quality of wine based on various physicochemical properties.
- **Educational Tool**: Serve as a reference or a hands-on project for learning about machine learning model deployment.
- **Template for ML Deployment**: Can be adapted or extended to deploy other types of machine learning models using the same technology stack.

### 📋 Prerequisites
- **Python 3.11+**: Required for both MLflow 2.14+
- **Docker**: For containerizing the application and deploying it to GCP Cloud Run.
- **Google Cloud Platform Account**: Necessary to access GCP Cloud Run and other GCP services.
- **MLflow**: For model training, logging, and packaging.
- **FastAPI**: For creating the web service that will serve predictions.


### 📁 Folder Structure
```md
.
├── Dockerfile
├── README.md
├── app
│   ├── basic_auth.py
│   ├── gcp_secrets.py
│   ├── helpers
│   │   ├── load_mlflow_models.py
│   │   └── models.py
│   ├── main.py
│   └── settings.py
├── deploy
│   └── production
│       └── service.yaml
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