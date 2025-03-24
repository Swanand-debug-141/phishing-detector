# Import necessary libraries
import pandas as pd
import joblib
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.feature_selection import SelectKBest, f_classif

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

# Step 3: Feature Selection (Select top 20 best features)
selector = SelectKBest(score_func=f_classif, k=20)
X_selected = selector.fit_transform(X, y)

# Get selected feature names for API use
selected_features = X.columns[selector.get_support()]
print("Selected Features:", selected_features)

# Step 4: Split Data into Training and Testing Sets
X_train, X_test, y_train, y_test = train_test_split(X_selected, y, test_size=0.2, random_state=42)

# Step 5: Train XGBoost Model
model = xgb.XGBClassifier(n_estimators=200, learning_rate=0.1, max_depth=6, use_label_encoder=False, eval_metric='logloss')
model.fit(X_train, y_train)

print("XGBoost Model Training Completed!")

# Step 6: Make Predictions
y_pred = model.predict(X_test)

# Step 7: Evaluate Model Performance
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")
print("Classification Report:\n", classification_report(y_test, y_pred))

# Step 8: Save Model and Feature Names for API
joblib.dump(model, "phishing_model_xgb.pkl")
joblib.dump(selected_features.tolist(), "selected_features.pkl")  # Save selected feature names
print("Model and Selected Features saved successfully!")
