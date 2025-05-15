#Importing necessary packages
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon

#Make list of states to be added to the drop down menu
states = [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado",
    "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho",
    "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine",
    "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi",
    "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey",
    "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio",
    "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina",
    "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia",
    "Washington", "West Virginia", "Wisconsin", "Wyoming"
]

#Make option box
doesoption = st.selectbox("Which state would you like to select?", [""] + states)
#Use selection to make sure the code runs after the user picks the state
if doesoption:
    st.write("You selected:", doesoption)
#Reading csv file 
    df = pd.read_csv("ilidata.csv")
#Changing the date from release date to weeks
    df["release_date"] = pd.to_datetime(df["release_date"])
    df["release_week"] = df["release_date"].dt.isocalendar().week
    df["release_year"] = df["release_date"].dt.isocalendar().year
    df["Weeks"] = ((df["release_date"] - df["release_date"].min()).dt.days) // 7

#Add title
    st.title("Influenza-like Illness Trends Over Time")

#Making time series graph with a label and description
    st.header("Time Series of ILI Percent By Week")
    st.write("""This plot shows the percentage of influenza-like illness and how it has changed week-by-week. Every point on the graph represents the percent of ILI cases
    observed in a given week. The graph shows us that about every year (roughly 52 weeks) the percentage of influenza like illness spikes then drops shortly after. This is important for public health officials and researchers to be
    able to visualize because it allows them to predict and prepare for when influenza like illness will spike again in the future.""")
    #Making a specific dataframe with plotting data to make it easier to plot
    plotdata = df[['Weeks', 'ili']].rename(columns={'ili': 'Percent ILI'})
    st.line_chart(
    plotdata,
    x='Weeks',
    y='Percent ILI',
    color=['#FF5743']
)

#Histogram labels and description
    st.header("Distribution of ILI Percent with Exponential Fit")
    st.write("""
    This histogram shows the distribution of ILI percent values. The estimate (1/lambda) from the exponential density function was then overlaid to look at
    if the ILI values match the exponential distribution. If it is assumed each ILI value was independently drawn from the same exponential distribution,
    the same mean provides a reasonable estimate of the true parameter, lambda, of the distribution.
    """)

#Defining the estimate
    ili_data = df["ili"]
    estimate = 1 / ili_data.mean()

#Making the histogram
    fig, ax = plt.subplots()
    count, bins, _ = ax.hist(ili_data, bins=30, density=True, alpha=0.6, color="skyblue", label="ILI histogram")

#Adding exponential distribution overlaid
    x_values = np.linspace(0, ili_data.max(), 1000)
    ax.plot(x_values, expon.pdf(x_values, scale=estimate), 'r-', lw=2, label=f"Exponential(λ̂={estimate:.2f})")
    ax.set_title("Histogram of ILI Percent with Exponential Fit")
    ax.set_xlabel("ILI Percent")
    ax.set_ylabel("Density")
    ax.legend()
    st.pyplot(fig)
else:
    st.write("Please select a state to begin.")
