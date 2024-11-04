# Particle Blueprints - Linux Container Tutorial

## Description

The **Linux Container Tutorial** guides users through packaging an application for Linux environments using container technology. This tutorial is designed to work across several Linux-based platforms, including the Tachyon (QCx6490-based), Raspberry Pi, and Nvidia Orin/Jetson boards, demonstrating a portable and reproducible deployment method.

## Table of Contents

*   [Introduction](#introduction)
*   [Prerequisites](#prerequisites)
*   [Getting Started](#getting-started)
*   [Running the Application](#running-the-application)
*   [API Usage](#api-usage)
*   [Project Structure](#project-structure)
*   [Contributing](#contributing)

## Introduction

Welcome to the **Linux Container Tutorial**! This tutorial provides a basic example of how to package a Python application into a container for deployment on Linux systems. It’s designed for compatibility with several boards, including Particle's Tachyon, Raspberry Pi, and Nvidia Jetson, making it easy to achieve portable, reproducible deployments.

## Prerequisites

For this tutorial, you’ll need:

*   **Podman:** A container engine compatible with Docker. [Install Podman](https://podman.io/getting-started/installation)
*   **Podman Compose:** A tool to manage multi-container applications using `podman-compose.yaml`. [Install Podman Compose](https://github.com/containers/podman-compose)

## Getting Started

### 1\. Clone the Repository

Clone or download this project to your local machine:

```
git clone https://github.com/particle-iot/linux-container-tutorial
cd linux-container-tutorial
```

## Running the Application

### Build and Run with Podman Compose

1.  **Build the Container Image:**
    
    ```
    podman-compose -f podman-compose.yaml build
    ```
    
2.  **Run the Container:**
    
    ```
    podman-compose -f podman-compose.yaml up
    ```
    
    The app will start and be accessible on [http://localhost:8000](http://localhost:8000).
    

### Stopping the Application

To stop the container, run:

```
podman-compose -f podman-compose.yaml down
```

## API Usage

The application exposes a simple `/add` endpoint, where you can provide two numbers as query parameters (`a` and `b`) to receive their sum.

### Example Request

To add 5 and 3, make a GET request to:

```
http://localhost:8000/add?a=5&b=3
```

### Example Response

```
{
  "result": 8.0
}
```

If either parameter is missing or invalid, the API will return an error message.

## Contributing

We welcome contributions to improve this project! If you'd like to suggest changes, please fork the repository and open a pull request.

### How to Contribute

1.  **Fork the repository.**
2.  **Make your changes in a new branch.**
3.  **Open a pull request with a detailed description of your changes.**
