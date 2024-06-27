# Flask API Project

This project demonstrates how to create a Flask API using Python 3.x, Docker Desktop, and Visual Studio Code, based on a course from Udemy.

## Prerequisites

- **Python 3.x**: Ensure you have Python 3.x installed.
- **Docker Desktop**: Install Docker Desktop for container management.
- **Visual Studio Code (VSCode)**: Use VSCode as your code editor.

## Setup Instructions

### 1. Install Python

#### Download and Install Python

1. Visit the [official Python website](https://www.python.org/downloads/).
2. Download the latest Python 3.x version for your operating system.
3. Run the installer and follow the on-screen instructions.
4. Ensure you check the box to add Python to your PATH during installation.

### 2. Install Visual Studio Code

#### Download and Install VSCode

1. Visit the [official VSCode website](https://code.visualstudio.com/).
2. Download the installer for your operating system.
3. Run the installer and follow the on-screen instructions.

### 3. Configure Visual Studio Code UI

1. Open Visual Studio Code.
2. Install the following recommended extensions:
   - Python
   - Docker
   - Remote - Containers
3. Configure your VSCode settings for Python development by setting up the Python interpreter and other preferences.

### 4. Create a New Project in Visual Studio Code

1. Open Visual Studio Code.
2. Open the terminal within VSCode (`View > Terminal`).
3. Navigate to your project directory:
   ```sh
   cd path/to/your/project
   ```
4. Create a new Python virtual environment:
   ```sh
   python -m venv venv
   ```
5. Activate the virtual environment:
   - On Windows:
     ```sh
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```sh
     source venv/bin/activate
     ```

## Using Docker

1. Ensure Docker Desktop is running.
2. Use the provided `docker-compose.yml` file to set up your environment:
   ```sh
   docker-compose up
   ```

## Project Structure

- `docker-compose.yml`: Defines the Docker services for the project.
- `app/`: Contains your Flask application code.
- `requirements.txt`: List of Python dependencies.

## Important Notes

- Always update your `requirements.txt` file whenever you create new apps or install new dependencies.
- Understand the basics of virtual environments, including isolated environments and preparing a virtual environment.

## Virtual Environments

### Isolated Environments

Virtual environments allow you to manage dependencies for your projects in isolation, ensuring that each project has its own set of dependencies.

### Preparing a Virtual Environment

#### Creating and Activating the Virtual Environment

1. Create a virtual environment:
   ```sh
   python -m venv venv
   ```
2. Activate the virtual environment:
   - On Windows:
     ```sh
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```sh
     source venv/bin/activate
     ```

---

This README provides comprehensive instructions for setting up the environment and tools needed for your Flask API project.
