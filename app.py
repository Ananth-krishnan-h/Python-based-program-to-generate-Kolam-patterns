# app.py
from flask import Flask, send_file, request, abort
import subprocess
import os
import time

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def home():
    # serve the static index.html in same folder
    return app.send_static_file('index.html')

@app.route('/generate', methods=['GET', 'POST'])
def generate():
    """
    Calls kolam_project.py in 'inference' mode (if supported).
    Blocks until the script finishes or timeout expires.
    Returns final_generated_kolam.png if present.
    """
    # try to run generator with an '--inference' flag; fallback to plain call
    cmd = ['python', 'kolam_project.py', '--inference']
    try:
        proc = subprocess.run(cmd, check=False, timeout=7200)  # 5 min timeout
    except subprocess.TimeoutExpired:
        return ("Generation timed out", 504)

    out_path = 'final_generated_kolam.png'
    if os.path.exists(out_path):
        return send_file(out_path, mimetype='image/png')
    else:
        # If the file wasn't created, try running without --inference
        try:
            subprocess.run(['python', 'kolam_project.py'], check=False, timeout=300)
        except subprocess.TimeoutExpired:
            return ("Generation timed out", 504)

        if os.path.exists(out_path):
            return send_file(out_path, mimetype='image/png')
        return ("final_generated_kolam.png not found after running generator.", 500)

if __name__ == '__main__':
    # change host/port if needed
    app.run(host='0.0.0.0', port=5000, debug=True)
