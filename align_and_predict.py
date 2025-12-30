import pandas as pd
import joblib, pickle

# ------------------------------
# CONFIG — update model filename if needed
MODEL_PATH = "model.joblib"
INPUT_CSV = "sampled_2000_numeric.csv"
OUTPUT_CSV = "sampled_2000_aligned.csv"
# ------------------------------

# Load the model
try:
    model = joblib.load(MODEL_PATH)
except Exception:
    model = pickle.load(open(MODEL_PATH, "rb"))

# Get feature names from the model
names = None
if hasattr(model, "feature_name_") and model.feature_name_:
    names = list(model.feature_name_)
elif hasattr(model, "booster_") and hasattr(model.booster_, "feature_name"):
    names = list(model.booster_.feature_name())
elif hasattr(model, "feature_name") and callable(model.feature_name):
    names = list(model.feature_name())
else:
    raise SystemExit("Could not determine model feature names. Check model file.")

print("Model expects these features:", names)

# Load CSV
df = pd.read_csv(INPUT_CSV)
print("Original CSV columns:", list(df.columns))

# Drop extra columns
extra = [c for c in df.columns if c not in names]
if extra:
    print("Dropping extra columns:", extra)
    df = df.drop(columns=extra)

# Add missing columns with zeros
missing = [c for c in names if c not in df.columns]
if missing:
    print("Adding missing columns (filled with 0):", missing)
    for c in missing:
        df[c] = 0

# Reorder columns to match model
df = df[names]

# Ensure all numeric
df = df.apply(pd.to_numeric, errors="coerce").fillna(0)

# Save aligned CSV
df.to_csv(OUTPUT_CSV, index=False)
print("Saved aligned CSV as:", OUTPUT_CSV)
