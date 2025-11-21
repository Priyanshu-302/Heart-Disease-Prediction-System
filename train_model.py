import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os

def train():
    # Load dataset
    if not os.path.exists('heart.csv'):
        raise FileNotFoundError("heart.csv not found. Cannot train model.")
        
    df = pd.read_csv('heart.csv')

    # Separate features and target
    X = df.drop('target', axis=1)
    y = df['target']

    # Define categorical and numerical features
    categorical_features = ['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal']
    numerical_features = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']

    # Create preprocessing steps
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), numerical_features),
            ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
        ])

    # Create the pipeline
    pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('classifier', RandomForestClassifier(random_state=42))
    ])

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    print("Training model...")
    pipeline.fit(X_train, y_train)

    # Evaluate
    y_pred = pipeline.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {accuracy:.4f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))

    # Save the model
    joblib.dump(pipeline, 'model.joblib')
    print("Model saved to model.joblib")

    # Calculate and save typical healthy profile (target = 0)
    print("Calculating typical healthy profile...")
    healthy_df = df[df['target'] == 0].drop('target', axis=1)
    healthy_profile = {}

    for col in healthy_df.columns:
        if col in categorical_features:
            # For categorical, use mode
            healthy_profile[col] = healthy_df[col].mode()[0]
        else:
            # For numerical, use mean (rounded for integer sliders if needed, but mean is safer for "typical")
            healthy_profile[col] = healthy_df[col].mean()

    # Adjust specific integer fields if necessary (though sliders handle floats, int is cleaner for some)
    int_columns = ['age', 'trestbps', 'chol', 'thalach', 'ca']
    for col in int_columns:
        if col in healthy_profile:
            healthy_profile[col] = int(healthy_profile[col])

    joblib.dump(healthy_profile, 'healthy_profile.joblib')
    print("Healthy profile saved to healthy_profile.joblib")
    print("Profile:", healthy_profile)

if __name__ == "__main__":
    train()
