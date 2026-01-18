#!/usr/bin/env python3
"""
batch_scan.py
Iterate over all .exe files in samples/benign and samples/malicious,
POST each to the Flask API at /predict, and write results to outputs/predictions.csv.
"""

import os
import csv
import time
import requests

API_URL = "http://127.0.0.1:5000/predict"  # adjust if different
SAMPLE_DIRS = {
    "benign": "/home/alyakhay/Desktop/ransomwareDetector/samples/benign",
    "malicious": "/home/alyakhay/Desktop/ransomwareDetector/samples/malicious"
}
OUT_CSV = "outputs/predictions.csv"
TIMEOUT = 20  # seconds

os.makedirs("outputs", exist_ok=True)

fieldnames = [
    "timestamp", "source_label", "filename", "filesize_bytes", "status_code",
    "prediction", "error", "elapsed_seconds"
]

def scan_file(path, source_label):
    start = time.time()
    filename = os.path.basename(path)
    filesize = os.path.getsize(path)
    try:
        with open(path, "rb") as f:
            files = {"file": (filename, f, "application/octet-stream")}
            resp = requests.post(API_URL, files=files, timeout=TIMEOUT)
        elapsed = time.time() - start
        if resp.status_code == 200:
            data = resp.json()
            pred = data.get("prediction", data.get("predictions", None))
            # normalize prediction value (single file -> single int)
            if isinstance(pred, list):
                pred = pred[0] if pred else None
            return {
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
                "source_label": source_label,
                "filename": filename,
                "filesize_bytes": filesize,
                "status_code": resp.status_code,
                "prediction": pred,
                "error": "",
                "elapsed_seconds": round(elapsed, 3)
            }
        else:
            return {
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
                "source_label": source_label,
                "filename": filename,
                "filesize_bytes": filesize,
                "status_code": resp.status_code,
                "prediction": None,
                "error": f"HTTP {resp.status_code}: {resp.text[:200]}",
                "elapsed_seconds": round(time.time()-start, 3)
            }
    except Exception as e:
        return {
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "source_label": source_label,
            "filename": filename,
            "filesize_bytes": filesize,
            "status_code": None,
            "prediction": None,
            "error": str(e),
            "elapsed_seconds": round(time.time()-start, 3)
        }

def main():
    # prepare CSV
    write_header = not os.path.exists(OUT_CSV)
    with open(OUT_CSV, "a", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if write_header:
            writer.writeheader()

        for label, d in SAMPLE_DIRS.items():
            if not os.path.isdir(d):
                print(f"[WARN] Sample folder not found: {d}")
                continue
            files = sorted([f for f in os.listdir(d) if f.lower().endswith(".exe")])
            print(f"[INFO] Scanning {len(files)} files in {d} (label={label})")
            for fn in files:
                path = os.path.join(d, fn)
                print(f"  -> {fn}", end="", flush=True)
                result = scan_file(path, label)
                writer.writerow(result)
                print(f"  done (pred={result['prediction']} err={bool(result['error'])})")

if __name__ == "__main__":
    main()

