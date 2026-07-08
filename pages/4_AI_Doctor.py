import streamlit as st

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="AI Doctor Assistant",
    page_icon="🤖",
    layout="wide"
)

# -----------------------------
# CUSTOM CSS
# -----------------------------
st.markdown("""
<style>

.main {
    background: linear-gradient(135deg,#f5f7fa,#e4ecfb);
}

.chat-title {
    text-align:center;
    font-size:40px;
    font-weight:bold;
    color:#0A66C2;
}

.chat-subtitle {
    text-align:center;
    color:gray;
    font-size:18px;
}

.info-box {
    padding:15px;
    border-radius:15px;
    background:#ffffff;
    box-shadow:0px 4px 12px rgba(0,0,0,0.08);
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# HEADER
# -----------------------------
st.markdown(
    '<p class="chat-title">🤖 AI Doctor Assistant</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="chat-subtitle">Your Virtual Medical Information Assistant</p>',
    unsafe_allow_html=True
)

st.markdown("---")

st.info(
    "⚠️ This AI provides educational information only and does not replace professional medical advice."
)

# -----------------------------
# QUICK QUESTIONS
# -----------------------------
st.subheader("⚡ Quick Questions")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🫁 What is Pneumonia?"):
        st.session_state.quick_question = "what is pneumonia"

with col2:
    if st.button("🌡️ Fever"):
        st.session_state.quick_question = "fever"

with col3:
    if st.button("💪 Healthy Lifestyle"):
        st.session_state.quick_question = "healthy lifestyle"

# -----------------------------
# CHAT HISTORY
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# -----------------------------
# INPUT
# -----------------------------
query = st.chat_input(
    "Ask your medical question..."
)

if (
    not query
    and "quick_question" in st.session_state
):
    query = st.session_state.quick_question
    del st.session_state.quick_question

# -----------------------------
# AI RESPONSE
# -----------------------------
if query:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": query
        }
    )

    with st.chat_message("user"):
        st.markdown(query)

    q = query.lower()

    # ------------------------------------------------
    # KNOWLEDGE BASE
    # ------------------------------------------------

    if "pneumonia" in q:

        answer = """
# 🫁 Pneumonia

Pneumonia is an infection that inflames the air sacs in one or both lungs.

### Common Symptoms

✔ Fever

✔ Cough

✔ Fatigue

✔ Chills

✔ Chest Pain

✔ Shortness of Breath

### Treatment

Treatment depends on severity and cause.

Consult a healthcare professional for diagnosis and treatment.
"""

    elif "symptom" in q:

        answer = """
# 🤒 Common Symptoms

### Respiratory Symptoms

✔ Fever

✔ Cough

✔ Fatigue

✔ Breathing Difficulty

✔ Chills

✔ Chest Discomfort

Persistent symptoms should be medically evaluated.
"""

    elif "fever" in q:

        answer = """
# 🌡️ Fever

Fever is often the body's response to infection.

### Recommendations

✔ Stay hydrated

✔ Rest adequately

✔ Monitor temperature

✔ Seek medical care if fever persists
"""

    elif "cough" in q:

        answer = """
# 😷 Cough

Common causes:

• Cold

• Flu

• Pneumonia

• Asthma

• Allergies

Persistent coughing requires medical evaluation.
"""

    elif "chest pain" in q:

        answer = """
# ❤️ Chest Pain

Possible causes:

• Lung infection

• Muscle strain

• Heart-related conditions

Severe chest pain requires immediate medical attention.
"""

    elif (
        "breathing" in q
        or "shortness of breath" in q
    ):

        answer = """
# 🫁 Breathing Difficulty

Possible causes:

• Pneumonia

• Asthma

• COPD

• Respiratory infections

Please seek medical evaluation if symptoms are severe.
"""

    elif (
        "can't breathe" in q
        or "cannot breathe" in q
        or "blood cough" in q
        or "unconscious" in q
        or "severe chest pain" in q
    ):

        answer = """
# 🚨 Emergency Warning

Your symptoms may require immediate medical attention.

Please contact emergency services or visit the nearest hospital immediately.

Do not rely solely on AI advice.
"""

    elif (
        "prevent" in q
        or "prevention" in q
    ):

        answer = """
# 🛡️ Prevention Tips

✔ Wash hands frequently

✔ Avoid smoking

✔ Exercise regularly

✔ Maintain healthy nutrition

✔ Get vaccinations when recommended
"""

    elif (
        "healthy lifestyle" in q
        or "lifestyle" in q
        or "healthy" in q
    ):

        answer = """
# 💪 Healthy Lifestyle

✔ Exercise regularly

✔ Eat balanced meals

✔ Stay hydrated

✔ Sleep 7–9 hours

✔ Avoid smoking

✔ Manage stress effectively
"""

    elif (
        "diet" in q
        or "food" in q
    ):

        answer = """
# 🥗 Healthy Diet

### Include

✔ Fruits

✔ Vegetables

✔ Whole grains

✔ Lean proteins

### Limit

❌ Excess sugar

❌ Excess processed food
"""

    elif (
        "water" in q
        or "hydration" in q
    ):

        answer = """
# 💧 Hydration

Proper hydration supports:

✔ Immune health

✔ Circulation

✔ Recovery

✔ Organ function

Aim for adequate daily water intake.
"""

    elif "exercise" in q:

        answer = """
# 🏃 Exercise

Benefits:

✔ Better lung health

✔ Improved immunity

✔ Stronger heart

✔ Weight management

Aim for at least 150 minutes weekly.
"""

    elif "sleep" in q:

        answer = """
# 😴 Sleep

Adults generally require:

### 7–9 Hours Daily

Benefits:

✔ Better recovery

✔ Stronger immunity

✔ Improved concentration
"""

    elif "stress" in q:

        answer = """
# 🧠 Stress Management

Helpful methods:

✔ Meditation

✔ Deep breathing

✔ Exercise

✔ Quality sleep

✔ Social interaction
"""

    elif "confidence" in q:

        answer = """
# 📊 AI Confidence Score

The confidence score indicates how certain the AI model is about its prediction.

Higher percentages indicate stronger confidence.

Always verify results with a healthcare professional.
"""

    elif (
        "xray" in q
        or "x-ray" in q
    ):

        answer = """
# 🩻 Chest X-Ray

Chest X-rays help identify:

✔ Pneumonia

✔ Lung infections

✔ Fluid buildup

✔ Other respiratory abnormalities

Your AI system analyzes X-ray patterns to assist diagnosis.
"""

    elif (
        "how does this ai work" in q
        or "how does ai work" in q
    ):

        answer = """
# 🤖 How This AI Works

1. Upload Chest X-Ray

2. Image is resized

3. MobileNetV2 extracts features

4. Deep Learning model analyzes image

5. Prediction is generated

6. Confidence score is calculated

The system supports but does not replace medical diagnosis.
"""

    else:

        answer = """
# 🤖 AI Doctor Assistant

I can answer questions about:

🫁 Pneumonia

🌡️ Fever

😷 Cough

❤️ Chest Pain

💧 Hydration

💪 Healthy Lifestyle

🏃 Exercise

😴 Sleep

🩻 X-Ray Analysis

📊 Confidence Scores

Try asking:

• What is pneumonia?

• I have fever

• Explain chest X-ray

• Healthy lifestyle tips
"""

    with st.chat_message("assistant"):
        st.markdown(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.title("🩺 AI Doctor")

st.sidebar.success(
    "Available Topics"
)

st.sidebar.markdown("""
✔ Pneumonia

✔ Fever

✔ Cough

✔ Chest Pain

✔ X-Ray

✔ Exercise

✔ Sleep

✔ Healthy Lifestyle

✔ Prevention

✔ Hydration
""")

st.sidebar.markdown("---")

if st.sidebar.button("🗑 Clear Chat"):

    st.session_state.messages = []

    st.rerun()