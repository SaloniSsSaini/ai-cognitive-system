import streamlit as st

st.title("AI Dashboard")

st.metric("Active Bots", 3)
st.metric("Messages", 120)

st.line_chart([5, 10, 20, 40])