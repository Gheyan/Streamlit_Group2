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
st.dataframe(df)

#Shows information about the data set such as the column, datatype, and other relevant info.
buffer = StringIO()
df.info(buf=buffer)
info_str = buffer.getvalue()  
st.text(info_str)

#Shows the null values present.
st.dataframe(df.isna().sum())

#Shows the generated descriptive statistics of the dataset
st.dataframe(df.describe())