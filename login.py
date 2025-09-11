import streamlit as st

# Hardcoded username & password
USERNAME = "admin"
PASSWORD = "1234"

st.title("🔐 Login Page")

# Input fields
username = st.text_input("Username")
password = st.text_input("Password", type="password")

# Login button
if st.button("Login"):
    if username == USERNAME and password == PASSWORD:
        st.success("✅ Login Successful!")
    else:
        st.error("❌ Invalid Username or Password")
