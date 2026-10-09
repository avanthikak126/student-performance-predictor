import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Load the dataset
df = pd.read_csv("dataset.csv")

# Features and target
X = df[["study_hours", "attendance", "previous_marks"]]
y = df["final_marks"]

# Train the model
model = LinearRegression()
model.fit(X, y)

# Save the trained model
joblib.dump(model, "model.pkl")

print("Model trained and saved as model.pkl")
