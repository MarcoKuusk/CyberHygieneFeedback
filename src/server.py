from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import json

app = Flask(__name__, static_folder='webinterface')
CORS(app)  # Enable CORS for all routes

# Directory to save assessment data
DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data'))

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def serve_static_files(path):
    return send_from_directory(app.static_folder, path)

@app.route('/saveAssessmentData/<filename>', methods=['POST'])
def save_assessment_data(filename):
    try:
        # Ensure the filename ends with .json
        if not filename.endswith('.json'):
            return jsonify({"error": "Invalid file type"}), 400

        # Get the JSON data from the request
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400

        # Save the data to the specified file
        file_path = os.path.join(DATA_DIR, filename)
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

        return jsonify({"message": f"Data saved to {filename}"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)