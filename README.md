# Kolam Pattern Generator

This is a Python-based program to generate traditional South Indian kolam (rangoli) designs. The project uses a Flask backend to serve a web page where you can generate beautiful, parameterized kolam patterns. The patterns are created as raster images (PNG) and can be used for art, research, or personal projects.

***

## 📁 Project Structure

To get started, make sure your project directory contains the following files:

* **`index.html`**: The main front-end web page.
* **`style.css`**: The stylesheet for `index.html`.
* **`requirements.txt`**: A list of all necessary Python libraries.
* **`app.py`**: The Flask application that serves the static page and handles the generation requests.
* **`kolam_project.py`**: The core script containing the logic for generating the kolam patterns.

***

## 💻 Setup and Installation

Follow these steps to set up the project and install the required dependencies.

1.  **Create a Virtual Environment**:
    Open your terminal (e.g., Git Bash, Command Prompt, or PowerShell) and navigate to your project folder. Run the following command to create a virtual environment:
    ```bash
    python -m venv venv
    ```

2.  **Activate the Environment**:
    Activate the virtual environment. This isolates the project's libraries from your system's global Python installation.
    * **On Windows**:
        ```bash
        venv\Scripts\activate
        ```
    * **On macOS/Linux**:
        ```bash
        source venv/bin/activate
        ```

3.  **Install Dependencies**:
    With the virtual environment active, upgrade `pip` and then install the libraries listed in `requirements.txt`:
    ```bash
    python -m pip install --upgrade pip
    python -m pip install -r requirements.txt
    ```
    * **Tip**: If you encounter issues with TensorFlow and do not have a GPU, you can try replacing `tensorflow` with `tensorflow-cpu` in your `requirements.txt` file before running the installation command.

***

## ▶️ How to Run the Application

Once your virtual environment is set up and all dependencies are installed, you can start the Flask web server.

1.  **Start the Server**:
    Make sure your virtual environment is active, and then run the `app.py` script:
    ```bash
    python app.py
    ```

2.  **Access the Generator**:
    You will see a message in your terminal indicating that the Flask server is running. Open your web browser and navigate to the following address:
    ```
    http://localhost:5000
    ```
    You should now be able to see the web page and generate your own kolam patterns.
