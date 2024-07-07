# vertexai-ep-streamlit

This is a simple example of how to use Streamlit for creating interactive web applications for productionise ML models using Vertex AI Endpoint serving and GCP CLoud Run.

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

This project provides an example for deploying machine learning models as web applications using Streamlit, Docker, and Google Cloud Platform (GCP) services, specifically Vertex AI and Cloud Run. It includes a basic Streamlit app that can be easily extended to include custom machine learning models and interfaces.

### 🔑 Key Features

- **Streamlit Integration**: Easy to create and customize interactive web UIs for ML models.
- **Docker Support**: Containerize the Streamlit app for easy deployment and scaling.
- **GCP Deployment**: Instructions and configuration for deploying to GCP Cloud Run, leveraging the managed infrastructure for auto-scaling and high availability.
- **Vertex AI Endpoint Serving**: Demonstrates how to serve ML models using Vertex AI, allowing for easy integration into the Streamlit app.
- **Poetry for Dependency Management**: Utilizes Poetry to manage project dependencies, making it easy to replicate the environment.

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
│   ├── common_func.py
│   ├── gcp_secrets.py
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