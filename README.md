# mlops-flows

`mlops-flows` is a comprehensive suite of examples demonstrating the deployment of machine learning (ML) workflows on Google Cloud Platform (GCP). It covers the deployment of an MLflow server, the use of FastAPI for serving ML predictions, the creation of interactive web applications with Streamlit, and the integration of Vertex AI for model serving. Each component is designed to be scalable and secure, leveraging the power of GCP's Cloud Run service.

## Overview
![mlops-flows](https://github.com/FISHWONGY/mlops-flows/assets/59711659/80f7a6ed-10dd-4dd9-b80b-222492cfbf81)


## Table of Contents

- [🌟 Introduction](#-introduction)
- [📚 Repository Structure](#-repository-structure)
- [🔧 Technologies Used](#-technologies-used)
- [🚀 Quickstart](#-quickstart)
- [🔍 Detailed Guides](#-detailed-guides)
- [📋 Prerequisites](#-prerequisites)
- [🛠️ Installation](#-installation)
- [📝 Usage](#-usage)

## 🌟 Introduction

This repository is structured to provide a step-by-step approach to MLOps, from deploying an MLflow server to serving models and creating user interfaces. 

## 📚 Repository Structure

The `mlops-flows` project is organized into four main directories, each representing a key aspect of the MLOps lifecycle:

1. `01-mlflow-gcp-cloudrun`: Deployment of MLflow on GCP Cloud Run with secure access.
2. `02-mlflow-wine-pred-endpoint`: Serving a wine quality prediction model using FastAPI on Cloud Run.
3. `03-mlflow-wine-streamlit`: Interactive Streamlit web application for wine quality analysis deployed on Cloud Run.
4. `04-vertexai-ep-streamlit`: Streamlit web application using Vertex AI for serving ML models on Cloud Run.

Each directory contains a Dockerfile for containerization, a README with detailed instructions, and the necessary configuration files for deployment.

## 🔧 Technologies Used

- **MLflow**: Open-source platform for the machine learning lifecycle.
- **FastAPI**: Modern, fast web framework for building APIs with Python.
- **Streamlit**: Framework for creating beautiful, interactive web apps for machine learning and data science.
- **Docker**: Platform for developing, shipping, and running applications.
- **GCP Cloud Run**: Fully managed compute platform for deploying and scaling containerized applications quickly and securely.
- **Vertex AI**: Google Cloud's AI platform for training, hosting, and managing ML models.
- **Poetry**: Python dependency management and packaging tool.
- **Skaffold**: Command-line tool that facilitates continuous development for Kubernetes applications.

## 🚀 Quickstart

To get started with the `mlops-flows` project, ensure you have the prerequisites installed, then follow the installation steps for each component in the repository.

## 🔍 Detailed Guides

For detailed instructions on deploying and using each component, refer to the individual README files within each directory:

- [mlflow-gcp-cloudrun README](01-mlflow-gcp-cloudrun/README.md)
- [mlflow-wine-pred-endpoint README](02-mlflow-wine-pred-endpoint/README.md)
- [mlflow-wine-streamlit README](03-mlflow-wine-streamlit/README.md)
- [vertexai-ep-streamlit README](04-vertexai-ep-streamlit/README.md)

## 📋 Prerequisites

Before you begin, ensure you have the following prerequisites installed:

- Python 3.11+
- Docker
- GCP Account
- Poetry
- Skaffold (optional for development)

## 🛠️ Installation

To install the `mlops-flows` project, clone the repository and navigate into each project directory to install dependencies and deploy the services:

```bash
git clone https://github.com/fishwongy/mlops-flows.git
cd mlops-flows
```
## 📝 Usage

Each component within the `mlops-flows` project can be used independently. Below are the general steps to run each service after installation. For detailed usage instructions, please refer to the README within each component's directory.

### 01-mlflow-gcp-cloudrun

To start the MLflow server on Cloud Run:

```bash
cd 01-mlflow-gcp-cloudrun
# Follow the specific instructions in the component's README to deploy to Cloud Run
```

### 02-mlflow-wine-pred-endpoint

To deploy the wine quality prediction model as an API endpoint:

```bash
cd 02-mlflow-wine-pred-endpoint
# Follow the specific instructions in the component's README to deploy to Cloud Run
```

### 03-mlflow-wine-streamlit

To run the Streamlit web application for wine quality analysis:

```bash
cd 03-mlflow-wine-streamlit
# Follow the specific instructions in the component's README to deploy to Cloud Run
```

### 04-vertexai-ep-streamlit

To deploy the Streamlit web application using Vertex AI for model serving:

```bash
cd 04-vertexai-ep-streamlit
# Follow the specific instructions in the component's README to deploy to Cloud Run
```

Remember, each component may have its own set of environment variables, configurations, and deployment commands that need to be executed. The README files within each directory will provide the exact steps to get each service up and running.

For any common operations or commands that apply to all components, such as starting a local development server or running tests, you can include those instructions here as well.

### Common Operations

For example, if you have a common way to run all components locally using Poetry:

```bash
# To run any component locally, navigate to the component directory and use Poetry
cd <component-directory>
poetry install  # Install dependencies
poetry run 
```

Make sure to replace `<component-directory>` with the actual directory name of the component you wish to run.
