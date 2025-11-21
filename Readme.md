# CardioGuard AI • Neural Diagnostic System 🫀

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-ff4b4b)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.3%2B-orange)
![License](https://img.shields.io/badge/License-MIT-green)

**CardioGuard AI** is a state-of-the-art heart disease prediction system powered by machine learning. It utilizes a Random Forest Classifier to analyze patient biometric data and provide a real-time risk assessment. The application features a futuristic, "Ultra Premium" user interface designed for clarity, engagement, and professional medical aesthetics.

## ✨ Key Features

*   **🤖 Advanced ML Engine**: Powered by a robust Random Forest Classifier trained on clinical heart disease data.
*   **🎨 Futuristic UI/UX**: Immersive interface with animated backgrounds, particle effects, and glassmorphism design.
*   **📊 Interactive Biometrics**: Easy-to-use sliders and dropdowns for inputting patient data (Age, BP, Cholesterol, etc.).
*   **⚡ Real-time Analysis**: Instant risk probability calculation with visual feedback.
*   **📈 Dynamic Visualizations**:
    *   Animated gauge charts for risk scoring.
    *   Key health metrics dashboard.
    *   Lottie animations for visual engagement.
*   **🔄 Auto-Healing**: Automatically retrains the model if the model file is missing or incompatible.

## 🛠️ Tech Stack

*   **Frontend**: [Streamlit](https://streamlit.io/)
*   **Machine Learning**: [Scikit-learn](https://scikit-learn.org/)
*   **Data Processing**: [Pandas](https://pandas.pydata.org/)
*   **Visualization**: [Plotly](https://plotly.com/), [Streamlit-Lottie](https://github.com/andfanilo/streamlit-lottie)
*   **Model Serialization**: [Joblib](https://joblib.readthedocs.io/)

## 📂 Project Structure

```
├── app.py                  # Main Streamlit application
├── train_model.py          # Model training script
├── heart.csv               # Dataset for training
├── model.joblib            # Trained Random Forest model
├── healthy_profile.joblib  # Reference profile for default values
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## 🚀 Installation & Setup

1.  **Clone the repository** (or download the files):
    ```bash
    git clone <repository-url>
    cd heart-disease-prediction
    ```

2.  **Create a virtual environment** (optional but recommended):
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Train the Model** (First Run):
    If `model.joblib` is missing, the app will attempt to train it automatically. You can also manually train it:
    ```bash
    python train_model.py
    ```

## 💻 Usage

1.  **Run the application**:
    ```bash
    streamlit run app.py
    ```

2.  **Navigate the Interface**:
    *   Enter patient details in the **Biometric Input** section.
    *   Adjust sliders for numerical values (Age, Blood Pressure, etc.).
    *   Select options for categorical values (Chest Pain Type, ECG results, etc.).

3.  **Analyze**:
    *   Click the **⚡ INITIATE ANALYSIS** button.
    *   View the **Risk Probability** gauge and detailed recommendation card.

## ⚠️ Medical Disclaimer

**CardioGuard AI is a demonstration tool for educational and research purposes only.**

*   It is **NOT** a substitute for professional medical advice, diagnosis, or treatment.
*   Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition.
*   Do not disregard professional medical advice or delay in seeking it because of something you have read on this application.

---
© 2025 CardioGuard AI | Neural Diagnostic System
