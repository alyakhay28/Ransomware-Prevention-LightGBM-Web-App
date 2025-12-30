import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score
from lightgbm import LGBMClassifier
import joblib

df = pd.read_csv('sampled_2000.csv')
df = df.drop(columns=['FileName', 'md5Hash'], errors='ignore')

X = df.drop(columns=['Benign'])
y = df['Benign']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, stratify=y, test_size=0.2, random_state=42
)

model = LGBMClassifier(max_depth=7, learning_rate=0.05, n_estimators=200)
model.fit(X_train, y_train)

pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, pred))
print("F1 Score:", f1_score(y_test, pred))

joblib.dump(model, 'model.joblib')
print("Model saved as model.joblib")
