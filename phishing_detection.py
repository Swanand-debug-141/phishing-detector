# Import necessary libraries
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Step 1: Load Dataset
df = pd.read_csv("dataset.csv")  # Load dataset
print("Dataset Loaded Successfully!")

# Step 2: Data Preprocessing
# Drop unnecessary columns
if 'id' in df.columns:
    df = df.drop(columns=['id'])  # Drop 'id' if it exists

# Separate Features (X) and Target Variable (y)
X = df.drop(columns=['CLASS_LABEL'])  # Drop target column
y = df['CLASS_LABEL']  # Target variable

# Get feature names for API use
feature_names = list(X.columns)
print("Features Used for Training:", feature_names)

# Step 3: Split Data into Training and Testing Sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Training Data Shape: {X_train.shape}")
print(f"Testing Data Shape: {X_test.shape}")

# Step 4: Train Machine Learning Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

print("Model Training Completed!")

# Step 5: Make Predictions
y_pred = model.predict(X_test)

# Step 6: Evaluate Model Performance
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

print("Classification Report:\n", classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

# Step 7: Save Model and Feature Names for API
joblib.dump(model, "phishing_model.pkl")
joblib.dump(feature_names, "feature_names.pkl")  # Save feature names separately
print("Model and Feature Names saved successfully!")
