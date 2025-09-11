import streamlit as st
import pandas as pd
import csv
from pathlib import Path

# Create or load data
def init_data():
    if not Path('data.csv').exists():
        df = pd.DataFrame({
            'name': ['John', 'Jane'],
            'email': ['john@email.com', 'jane@email.com'],
            'score': [85, 92]
        })
        df.to_csv('data.csv', index=False)
    return pd.read_csv('data.csv')

# Streamlit app
st.title("Simple Data App")

# Load data
df = init_data()
st.dataframe(df)

# Add new data
with st.form("add_data"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    score = st.number_input("Score", min_value=0, max_value=100)
    
    if st.form_submit_button("Add Entry"):
        new_data = pd.DataFrame([[name, email, score]], 
                              columns=['name', 'email', 'score'])
        new_data.to_csv('data.csv', mode
