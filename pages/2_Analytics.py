import streamlit as st
import pandas as pd
import plotly.express as px

from db import get_patients

st.set_page_config(
    page_title="Analytics",
    page_icon="📊"
)

st.title("📊 Medical Analytics Dashboard")

data = get_patients()

if len(data) == 0:
    st.warning("No patient records found.")
    st.stop()

df = pd.DataFrame(
    data,
    columns=[
        "ID",
        "Name",
        "Age",
        "Gender",
        "Diagnosis",
        "Confidence"
    ]
)

# -----------------------
# KPI CARDS
# -----------------------

total_patients = len(df)

pneumonia_cases = len(
    df[df["Diagnosis"] == "Pneumonia"]
)

normal_cases = len(
    df[df["Diagnosis"] == "Normal"]
)

avg_confidence = round(
    df["Confidence"].mean(),
    2
)

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Patients",
    total_patients
)

col2.metric(
    "Pneumonia",
    pneumonia_cases
)

col3.metric(
    "Normal",
    normal_cases
)

col4.metric(
    "Avg Confidence",
    f"{avg_confidence}%"
)

st.divider()

# -----------------------
# DIAGNOSIS CHART
# -----------------------

fig1 = px.pie(
    df,
    names="Diagnosis",
    title="Diagnosis Distribution"
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

# -----------------------
# GENDER CHART
# -----------------------

fig2 = px.histogram(
    df,
    x="Gender",
    title="Gender Distribution"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# -----------------------
# AGE CHART
# -----------------------

fig3 = px.histogram(
    df,
    x="Age",
    nbins=10,
    title="Age Distribution"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)