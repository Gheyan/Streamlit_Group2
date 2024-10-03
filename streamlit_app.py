# Imported libraries
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import altair as alt
from wordcloud import WordCloud
from mpl_toolkits.mplot3d import Axes3D
from io import StringIO


#General Information About The Group
st.write("CSS145_BM4_1Q2425")
st.title("Group 2: ")

st.markdown("""
- Aleah Balagao
- Sean Chester Cabantog
- John Daniel Garina
- Gian Carlo Mateo
- Felipe Panugan
""")

#imported datasheet

#The variable df is set to the read csv dataset
df = pd.read_csv("laptop_price - dataset.csv")

#this shows the datasheet
st.markdown("### Laptop_Price DataSheet")
st.dataframe(df)

#Shows information about the data set such as the column, datatype, and other relevant info.
st.markdown("### Info About Datasheet")
buffer = StringIO()
df.info(buf=buffer)
info_str = buffer.getvalue()  
st.text(info_str)

#Shows the null values present.
st.markdown("### Present Null Values in the DataSheet")
st.dataframe(df.isna().sum())

#Shows the generated descriptive statistics of the dataset
st.markdown("### DataSheet Descriptive Statistics")
st.dataframe(df.describe())

#Shows general information about how we used the barchart
st.title("Bar Chart")
st.markdown("Used to accomplish the following: ")
st.markdown("""
1. Show the different amount of unique laptops per company
2. Identify the company with the most amount of unique laptops
3. Identify the company with the least amount of unique laptops
""")

#Creates the appropriate Bar Graph to show the different companies that are selling their respective number of unique laptop devices
def barchart():
  company_count = df['Company'].value_counts()
  plt.bar(company_count.index, company_count.values)
  plt.xticks(rotation=75)
  plt.title("Companies and Their Number of Unique Laptop/s")
  plt.xlabel("Company")
  plt.ylabel("Number of Unique Laptops")
  #syntax to show the chart on streamlit
  st.pyplot(plt)
  #This clears the elements of the previous graph, a must properly run graphs
  plt.clf()

barchart()