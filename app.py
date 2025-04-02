import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title
st.title("Data Analysis Dashboard")

# Upload CSV
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df.head())

    # Basic Statistics
    st.write("### Summary Statistics")
    st.write(df.describe())

    # Data Visualization
    st.write("### Histogram")
    column = st.selectbox("Select Column", df.columns)
    plt.figure(figsize=(10, 5))
    sns.histplot(df[column], kde=True)
    st.pyplot(plt)
