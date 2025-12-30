Lightweight Ransomware Prevention Web-Based App Using LightGBM

Project Overview

This project implements a lightweight, web-based application designed for static analysis and detection of ransomware using a machine learning model, LightGBM. The primary goal is to provide an accessible, low-resource defense mechanism for Small and Medium-sized Enterprises (SMEs) and individual users who may lack high-spec hardware or extensive cybersecurity expertise.

The application performs static analysis of Portable Executable (PE) files (like .exe or .dll files) by extracting header features. It then uses a pre-trained LightGBM classification model to quickly determine if the file is likely benign or malicious (ransomware).

Key Features

- Lightweight Design: Optimized for low-spec hardware (CPU-only, ≤4GB RAM requirement).

- Static Analysis: Analyzes PE headers without executing the file, ensuring fast and safe scanning.

- Web-Based Interface: Simple, non-technical user interface (UI) built with Bootstrap for easy file upload and clear, color-coded results.

- High Efficiency: Utilizes LightGBM for fast prediction times (target: <10 ms).

- Privacy Focused: No file storage after scanning (session-based processing).

Methodology

The project followed an Agile Methodology (Plan, Design, Develop, Test, Deploy, Review).

Technology Stack

- Backend Framework: Python (Flask)

- Machine Learning: LightGBM (Gradient Boosting Framework)

- Feature Extraction: pefile library (for static PE header analysis)

- Frontend: HTML/CSS (Bootstrap 5)

- Serialization: joblib (for model persistence)

Installation and Setup

Prerequisites

1. Python 3.x

2. pip (Python package installer)

3. Virtual environment (recommended)

Steps

1. Clone the Repository:

git clone [YOUR_REPO_URL]
cd ransomwareDetector

1. Create and Activate Virtual Environment:

python3 -m venv venv
source venv/bin/activate  # On Linux/macOS
# venv\Scripts\activate   # On Windows

1. Install Dependencies:

pip install flask lightgbm pandas joblib pefile

1. Model and Feature Files:
Ensure the following files are present in your project directory:

- model.joblib (or lightgbm_model.txt if using LightGBM's native save format): The trained classification model.

- app.py: The Flask application script.

- feature_extractor.py: The script containing the extract_features function.

- templates/index.html: The Bootstrap frontend file.

1. Run the Flask Application:

python3 app.py

The application will start running locally, typically accessible at http://127.0.0.1:5000.

Usage

1. Open your web browser and navigate to http://127.0.0.1:5000.

2. Use the file upload form (Bootstrap UI) to select a Portable Executable (.exe, .dll) file.

3. Click "Scan File."

4. The system will extract the PE header features, pass them to the LightGBM model, and display the result:

- Green Alert: File is benign (prediction = 1).

- Red Alert: File is malicious/ransomware (prediction = 0).

Model Training and Data

Dataset

The model was trained offline using the Kaggle PE Header ransomware dataset (~2,157 samples).

- Labeling: Binary classification where Benign = 1 and Malicious = 0.

- Features: Static PE header fields (e.g., Machine, ExportSize, ResourceSize, NumberOfSections, DllCharacteristics, etc.).

Feature Extraction Consistency

A critical component is the feature_extractor.py script, which ensures that the features extracted from a file at runtime are exactly the same type and order as those used during the original training process. This guarantees accurate inference by the LightGBM model.

The features used are strictly static PE attributes, avoiding complex metrics like entropy calculation or import table analysis for speed and resource efficiency.

Core Components

app.py (Flask Backend)

This file manages the web server and API endpoints:

- / (GET): Renders the index.html frontend template.

- /predict (POST):

- Handles file upload.

- Saves the uploaded file temporarily.

- Calls feature_extractor.extract_features() on the saved file.

- Loads the model.joblib once at startup.

- Performs prediction using the LightGBM model.

- Returns the result as a JSON response to the frontend.

feature_extractor.py

This module uses the pefile library to statically read an executable file and generate the required feature vector for the LightGBM model.

templates/index.html (Bootstrap Frontend)

Provides the user interface for file upload and displays the prediction result clearly (Green for safe, Red for malicious).

This project was developed as a final-year undergraduate thesis, focusing on the practical application of lightweight machine learning in cybersecurity.
