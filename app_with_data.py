import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Working with Data in Streamlit")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Preview of Data:")
    st.dataframe(df.head())

if uploaded_file is not None:
    if st.checkbox("Show missing value counts:"):
        st.write(df.isnull().sum())

    if st.checkbox("Drop rows with missing values:"):
        df = df.dropna()
        st.write("Data after dropping missing values:")
        st.dataframe(df.head())
    
if uploaded_file is not None:
    st.subheader("Quick Statistics")
    st.write(df.describe())

if uploaded_file is not None:
    numeric_columns = df.select_dtypes(include="number").columns.tolist()
    if numeric_columns:
        selected_col = st.selectbox("Choose a numeric column for visualization", numeric_columns)

        fig, ax = plt.subplots()
        ax.hist(df[selected_col], bins=20, color='skyblue')
        ax.set_title(f"Histogram of {selected_col}")
        st.pyplot(fig)