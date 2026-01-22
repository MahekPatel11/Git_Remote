import streamlit as st
st.title("Streamlit Capstone Project")

name = st.text_input("Enter your name:")

age = st.text_input("Enter your current age:")

st.write("This is the extra line.")

if st.button("Submit"):
    st.success(f"Hello {name} of age {age}, welcome to the Streamlit app!")
