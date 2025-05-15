#Importing necessary packages
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon

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

doesoption = st.selectbox("Which state would you like to select?", [""] + states)

if doesoption:
    st.write("You selected:", doesoption)
    #Reading csv file 
    df = pd.read_csv("C:\\Users\\Callie\\Downloads\\ilidata.csv")

    df["release_date"] = pd.to_datetime(df["release_date"])
    df["release_week"] = df["release_date"].dt.isocalendar().week
    df["release_year"] = df["release_date"].dt.isocalendar().year
    df["Weeks"] = ((df["release_date"] - df["release_date"].min()).dt.days) // 7

    # Streamlit Header
    st.title("Influenza-like Illness Trends Over Time")

    #Making time series
    st.header("Time Series of ILI Percent By Week")
    st.write("""This plot shows the percentage of influenza-like illness and how it has changed week-by-week. Every point on the graph represents the percent of ILI cases
    observed in a given week.""")
    #Making a specific dataframe with plotting data to make it easier to plot
    plotdata = df[['Weeks', 'ili']].rename(columns={'ili': 'Percent ILI'})

    #Making time series plot
    st.line_chart(
    plotdata,
    x='Weeks',
    y='Percent ILI',
    color=['#FF5743']
)

    #Making histogram 
    st.header("Distribution of ILI Percent with Exponential Fit")
    st.write("""
    This histogram shows the distribution of ILI percent values. We then overlaid the estimate (1/lambda) from the exponential density function to look at
    if the ILI values match the exponential distribution. Assuming each ILI value was independently drawn from the same exponential distribution,
    the same mean provides a reasonable estimate of the true parameter, lambda, of the distribution.The density curve helps visualize how likely certain ILI percentages are, given this assumption.
    """)

    #Defining estimate
    ili_data = df["ili"]
    estimate = 1 / ili_data.mean()

    fig, ax = plt.subplots()
    count, bins, _ = ax.hist(ili_data, bins=30, density=True, alpha=0.6, color="skyblue", label="ILI histogram")

    #Adding exponential distribution
    x_values = np.linspace(0, ili_data.max(), 1000)
    ax.plot(x_values, expon.pdf(x_values, scale=estimate), 'r-', lw=2, label=f"Exponential(λ̂={estimate:.2f})")
    ax.set_title("Histogram of ILI Percent with Exponential Fit")
    ax.set_xlabel("ILI Percent")
    ax.set_ylabel("Density")
    ax.legend()
    st.pyplot(fig)
else:
    st.write("Please select a state to begin.")
