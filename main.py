import streamlit as st
import pandas as pd

# Title of the app
st.title("This is my test on 1-14-2025")

# Simple text message
st.write("Shoot for the moon")

# File uploader
uploaded_file = st.file_uploader("Upload your file", type=["csv", "xlsx"])

if uploaded_file is not None:
    # Check if the uploaded file is a CSV or Excel file
    if uploaded_file.name.endswith("csv"):
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith("xlsx"):
        df = pd.read_excel(uploaded_file)

    # Display the uploaded file's data using Pandas
    st.write("Here is a preview of your uploaded file:")
    st.write(df)

    # You can add more analysis here if needed
    st.write("Data Analysis Example:")
    st.write(df.describe())  # Example of a basic summary of the data
else:
    st.write("Please upload a file to get started.")
