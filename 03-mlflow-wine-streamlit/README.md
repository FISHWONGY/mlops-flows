# 🚀 mlflow-wine-streamlit

This is a simple example of how to use Streamlit for creating interactive web applications for wine quality analysis. It demonstrates the power of Streamlit along with Docker and Google Cloud Platform (GCP) for deploying machine learning models.

## Table of Contents

- [📖 Description](#description-)
- [🔑 Key Features](#key-features-)
- [🎯 Purpose](#purpose-)
- [🛠️ Usage Scenarios](#usage-scenarios-)
- [📋 Prerequisites](#prerequisites-)
- [📁 Folder Structure](#folder-structure-)
- [📦Installation](#installation-)
- [✨ Usage ](#usage-)



### 🔑 Key Features

- **Interactive Web UI**: Built with Streamlit for a responsive user experience.
- **Docker Integration**: Containerized application for easy deployment and scaling.
- **GCP Cloud Run Deployment**: Demonstrates how to deploy a containerized application to GCP Cloud Run.
- **Machine Learning Integration**: Incorporates MLflow for managing machine learning models.

### 🎯 Purpose

The purpose of this project is to provide a practical example of deploying a machine learning model as a web application. It aims to demonstrate:
- The ease of creating interactive web applications with Streamlit.
- Best practices for containerizing Python applications with Docker.
- The process of deploying applications to GCP Cloud Run.

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
│   ├── basic_auth.py
│   ├── gcp_secrets.py
│   ├── kevin.jpg
│   ├── main.py
│   ├── michael.jpg
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