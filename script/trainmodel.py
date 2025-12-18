import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LogisticRegression
import pickle
import os

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(BASE_DIR, "data", "titanic_ml.csv")
MODEL_PATH = os.path.join(BASE_DIR, "data", "titanic_model.pkl")

# Load data
df = pd.read_csv(CSV_PATH)

# Encode categorical variables
encoder = OneHotEncoder(sparse_output=False, drop='first')
encoded_cols = encoder.fit_transform(df[['sex', 'embarked']])
encoded_df = pd.DataFrame(encoded_cols, columns=encoder.get_feature_names_out(['sex','embarked']))

# Combine numeric + encoded features
X = pd.concat([df[['pclass','age','fare']], encoded_df], axis=1)
y = df['survived']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Logistic Regression
model = LogisticRegression(max_iter=500)
model.fit(X_train, y_train)

# Evaluate
score = model.score(X_test, y_test)
print(f"Test Accuracy: {score:.4f}")

# Save model
with open(MODEL_PATH, 'wb') as f:
    pickle.dump(model, f)

print("Model saved to:", MODEL_PATH)
