import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

# Load dataset
df = pd.read_csv("data/disease_symptoms.csv")

# Encode categorical columns
encoders = {}

categorical_cols = [
    "Fever",
    "Cough",
    "Fatigue",
    "Difficulty Breathing",
    "Gender",
    "Blood Pressure",
    "Cholesterol Level"
]

for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    encoders[col] = le

# Encode disease target
disease_encoder = LabelEncoder()

df["Disease"] = disease_encoder.fit_transform(
    df["Disease"]
)

# Features
X = df.drop(
    columns=["Disease", "Outcome Variable"]
)

# Target
y = df["Disease"]

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Model
model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(
    X_train,
    y_train
)

# Accuracy
accuracy = model.score(
    X_test,
    y_test
)

print("Accuracy:", accuracy)

# Save
joblib.dump(
    model,
    "models/disease_predictor.pkl"
)

joblib.dump(
    encoders,
    "models/encoders.pkl"
)

joblib.dump(
    disease_encoder,
    "models/disease_encoder.pkl"
)

print("Model Saved Successfully")