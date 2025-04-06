import os
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import barcode_scanner as bs
import api_call as api
import csv

app = Flask(__name__)
CORS(app)  # Aktiviert CORS für die gesamte App

UPLOAD_FOLDER = './uploads'  # Ordner, in dem Dateien gespeichert werden
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')  # Ensure you have an 'index.html' file.


@app.route('/api', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "Keine Datei hochgeladen"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "Leerer Dateiname"}), 400

    # Datei speichern
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    result = add_to_csv(file_path)
    os.remove(file_path)
    return jsonify(result), 200


def add_to_csv(file_path):
    barcode = bs.scan_barcode(file_path)
    data = api.get_product_info(barcode)
    data = string_to_values_list(data)
    # Pfad zur CSV-Datei
    csv_file = "list.csv"
    # Neue Zeile, die hinzugefügt werden soll
    new_row = [barcode, data[3], data[4], data[10], "20.12.2004"]
    # Die Datei im "append"-Modus öffnen
    with open(csv_file, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        # Neue Zeile schreiben
        writer.writerow(new_row)
    return new_row


def string_to_values_list(input_string):
    # Den String in Zeilen aufteilen
    lines = input_string.strip().split("\n")
    values = []
    for line in lines:
        # Leere Zeilen oder Trennstriche überspringen
        if not line.strip() or line.strip() == "---":
            continue
        # Schlüssel und Wert anhand des "=" trennen
        if "=" in line:
            key, value = line.split("=", 1)
            # Leere Werte als None speichern
            values.append(value.strip() if value.strip() else None)
    
    return values

if __name__ == '__main__':
    app.run(debug=True)