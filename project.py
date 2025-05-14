import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv("ilidata.csv")

option = st.selectbox(
    "Which state would you like to select?",
    ("Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"),
)
st.write("You selected:", option)

state_df = df[df['state'] == option].sort_values(by='epiweek').reset_index(drop=True)
state_df['Weeks'] = range(len(state_df))

plotdata = state_df[['Weeks', 'ili']].rename(columns={'ili': 'Percent ILI'})

#Making plot
st.line_chart(
    plotdata,
    x='Weeks',
    y='Percent ILI',
    color=['#FF5733']
)
