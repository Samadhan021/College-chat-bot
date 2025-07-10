import streamlit as st
import pandas as pd

# Load sample data from root-level file
data = pd.read_csv("sample_faq.csv")
st.title("🎓 College Helpdesk Chatbot")

query = st.text_input("Ask your question:")

if query:
    response = "Sorry, I don't understand your query yet."
    if "exam" in query.lower():
        response = data[data.intent == "exam_schedule"].response.values[0]
    elif "hod" in query.lower():
        response = data[data.intent == "faculty_contact"].response.values[0]
    st.success(response)
