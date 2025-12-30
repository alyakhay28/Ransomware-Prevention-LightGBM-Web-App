# Lightweight Ransomware Prevention Web-Based App Using LightGBM

## Project Overview

This project implements a lightweight, web-based application designed for **static analysis and detection of ransomware** using a **LightGBM** machine learning model. The main goal is to provide an **accessible, low-resource defense mechanism** for small and medium-sized enterprises (SMEs) and individual users who may lack high-spec hardware or advanced cybersecurity expertise.

The application performs **static analysis of Portable Executable (PE) files** (like `.exe` or `.dll`) by extracting header features and uses a **pre-trained LightGBM model** to quickly determine if the file is likely benign or malicious.

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
