import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.ai_engine import simulate_thought

st.set_page_config(page_title="AI Thought Simulator")

st.title("🧠 AI Thought Simulator")

scenario = st.text_area("Describe your situation", height=150)

mode = st.selectbox(
    "Thinking Style",
    ["Logical", "Risk-Averse", "Growth-Focused"]
)

if st.button("Simulate Thinking"):
    if scenario:
        with st.spinner("Analyzing decision..."):
            result = simulate_thought(scenario, mode)

        st.subheader("🧠 AI Reasoning")
        st.write(result)
