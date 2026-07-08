import streamlit as st

from db import get_patients

st.title("📋 Patient History")

patients = get_patients()

st.dataframe(
    patients,
    use_container_width=True
)

