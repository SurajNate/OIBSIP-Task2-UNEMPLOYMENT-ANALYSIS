import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import io

st.set_page_config(layout="wide")

# File Paths (Modify these paths based on your local directory)
file1 = 'Unemployment in India.csv'
file2 = 'Unemployment_Rate_upto_11_2020.csv'

# Load datasets directly from the given location
data1 = pd.read_csv(file1)
data2 = pd.read_csv(file2)

# Function to capture the info() output into a string
def capture_info(df):
    buffer = io.StringIO()
    df.info(buf=buffer)
    return buffer.getvalue()

st.title("Unemployment Data Analysis - [@suraj_nate](https://www.instagram.com/suraj_nate/)")
st.write("""
    This is an analysis of unemployment data. The datasets used for this analysis are sourced from Kaggle.\n 
    The first dataset, "Unemployment in India", and the second dataset, "Unemployment Rate up to 11/2020", 
    provide insights into unemployment rates and their trends across different regions and time periods.
    
    You can explore the datasets further on Kaggle:
    - Unemployment in India Datasets [https://www.kaggle.com/datasets/gokulrajkmv/unemployment-in-india]
""")
st.write("<hr>" , unsafe_allow_html=True)
# Create columns for Dataset Info
col1, col2 = st.columns(2)

# Display Dataset 1 Info in the first column
with col1:
    st.subheader("Dataset 1 Info")
    data1_info = capture_info(data1)
    st.text(data1_info)

# Display Dataset 2 Info in the second column
with col2:
    st.subheader("Dataset 2 Info")
    data2_info = capture_info(data2)
    st.text(data2_info)

# Dataset Previews
st.subheader("Dataset 1")
st.dataframe(data1) 
st.subheader("Dataset 2")
st.dataframe(data2) 

# Check for common column and merge
if any(col in data1.columns for col in data2.columns):
    merged_data = pd.merge(data1, data2, on=list(set(data1.columns) & set(data2.columns)), how='outer')
    st.subheader("Merged Dataset Preview")
    st.write(merged_data.head())
else:
    st.write("No common column found. Datasets will be analyzed separately.")

# Missing Values
st.subheader("Missing Values Analysis")
st.write("Dataset 1 Missing Values:")
st.write(data1.isnull().sum())
st.write("Dataset 2 Missing Values:")
st.write(data2.isnull().sum())

# Statistics Summary
st.subheader("Statistics Summary")
st.write("Dataset 1 Statistics:")
st.write(data1.describe())
st.write("Dataset 2 Statistics:")
st.write(data2.describe())

# Visualization: Unemployment Rate Distribution
data1.columns = data1.columns.str.strip()
st.subheader("Unemployment Rate Distribution (Dataset 1)")
fig, ax = plt.subplots(figsize=(10, 6))
sns.histplot(data1['Estimated Unemployment Rate (%)'], bins=20, kde=True, color='blue', ax=ax)
ax.set_title('Unemployment Rate Distribution (Dataset 1)')
ax.set_xlabel('Unemployment Rate (%)')
ax.set_ylabel('Frequency')
st.pyplot(fig)

# Visualization: Average Unemployment Rate by Region (Dataset 2)
data2.columns = data2.columns.str.strip()
if 'Region' in data2.columns and 'Estimated Unemployment Rate (%)' in data2.columns:
    st.subheader("Average Unemployment Rate by Region (Dataset 2)")
    fig, ax = plt.subplots(figsize=(15, 6))
    region_group = data2.groupby('Region')['Estimated Unemployment Rate (%)'].mean()
    region_group.sort_values().plot(kind='bar', color='orange', ax=ax)
    ax.set_title('Average Unemployment Rate by Region (Dataset 2)')
    ax.set_xlabel('Region')
    ax.set_ylabel('Unemployment Rate (%)')
    st.pyplot(fig)

# Footer
st.write("---")
st.markdown('<center><a href="https://www.instagram.com/suraj_nate/" target="_blank" style="color:white;text-decoration:none">&copy; 2025 @suraj_nate All rights reserved.</a></center>', unsafe_allow_html=True)