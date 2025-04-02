import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Data Analysis Dashboard")

uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df.head())

    st.write("### Summary Statistics")
    st.write(df.describe())

    st.write("### Histogram")
    column = st.selectbox("Select Column", df.columns)
    plt.figure(figsize=(10, 5))
    sns.histplot(df[column], kde=True)
    st.pyplot(plt)
