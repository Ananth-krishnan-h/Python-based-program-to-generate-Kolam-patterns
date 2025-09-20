# Python-based-program-to-generate-Kolam-patterns.
A Python-based generator for traditional South Indian kolam (rangoli) designs. It creates beautiful, parameterized kolam patterns as vector (SVG) and raster (PNG) output, supports animation/export, a simple CLI, and a scriptable API for research, art, or your SIH project.


1) Files you should have in one folder

  Place these files in the same directory:
  index.html
  style.css
  requirements.txt
  app.py ← use the version below (serves the static page + /generate)
  kolam_project.py ← your generator script (should produce final_generated_kolam.png)

2) Prepare a Python virtual environment & install deps

  Open Git Bash (or PowerShell/CMD) and cd into the project folder.

  Create and activate a venv:
  Windows CMD:
  python -m venv venv
  venv\Scripts\activate.bat

  Upgrade pip and install requirements:
  python -m pip install --upgrade pip
  python -m pip install -r requirements.txt

  Tip: If you don't have a GPU or TF wheel issues, try tensorflow-cpu instead of tensorflow in requirements.txt.

5) Start the Flask backend

  With your venv active and dependencies installed:

  python app.py

  You should see Flask launch and bind to port 5000. Example console line:

   * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
