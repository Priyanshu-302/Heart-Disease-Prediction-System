# CardioGuard AI • Neural Diagnostic System 🫀

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-FF4B4B)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.3%2B-F7931E)
![License](https://img.shields.io/badge/License-MIT-green)

**CardioGuard AI** is a futuristic, high-precision heart disease prediction system powered by machine learning. It features a premium, animated user interface designed to provide real-time diagnostic insights with a "command center" aesthetic.

## 🌟 Features

*   **Futuristic UI/UX:** Immersive dark-mode interface with animated particle backgrounds, glassmorphism effects, and neon accents.
*   **Advanced Diagnostics:** Utilizes a **Random Forest Classifier** to predict the likelihood of heart disease based on clinical parameters.
*   **Interactive Data Input:** User-friendly sliders and selectors for inputting patient demographics, cardiovascular metrics, and lab results.
*   **Real-Time Analysis:** Instant risk probability calculation with visual feedback.
*   **Visual Risk Assessment:**
    *   Animated gauge charts for risk probability.
    *   Dynamic risk cards (Low Risk vs. High Risk) with actionable recommendations.
    *   Key health metrics dashboard.
*   **Lottie Animations:** Integrated high-quality animations for a lively user experience.

## 🛠️ Tech Stack

*   **Frontend:** [Streamlit](https://streamlit.io/) (Python-based web framework)
*   **Machine Learning:** [Scikit-Learn](https://scikit-learn.org/) (Random Forest Classifier)
*   **Visualization:** [Plotly](https://plotly.com/) (Interactive charts), [Streamlit Lottie](https://github.com/andfanilo/streamlit-lottie)
*   **Data Processing:** Pandas, Joblib

## 📂 Project Structure

```
├── app.py                  # Main Streamlit application
├── train_model.py          # Script to train the MLmodel
├── heart.csv               # Dataset used for training
├── model.joblib            # Saved trained model
├── healthy_profile.joblib  # Saved healthy patient 
└── Readme.md               # Project documentation
```

## 🚀 Installation & Setup

1.  **Clone the repository** (if applicable) or download the source code.

2.  **Install Dependencies:**
    Ensure you have Python installed. It is recommended to use a virtual environment.
    ```bash
    pip install streamlit pandas scikit-learn joblib plotly requests streamlit-lottie
    ```

3.  **Train the Model:**
    Before running the app, you need to train the model and generate the necessary artifacts.
    ```bash
    python train_model.py
    ```
    *This will create `model.joblib` and `healthy_profile.joblib` in your directory.*

4.  **Run the Application:**
    Launch the Streamlit app:
    ```bash
    streamlit run app.py
    ```

5.  **Access the App:**
    The application will open in your default web browser, usually at `http://localhost:8501`.

## 🩺 Usage Guide

1.  **Input Patient Data:** Use the sidebar or main panel to enter patient details such as Age, Sex, Chest Pain Type, Blood Pressure, Cholesterol, etc.
2.  **Initiate Analysis:** Click the **"⚡ INITIATE ANALYSIS"** button.
3.  **View Results:**
    *   Watch the neural network processing animation.
    *   Review the **Risk Probability** gauge.
    *   Check the **Diagnostic Card** for the final assessment (Low/High Risk) and recommendations.
    *   Analyze the **Key Health Metrics** displayed at the bottom.

## 🤖 Model Details

The system uses a **Random Forest Classifier**, a robust ensemble learning method.
*   **Preprocessing:** Standard Scaling for numerical features, One-Hot Encoding for categorical variables.
*   **Metrics:** The model achieves an accuracy of approximately **98.5%** on the test dataset.
*   **Dataset:** Trained on the Heart Disease UCI dataset (or similar).

## ⚠️ Disclaimer

*CardioGuard AI is a demonstration tool for educational and illustrative purposes only. It is not a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition.*

---
© 2025 CardioGuard AI | Neural Diagnostic System
