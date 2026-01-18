from flask import Flask, request, render_template, redirect, url_for
import pandas as pd
import os
from feature_extractor import extract_features
import joblib
import uuid

app = Flask(__name__)

MODEL_PATH = "model.joblib"
model = joblib.load(MODEL_PATH)

FEATURES = [
    'Machine','DebugSize','DebugRVA','MajorImageVersion','MajorOSVersion',
    'ExportRVA','ExportSize','IatVRA','MajorLinkerVersion','MinorLinkerVersion',
    'NumberOfSections','SizeOfStackReserve','DllCharacteristics','ResourceSize','BitcoinAddresses'
]

RESULTS_STORE = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'files' not in request.files:
        return "No files provided", 400

    files = request.files.getlist('files')
    session_id = str(uuid.uuid4())
    RESULTS_STORE[session_id] = []

    for upload in files:
        temp_path = os.path.join("/tmp", upload.filename)
        upload.save(temp_path)
        features = extract_features(temp_path)
        df = pd.DataFrame([features], columns=FEATURES).astype(float)

        pred_label = int(model.predict(df)[0])
        pred_prob = float(model.predict_proba(df)[0][pred_label]) * 100

        RESULTS_STORE[session_id].append({
            "filename": upload.filename,
            "features": features,
            "prediction": pred_label,  # 1=Benign, 0=Malicious
            "probability": round(pred_prob, 2)
        })
        os.remove(temp_path)

    return redirect(url_for('results', session_id=session_id))

@app.route('/results/<session_id>')
def results(session_id):
    if session_id not in RESULTS_STORE:
        return "Session not found", 404
    return render_template('results.html', results=RESULTS_STORE[session_id], session_id=session_id)

if __name__ == "__main__":
    app.run(debug=True)

