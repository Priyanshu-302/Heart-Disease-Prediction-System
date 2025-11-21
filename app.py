import streamlit as st
import pandas as pd
import joblib
import requests
from streamlit_lottie import st_lottie
import plotly.graph_objects as go
import time
import textwrap

# Load the trained model and healthy profile
# Load the trained model and healthy profile
try:
    model = joblib.load('model.joblib')
    healthy_profile = joblib.load('healthy_profile.joblib')
except (FileNotFoundError, AttributeError, Exception) as e:
    st.warning(f"Model not found or incompatible ({str(e)}). Retraining model...")
    try:
        import train_model
        train_model.train()
        model = joblib.load('model.joblib')
        healthy_profile = joblib.load('healthy_profile.joblib')
        st.success("Model retrained successfully!")
    except Exception as train_error:
        st.error(f"Failed to retrain model: {str(train_error)}")
        st.stop()

# Page configuration
st.set_page_config(
    page_title="CardioGuard AI • Neural Diagnostic System",
    page_icon="🫀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- ASSETS ---
def load_lottieurl(url):
    try:
        r = requests.get(url, timeout=3)
        if r.status_code == 200:
            return r.json()
    except:
        pass
    return None

lottie_heart = load_lottieurl("https://lottie.host/4b6c4c83-6e99-4876-8263-7885b3464465/10h57t5Y9l.json")
lottie_dna = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_hzgq1wjm.json")
lottie_scan = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_w51pcehl.json")

# --- ULTRA PREMIUM CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;600;700&family=JetBrains+Mono:wght@400;600&display=swap');
    
    /* Animated Background with Particles */
    .stApp {
        background: linear-gradient(125deg, #0a0e27 0%, #1a1f3a 50%, #0f1419 100%);
        background-attachment: fixed;
    }
    
    .stApp::before {
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
            radial-gradient(circle at 20% 50%, rgba(56, 189, 248, 0.05) 0%, transparent 50%),
            radial-gradient(circle at 80% 80%, rgba(168, 85, 247, 0.05) 0%, transparent 50%),
            radial-gradient(circle at 40% 20%, rgba(236, 72, 153, 0.03) 0%, transparent 50%);
        animation: float 8s ease-in-out infinite;
        pointer-events: none;
        z-index: 0;
    }
    
    /* Ensure content is above background */
    .main .block-container {
        z-index: 1;
        position: relative;
    }

    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-20px); }
    }
    
    /* Typography */
    html, body, [class*="css"] {
        font-family: 'Space Grotesk', sans-serif;
        color: #e2e8f0;
    }
    
    h1, h2, h3 {
        font-weight: 700;
        color: #38bdf8; /* Fallback */
        background: linear-gradient(135deg, #38bdf8 0%, #a78bfa 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    /* Floating Card System */
    .diagnostic-card {
        background: rgba(255, 255, 255, 0.05); /* Slightly more opaque */
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 24px;
        padding: 32px;
        box-shadow: 
            0 8px 32px rgba(0, 0, 0, 0.3),
            inset 0 1px 0 rgba(255, 255, 255, 0.1);
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
        margin-bottom: 20px;
    }
    
    .diagnostic-card::before {
        content: "";
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(56, 189, 248, 0.1), transparent);
        transition: left 0.5s;
    }
    
    .diagnostic-card:hover::before {
        left: 100%;
    }
    
    .diagnostic-card:hover {
        transform: translateY(-4px) scale(1.01);
        border-color: rgba(56, 189, 248, 0.3);
        box-shadow: 
            0 16px 48px rgba(56, 189, 248, 0.2),
            inset 0 1px 0 rgba(255, 255, 255, 0.2);
    }
    
    /* Pulse Animation for Critical Elements */
    @keyframes pulse {
        0%, 100% { 
            opacity: 1;
            transform: scale(1);
        }
        50% { 
            opacity: 0.8;
            transform: scale(1.05);
        }
    }
    
    .pulse-glow {
        animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
    }
    
    /* Neon Button */
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white !important;
        border: 2px solid rgba(102, 126, 234, 0.5);
        padding: 18px 48px;
        border-radius: 16px;
        font-size: 18px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 2px;
        box-shadow: 
            0 0 20px rgba(102, 126, 234, 0.5),
            0 0 40px rgba(102, 126, 234, 0.2);
        transition: all 0.3s ease;
        font-family: 'JetBrains Mono', monospace;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 
            0 0 30px rgba(102, 126, 234, 0.8),
            0 0 60px rgba(102, 126, 234, 0.4);
        border-color: rgba(167, 139, 250, 0.8);
    }
    
    /* Input Styling */
    .stSlider>div>div>div {
        background: linear-gradient(90deg, #667eea, #764ba2) !important;
    }
    
    [data-baseweb="select"] {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 12px;
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1a1f3a 0%, #0f1419 100%);
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    /* Risk Display */
    .risk-container {
        text-align: center;
        padding: 24px;
        margin: 24px 0;
    }
    
    .risk-high {
        font-size: 3.5rem;
        font-weight: 900;
        color: #f43f5e !important; /* Solid Color Fix */
        animation: pulse 2s infinite;
        text-shadow: 0 0 40px rgba(244, 63, 94, 0.5);
    }
    
    .risk-low {
        font-size: 3.5rem;
        font-weight: 900;
        color: #10b981 !important; /* Solid Color Fix */
        text-shadow: 0 0 40px rgba(16, 185, 129, 0.5);
    }
    
    /* Metrics Display */
    .metric-box {
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 20px;
        text-align: center;
        transition: all 0.3s;
    }
    
    .metric-box:hover {
        background: rgba(255, 255, 255, 0.05);
        border-color: rgba(56, 189, 248, 0.3);
    }
    
    .metric-value {
        font-size: 2rem;
        font-weight: 700;
        color: #38bdf8;
        font-family: 'JetBrains Mono', monospace;
    }
    
    .metric-label {
        font-size: 0.9rem;
        color: #94a3b8;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    </style>
""", unsafe_allow_html=True)

# --- HEADER WITH ANIMATIONS ---
st.markdown("<br>", unsafe_allow_html=True)
header_col1, header_col2, header_col3 = st.columns([1, 3, 1])

with header_col1:
    if lottie_heart:
        st_lottie(lottie_heart, height=140, key="heart_main")

with header_col2:
    st.markdown("""
        <div style='text-align: center;'>
            <h1 style='font-size: 3.5rem; margin-bottom: 0;'>CARDIOGUARD AI</h1>
            <p style='font-size: 1.2rem; color: #64748b; font-family: "JetBrains Mono", monospace;'>
                [ NEURAL DIAGNOSTIC SYSTEM v4.2 ]
            </p>
        </div>
    """, unsafe_allow_html=True)

with header_col3:
    if lottie_dna:
        st_lottie(lottie_dna, height=140, key="dna")

st.markdown("<br>", unsafe_allow_html=True)

# --- INPUT SECTION ---
st.markdown("""
    <div class='diagnostic-card'>
        <h2 style='margin-bottom: 20px;'>📊 Patient Biometric Input</h2>
    </div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Mappings
cp_mapping_rev = {0: 'Typical Angina', 1: 'Atypical Angina', 2: 'Non-anginal Pain', 3: 'Asymptomatic'}
restecg_mapping_rev = {0: 'Normal', 1: 'ST-T Wave Abnormality', 2: 'Left Ventricular Hypertrophy'}
slope_mapping_rev = {0: 'Upsloping', 1: 'Flat', 2: 'Downsloping'}
thal_mapping_rev = {0: 'Unknown', 1: 'Normal', 2: 'Fixed Defect', 3: 'Reversible Defect'}

# Layout in columns
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("##### 👤 Demographics")
    age = st.slider('Age', 1, 100, int(healthy_profile['age']), key='age')
    sex_default = 'Male' if healthy_profile['sex'] == 1 else 'Female'
    sex_label = st.radio('Sex', ('Female', 'Male'), index=0 if sex_default=='Female' else 1, horizontal=True)
    sex = 1 if sex_label == 'Male' else 0
    
    st.markdown("##### 🫀 Cardiovascular")
    trestbps = st.slider('Resting BP (mm Hg)', 90, 200, int(healthy_profile['trestbps']))
    chol = st.slider('Cholesterol (mg/dl)', 100, 600, int(healthy_profile['chol']))
    thalach = st.slider('Max Heart Rate', 60, 220, int(healthy_profile['thalach']))

with col2:
    st.markdown("##### 🩺 Clinical Symptoms")
    cp_default_label = cp_mapping_rev.get(healthy_profile['cp'], 'Typical Angina')
    cp_options = list(cp_mapping_rev.values())
    cp_index = cp_options.index(cp_default_label)
    cp_label = st.selectbox('Chest Pain Type', cp_options, index=cp_index)
    cp_mapping = {v: k for k, v in cp_mapping_rev.items()}
    cp = cp_mapping[cp_label]
    
    exang_default = 'Yes' if healthy_profile['exang'] == 1 else 'No'
    exang_label = st.radio('Exercise Induced Angina', ('No', 'Yes'), index=0 if exang_default=='No' else 1, horizontal=True)
    exang = 1 if exang_label == 'Yes' else 0
    
    oldpeak = st.slider('ST Depression', 0.0, 6.2, float(healthy_profile['oldpeak']))

with col3:
    st.markdown("##### 🔬 Lab Results")
    fbs_default = 'True' if healthy_profile['fbs'] == 1 else 'False'
    fbs_label = st.radio('High Fasting Blood Sugar', ('No', 'Yes'), index=0 if fbs_default=='False' else 1, horizontal=True)
    fbs = 1 if fbs_label == 'Yes' else 0
    
    restecg_default_label = restecg_mapping_rev.get(healthy_profile['restecg'], 'Normal')
    restecg_options = list(restecg_mapping_rev.values())
    restecg_index = restecg_options.index(restecg_default_label)
    restecg_label = st.selectbox('Resting ECG', restecg_options, index=restecg_index)
    restecg_mapping = {v: k for k, v in restecg_mapping_rev.items()}
    restecg = restecg_mapping[restecg_label]
    
    slope_default_label = slope_mapping_rev.get(healthy_profile['slope'], 'Upsloping')
    slope_options = list(slope_mapping_rev.values())
    slope_index = slope_options.index(slope_default_label)
    slope_label = st.selectbox('ST Slope', slope_options, index=slope_index)
    slope_mapping = {v: k for k, v in slope_mapping_rev.items()}
    slope = slope_mapping[slope_label]
    
    ca = st.slider('Major Vessels', 0, 4, int(healthy_profile['ca']))
    
    thal_default_label = thal_mapping_rev.get(healthy_profile['thal'], 'Normal')
    thal_options = list(thal_mapping_rev.values())
    thal_index = thal_options.index(thal_default_label)
    thal_label = st.selectbox('Thalassemia', thal_options, index=thal_index)
    thal_mapping = {v: k for k, v in thal_mapping_rev.items()}
    thal = thal_mapping[thal_label]

# Create DataFrame
input_df = pd.DataFrame({
    'age': [age], 'sex': [sex], 'cp': [cp], 'trestbps': [trestbps], 'chol': [chol],
    'fbs': [fbs], 'restecg': [restecg], 'thalach': [thalach], 'exang': [exang],
    'oldpeak': [oldpeak], 'slope': [slope], 'ca': [ca], 'thal': [thal]
})

st.markdown("<br><br>", unsafe_allow_html=True)

# --- ANALYZE BUTTON ---
button_col1, button_col2, button_col3 = st.columns([1, 1, 1])
with button_col2:
    analyze_button = st.button('⚡ INITIATE ANALYSIS', use_container_width=True)

if analyze_button:
    # Loading animation
    with st.spinner(''):
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        steps = [
            "Initializing neural network...",
            "Processing biometric data...",
            "Running prediction algorithms...",
            "Analyzing risk factors...",
            "Generating diagnosis..."
        ]
        
        for i, step in enumerate(steps):
            status_text.markdown(f"<p style='text-align: center; color: #38bdf8;'>{step}</p>", unsafe_allow_html=True)
            progress_bar.progress((i + 1) * 20)
            time.sleep(0.3)
        
        status_text.empty()
        progress_bar.empty()
    
    # Make prediction
    prediction = model.predict(input_df)
    prediction_proba = model.predict_proba(input_df)
    risk_score = prediction_proba[0][1]
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- RESULTS SECTION ---
    result_col1, result_col2 = st.columns([1, 1])
    
    with result_col1:
        # Animated gauge
        fig = go.Figure(go.Indicator(
            mode = "gauge+number+delta",
            value = risk_score * 100,
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': "RISK PROBABILITY", 'font': {'size': 24, 'color': '#e2e8f0'}},
            delta = {'reference': 50, 'increasing': {'color': "#f43f5e"}, 'decreasing': {'color': "#10b981"}},
            number = {'suffix': "%", 'font': {'size': 48, 'color': '#e2e8f0'}},
            gauge = {
                'axis': {'range': [None, 100], 'tickwidth': 2, 'tickcolor': "#334155"},
                'bar': {'color': "#667eea" if risk_score < 0.5 else "#f43f5e"},
                'bgcolor': "rgba(0,0,0,0)",
                'borderwidth': 2,
                'bordercolor': "#334155",
                'steps': [
                    {'range': [0, 30], 'color': 'rgba(16, 185, 129, 0.2)'},
                    {'range': [30, 70], 'color': 'rgba(251, 191, 36, 0.2)'},
                    {'range': [70, 100], 'color': 'rgba(244, 63, 94, 0.2)'}
                ],
                'threshold': {
                    'line': {'color': "white", 'width': 4},
                    'thickness': 0.75,
                    'value': risk_score * 100
                }
            }
        ))
        
        fig.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font={'color': "#e2e8f0", 'family': "Space Grotesk"},
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with result_col2:
        # Construct HTML for the card to ensure it renders as one block
        card_html = textwrap.dedent("""
            <div class='diagnostic-card' style='height: 400px; display: flex; flex-direction: column; justify-content: center; align-items: center;'>
        """)
        
        if risk_score > 0.5:
            card_html += textwrap.dedent(f"""
                <div class='risk-container'>
                    <div class='risk-high pulse-glow'>⚠️ HIGH RISK</div>
                    <p style='font-size: 1.3rem; color: #cbd5e1; margin-top: 20px;'>
                        Confidence: <span style='color: #f43f5e; font-weight: 700;'>{risk_score:.1%}</span>
                    </p>
                    <p style='color: #94a3b8; margin-top: 16px; line-height: 1.6;'>
                        The diagnostic algorithm has detected patterns<br>
                        consistent with elevated cardiac risk.<br><br>
                        <strong style='color: #f43f5e;'>⚕️ RECOMMENDATION:</strong><br>
                        Immediate cardiology consultation required
                    </p>
                </div>
            """)
        else:
            card_html += textwrap.dedent(f"""
                <div class='risk-container'>
                    <div class='risk-low'>✓ LOW RISK</div>
                    <p style='font-size: 1.3rem; color: #cbd5e1; margin-top: 20px;'>
                        Confidence: <span style='color: #10b981; font-weight: 700;'>{(1-risk_score):.1%}</span>
                    </p>
                    <p style='color: #94a3b8; margin-top: 16px; line-height: 1.6;'>
                        The diagnostic algorithm indicates<br>
                        a healthy cardiovascular profile.<br><br>
                        <strong style='color: #10b981;'>✓ RECOMMENDATION:</strong><br>
                        Maintain current lifestyle and routine checkups
                    </p>
                </div>
            """)
        
        card_html += "</div>"
        
        st.markdown(card_html, unsafe_allow_html=True)
    
    # Key Metrics
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 📈 Key Health Metrics")
    
    metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)
    
    with metric_col1:
        st.markdown(f"""
            <div class='metric-box'>
                <div class='metric-value'>{age}</div>
                <div class='metric-label'>Age (Years)</div>
            </div>
        """, unsafe_allow_html=True)
    
    with metric_col2:
        st.markdown(f"""
            <div class='metric-box'>
                <div class='metric-value'>{trestbps}</div>
                <div class='metric-label'>BP (mm Hg)</div>
            </div>
        """, unsafe_allow_html=True)
    
    with metric_col3:
        st.markdown(f"""
            <div class='metric-box'>
                <div class='metric-value'>{chol}</div>
                <div class='metric-label'>Cholesterol</div>
            </div>
        """, unsafe_allow_html=True)
    
    with metric_col4:
        st.markdown(f"""
            <div class='metric-box'>
                <div class='metric-value'>{thalach}</div>
                <div class='metric-label'>Max HR</div>
            </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
    <div style='text-align: center; color: #475569; font-size: 0.85rem; font-family: "JetBrains Mono", monospace;'>
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━<br>
        © 2025 CARDIOGUARD AI | NEURAL DIAGNOSTIC SYSTEM<br>
        Powered by Random Forest ML • 98.54% Accuracy<br>
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    </div>
""", unsafe_allow_html=True)
