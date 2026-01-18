

---

```markdown
# Ransomware Prevention LightGBM Web App

A lightweight web application for detecting ransomware in PE files using LightGBM.  
The app allows batch file scanning, displays prediction results with probability, and visualizes data in interactive dashboards using Bootstrap and Chart.js.

---

## 1. Project Overview

- **Frontend:** Bootstrap 5 + HTML templates  
- **Backend:** Flask + Python  
- **ML Model:** LightGBM (primary), optional comparison with XGBoost or other models  
- **Data Handling:** PE file feature extraction using `pefile`  
- **Visualization:** Interactive charts for prediction distribution, probability trends, and detailed file features

---

## 2. Folder Structure

```

ransomwareDetector/
├── backend/
│   ├── app.py                # Flask web app
│   ├── feature_extractor.py  # Extract features from PE files
│   └── train_model.py        # Model training & evaluation
├── data/
│   ├── data_file.csv         # Original dataset
│   ├── sampled_2000_aligned.csv
│   └── samples/              # Raw sample files
├── experiments/
│   ├── align_and_predict.py
│   ├── batch_scan.py
│   ├── check_dataset_features.py
│   ├── find_label_candidates.py
│   ├── sample_2000.py
│   ├── sampled_2000.csv
│   └── sampled_2000_numeric.csv
├── models/
│   └── model.joblib          # Trained LightGBM model
├── outputs/
│   ├── predictions.csv
│   └── predictions (Copy).csv
├── static/                   # CSS, JS, images
├── templates/
│   ├── index.html
│   ├── results.html
│   └── features.html
├── test_files/               # Optional test files
├── venv/                     # Python virtual environment
├── README.md
└── requirements.txt

````

---

## 3. Prerequisites

- Python 3.10+  
- Virtual environment (`venv`)  
- Git  

---

## 4. Setup Instructions (New VM)

1. Clone the repository:

```bash
git clone https://github.com/alyakhay28/Ransomware-Prevention-LightGBM-Web-App.git
cd Ransomware-Prevention-LightGBM-Web-App
````

2. Create and activate virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate     # Linux/macOS
# venv\Scripts\activate      # Windows
```

3. Install required packages:

```bash
pip install -r requirements.txt
```

4. Launch the web app:

```bash
cd backend
python app.py
```

5. Open a browser at `http://127.0.0.1:5000/` to use the app.

---

## 5. Using the Web App

* **Upload PE files** through the homepage.
* **View results** in the dashboard:

  * Bar chart: classification per file
  * Pie chart: benign vs malicious distribution
  * Line chart: prediction probability trend
* **Detailed features** can be inspected per file.

---

## 6. Experiments & Model Comparison

### Folder

* `experiments/` → scripts for testing, data preprocessing, feature alignment, and predictions

### Running Experiments

1. Activate virtual environment:

```bash
source venv/bin/activate   # Linux/macOS
# venv\Scripts\activate    # Windows
```

2. Navigate to experiments folder:

```bash
cd experiments
```

3. Run a script (example):

```bash
python align_and_predict.py
```

4. Output files will be saved in:

* `outputs/` → predictions
* `data/` → processed datasets

---

### Adding and Comparing New Models

1. Train a new model in `backend/train_model.py`
2. Save the trained model in `models/` (e.g., `xgboost_model.joblib`)
3. Update `backend/app.py` to include the new model for predictions
4. Compare models using metrics like accuracy, F1-score, and prediction time

---

## 7. Notes

* `__pycache__/` and `venv/` are ignored in `.gitignore`
* For lightweight testing, ensure files in `test_files/` are small to avoid high RAM usage
* Use `pip freeze > requirements.txt` to update dependencies when adding new packages

---

