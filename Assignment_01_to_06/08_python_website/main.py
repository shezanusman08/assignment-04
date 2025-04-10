import streamlit as st
import pandas as pd
import matplotlib.pylab as plt


st.title("Simple Data Dashboard")

upload_file = st.file_uploader("Choose as CSV file",type="csv")

if upload_file is not None:
    df = pd.read_csv(upload_file)

    st.subheader("Data Preview")
    st.write(df.head())
    
    st.subheader("Data Summary")
    st.write(df.describe())

    st.subheader("Data Summary")
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select column to filter by,",columns)
    unique_values = df[selected_column].unique()
    selected_value = st.selectbox("Select value,",unique_values)

    filtered_df = df[df[selected_column] == selected_value]
    st.write(filtered_df)

    st.subheader("Plot Data")
    x_column = st.selectbox("Select x_axis column,",columns)
    y_column = st.selectbox("Select y_axis column,",columns)

    if st.button("Generate Plot"):
        st.line_chart(filtered_df.set_index(x_column)[y_column])
else:
    st.write("Waiting on file uploaded...")