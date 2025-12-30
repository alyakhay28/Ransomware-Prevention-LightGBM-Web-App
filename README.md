

````markdown
# Lightweight Ransomware Prevention Web-Based App Using LightGBM

## Project Overview

This project implements a lightweight, web-based application designed for **static analysis and detection of ransomware** using a **LightGBM** machine learning model. The main goal is to provide an **accessible, low-resource defense mechanism** for small and medium-sized enterprises (SMEs) and individual users who may lack high-spec hardware or advanced cybersecurity expertise.

The application performs **static analysis of Portable Executable (PE) files** (like `.exe` or `.dll`) by extracting header features and uses a **pre-trained LightGBM model** to quickly determine if the file is likely benign or malicious (ransomware).

---

## Key Features

- **Lightweight Design**: Optimized for low-spec hardware (CPU-only, ≤4GB RAM).
- **Static Analysis**: Analyzes PE headers without executing the file, ensuring fast and safe scanning.
- **Web-Based Interface**: Simple UI built with **Bootstrap** for easy file upload and clear, color-coded results.
- **High Efficiency**: Uses LightGBM for fast predictions (<10 ms per file).
- **Privacy Focused**: Files are not stored after scanning (session-based processing).

---

## Methodology

The project follows an **Agile development methodology**:

1. Plan  
2. Design  
3. Develop  
4. Test  
5. Deploy  
6. Review  

---

## Technology Stack

- **Backend Framework**: Python (Flask)  
- **Machine Learning**: LightGBM (Gradient Boosting Framework)  
- **Feature Extraction**: `pefile` library (static PE header analysis)  
- **Frontend**: HTML/CSS (Bootstrap 5)  
- **Model Serialization**: `joblib`  

---

## Installation and Setup

### Prerequisites

1. Python 3.x  
2. pip (Python package installer)  
3. Virtual environment (recommended)  

### Steps

1. **Clone the repository**:

```bash
git clone [YOUR_REPO_URL]
cd ransomwareDetector
````

2. **Create and activate a virtual environment**:

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate   # Windows
```

3. **Install dependencies**:

```bash
pip install flask lightgbm pandas joblib pefile
```

4. **Ensure the following files are present in your project directory**:

* `model.joblib` (or `lightgbm_model.txt` if using LightGBM's native save format) – The trained classification model
* `app.py` – The Flask application script
* `feature_extractor.py` – Script containing `extract_features` function
* `templates/index.html` – Bootstrap frontend file

5. **Run the Flask application**:

```bash
python3 app.py
```

The application will start locally, typically accessible at: `http://127.0.0.1:5000`

---

## Usage

1. Open your browser and navigate to `http://127.0.0.1:5000`
2. Upload a **Portable Executable (.exe, .dll)** file using the form
3. Click **Scan File**
4. View results:

* **Green Alert**: File is benign (prediction = 1)
* **Red Alert**: File is malicious/ransomware (prediction = 0)

---

## Model Training and Data

### Dataset

* **Source**: Kaggle PE Header ransomware dataset (~2,157 samples)
* **Labeling**: Binary classification – Benign = 1, Malicious = 0
* **Features**: Static PE header fields (e.g., `Machine`, `ExportSize`, `ResourceSize`, `NumberOfSections`, `DllCharacteristics`, etc.)

### Feature Extraction Consistency

The `feature_extractor.py` script ensures that **features extracted at runtime match the type and order used during training**, guaranteeing accurate inference. Only static PE attributes are used for **speed and low resource usage**.

---

## Core Components

### `app.py` (Flask Backend)

* **/** (GET): Renders `index.html` frontend
* **/predict** (POST):

  * Handles file upload
  * Temporarily saves the file
  * Calls `feature_extractor.extract_features()`
  * Loads `model.joblib` once at startup
  * Performs prediction using the LightGBM model
  * Returns JSON response to frontend

### `feature_extractor.py`

Uses the `pefile` library to **statically read an executable** and generate a feature vector for the LightGBM model.

### `templates/index.html` (Bootstrap Frontend)

Provides the **file upload UI** and displays prediction results:

* **Benign**: Safe
* **Malicious**: Likely ransomware

---

## Notes

* Designed as a **final-year undergraduate thesis project**
* Focused on the **practical application of lightweight machine learning in cybersecurity**
* Optimized for **speed, low resource usage, and privacy**

---
