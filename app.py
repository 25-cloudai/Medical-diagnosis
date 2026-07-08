import streamlit as st
st.set_page_config(
    page_title="AI Medical Diagnosis Assistant",
    page_icon="🩺",
    layout="wide"
)
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
from pdf_report import generate_pdf
import plotly.graph_objects as go
import cv2
from db import *

create_table()
create_users_table()
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.warning("Please login first")
    st.stop()

# -------------------------------
# PAGE CONFIG
# -------------------------------

st.success(
    f"Welcome {st.session_state['user']} 👋"
)

st.markdown("""
<style>

/* -----------------------------
   MAIN APP
------------------------------*/

.stApp{
    background:#1a1a1a;
    color:white;
}

/* Hide Streamlit Menu */

#MainMenu{visibility:hidden;}
footer{visibility:hidden;}
header{visibility:hidden;}

/* Container */

.block-container{
    padding-top:1.5rem;
    padding-bottom:2rem;
}

/* -----------------------------
   TITLE
------------------------------*/

.title{
    font-size:48px;
    font-weight:700;
    text-align:center;
    color:#ffffff;
}

.subtitle{
    text-align:center;
    color:#d1d5db;
    font-size:20px;
    margin-bottom:20px;
}

/* -----------------------------
   SIDEBAR
------------------------------*/

section[data-testid="stSidebar"]{
    background:#242424;
}

section[data-testid="stSidebar"] *{
    color:white !important;
}

/* -----------------------------
   METRIC CARDS
------------------------------*/

[data-testid="stMetric"]{
    background:#2b2b2b;
    border-radius:15px;
    padding:15px;
    border:1px solid #3a3a3a;
}

[data-testid="stMetricLabel"]{
    color:#d1d5db !important;
    font-weight:bold;
}

[data-testid="stMetricValue"]{
    color:#22c55e !important;
    font-size:34px !important;
}

/* -----------------------------
   INPUT BOXES
------------------------------*/

.stTextInput input,
.stNumberInput input{
    background:white !important;
    color:black !important;
    border-radius:10px;
    border:none;
}

.stTextInput label,
.stNumberInput label{
    color:white !important;
}

/* -----------------------------
   SELECT BOX
------------------------------*/

div[data-baseweb="select"]>div{
    background:white !important;
    color:black !important;
    border-radius:10px;
}

div[data-baseweb="select"] span{
    color:black !important;
}

/* -----------------------------
   FILE UPLOADER
------------------------------*/

[data-testid="stFileUploader"]{
    background:#2b2b2b;
    border-radius:15px;
    border:1px solid #3a3a3a;
    padding:20px;
}

[data-testid="stFileUploader"] *{
    color:white !important;
}

/* Upload Button */

[data-testid="stFileUploader"] button{
    background:white !important;
    color:black !important;
    border-radius:8px;
}

/* -----------------------------
   BUTTONS
------------------------------*/

.stButton>button{
    width:100%;
    background:#22c55e;
    color:white;
    border:none;
    border-radius:10px;
    font-weight:bold;
    padding:10px;
}

.stButton>button:hover{
    background:#16a34a;
}

/* Download Button */

.stDownloadButton>button{
    width:100%;
    background:#22c55e;
    color:white;
    border:none;
    border-radius:10px;
    font-weight:bold;
}

.stDownloadButton>button:hover{
    background:#16a34a;
}

/* -----------------------------
   SUCCESS
------------------------------*/

.stSuccess{
    border-radius:12px;
}

/* -----------------------------
   WARNING
------------------------------*/

.stWarning{
    border-radius:12px;
}

/* -----------------------------
   ERROR
------------------------------*/

.stError{
    border-radius:12px;
}

/* -----------------------------
   INFO
------------------------------*/

.stInfo{
    border-radius:12px;
}

/* -----------------------------
   CHAT
------------------------------*/

[data-testid="stChatMessage"]{
    background:#2b2b2b;
    border-radius:12px;
    padding:12px;
}

/* -----------------------------
   TABLES
------------------------------*/

table{
    border-collapse:collapse;
    width:100%;
}

th{
    background:#22c55e;
    color:white;
}

td{
    background:#2b2b2b;
    color:white;
}

/* -----------------------------
   HEADINGS
------------------------------*/

h1,h2,h3,h4{
    color:white;
}

/* -----------------------------
   IMAGE
------------------------------*/

img{
    border-radius:12px;
}

/* -----------------------------
   SCROLLBAR
------------------------------*/

::-webkit-scrollbar{
    width:8px;
}

::-webkit-scrollbar-thumb{
    background:#22c55e;
    border-radius:10px;
}

/* -----------------------------
   FOOTER
------------------------------*/

.stCaption{
    color:#d1d5db !important;
    text-align:center;
}
/* Text Input */
.stTextInput input {
    color: black !important;
    background-color: white !important;
}

/* Number Input */
.stNumberInput input {
    color: black !important;
    background-color: white !important;
}

/* Selectbox (Gender) */
div[data-baseweb="select"] > div {
    color: black !important;
    background-color: white !important;
}

div[data-baseweb="select"] span {
    color: black !important;
}

div[data-baseweb="select"] svg {
    fill: black !important;
}

/* Dropdown Options */
div[role="option"] {
    color: black !important;
    background: white !important;
}

/* File Uploader */
[data-testid="stFileUploader"] * {
    color: black !important;
}

[data-testid="stFileUploader"] button {
    color: black !important;
    background: white !important;
}

/* Placeholder */
input::placeholder {
    color: gray !important;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# LOAD MODEL
# -------------------------------
model = load_model("models/pneumonia_model.keras")

# -------------------------------
# SIDEBAR
# -------------------------------
st.sidebar.title("👤 Patient Information")

patient_name = st.sidebar.text_input("Patient Name")

age = st.sidebar.number_input(
    "Age",
    min_value=1,
    max_value=120,
    value=25
)

gender = st.sidebar.selectbox(
    "Gender",
    ["Male", "Female", "Other"]
)

st.sidebar.markdown("---")

st.sidebar.info("""
This AI system assists in detecting
Pneumonia from Chest X-Ray images.

⚠️ Not a replacement for professional diagnosis.
""")
if st.sidebar.button("🚪 Logout"):

    st.session_state.clear()

    st.rerun()

# -------------------------------
# HEADER
# -------------------------------
st.markdown(
    '<p class="title">🩺 AI Medical Diagnosis Assistant</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="subtitle">Deep Learning Powered Chest X-Ray Analysis</p>',
    unsafe_allow_html=True
)

st.markdown("---")

# -------------------------------
# DASHBOARD METRICS
# -------------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Model Accuracy", "95%")

with col2:
    st.metric("Dataset Images", "5216")

with col3:
    st.metric("Disease Support", "Pneumonia")

st.markdown("---")

# -------------------------------
# FILE UPLOAD
# -------------------------------
uploaded_file = st.file_uploader(
    "📤 Upload Chest X-Ray Image",
    type=["jpg", "jpeg", "png"]
)
result = ""

# -------------------------------
# PREDICTION
# -------------------------------
if uploaded_file:

    image = Image.open(uploaded_file)

    col1, col2 = st.columns(2)

    with col1:

        st.image(
            image,
            caption="Uploaded X-Ray",
            use_container_width=True
        )

    image = image.resize((224, 224))

    img_array = np.array(image)

    if len(img_array.shape) == 2:
        img_array = np.stack(
            (img_array,) * 3,
            axis=-1
        )

    img_array = img_array / 255.0

    img_array = np.expand_dims(
        img_array,
        axis=0
    )

    prediction = model.predict(img_array)

    confidence = float(prediction[0][0])

    with col2:

        st.subheader("📊 Diagnosis Result")

        if confidence >= 0.5:

            result = "Pneumonia"

            st.error(
                "🫁 Pneumonia Detected"
            )

            display_confidence = confidence * 100

        else:

            result = "Normal"

            st.success(
                "✅ Normal Chest X-Ray"
            )

            display_confidence = (1 - confidence) * 100

        # Save patient once
        save_patient(
            patient_name,
            age,
            gender,
            result,
            display_confidence
        )

        st.metric(
            "Confidence",
            f"{display_confidence:.2f}%"
        )

# -------------------------
# GAUGE CHART
# -------------------------
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=display_confidence,
            title={'text': "AI Confidence"},
            gauge={
                'axis': {'range': [0, 100]}
            }
        ))

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.markdown("---")
    st.markdown("---")

# -------------------------
# RECOMMENDATIONS
# -------------------------
    st.subheader("🤖 AI Health Recommendations")

    if result == "Pneumonia":

        st.warning("""
### 🫁 Recommended Actions

✔ Consult a doctor immediately

✔ Take prescribed medications

✔ Stay hydrated

✔ Get adequate rest

✔ Avoid smoking and dust exposure

✔ Monitor breathing difficulties

✔ Seek emergency care if symptoms worsen

✔ Follow-up chest examination if advised
""")

    else:

        st.success("""
### ✅ Healthy Recommendations

✔ Maintain a healthy lifestyle

✔ Continue regular exercise

✔ Eat a balanced diet

✔ Drink sufficient water

✔ Avoid smoking

✔ Get adequate sleep

✔ Schedule routine health checkups

✔ Maintain good respiratory hygiene
""")

    st.markdown("---")

# -------------------------
# PDF REPORT GENERATION
# -------------------------
    import os
    os.makedirs("reports", exist_ok=True)
    pdf_file = f"reports/{patient_name}_report.pdf"

    generate_pdf(
        patient_name,
        age,
        gender,
        result,
        display_confidence,
        pdf_file
    )

    with open(pdf_file, "rb") as file:

        st.download_button(
            label="📄 Download PDF Report",
            data=file,
            file_name=f"{patient_name}_report.pdf",
            mime="application/pdf"
        )
    
# -------------------------------
# FOOTER
# -------------------------------
st.markdown("---")

st.caption(
    "Developed using TensorFlow, MobileNetV2, Streamlit and Deep Learning"
)