
### **1. Project Title & Description**

```markdown
# Ransomware Prevention LightGBM Web App

This web app detects ransomware in Windows PE files using LightGBM.  
Users can upload files, see prediction results, probability trends, and detailed feature analysis.
```

---

### **2. Folder Structure (explained)**

```markdown
## Folder Structure

- `backend/` → Flask app & model training scripts (`app.py`, `feature_extractor.py`, `train_model.py`)  
- `data/` → CSV datasets and sample files for testing/training  
- `models/` → Trained LightGBM model (`model.joblib`)  
- `outputs/` → Prediction outputs from batch scans  
- `templates/` → HTML templates for Flask (`index.html`, `results.html`, `features.html`)  
- `static/` → Static files (CSS, JS, images)  
- `experiments/` → Data preprocessing, feature alignment, and experiment scripts  
- `test_files/` → Example PE files for testing  
- `venv/` → Python virtual environment (excluded in GitHub `.gitignore`)
```

---

### **3. Prerequisites**

```markdown
## Prerequisites

- Python 3.9+  
- Virtual environment (venv)  
- Git  
```

---

### **4. Setup & Install Dependencies**

````markdown
## Setup

1. Clone the repo:
```bash
git clone https://github.com/alyakhay28/Ransomware-Prevention-LightGBM-Web-App.git
cd Ransomware-Prevention-LightGBM-Web-App
````

2. Create and activate virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
```

3. Install Python dependencies:

```bash
pip install -r requirements.txt
```

````

---

### **5. Running the App**

```markdown
## Run the Web App

1. Start Flask server:
```bash
cd backend
python app.py
````

2. Open browser at `http://127.0.0.1:5000`
3. Upload PE files and see scan results with charts and detailed feature tables.

````

---

### **6. Notes / Optional Info**

```markdown
## Notes

- The trained model is in `models/model.joblib`.  
- Any batch predictions are stored in `outputs/`.  
- Frontend uses Bootstrap 5 and Chart.js for visualizations.  
- The repo is tested on Ubuntu VM; minor adjustments may be needed for Windows.
````

---


