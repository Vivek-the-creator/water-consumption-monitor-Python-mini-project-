import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("🏠💧 Water Consumption Monitor")

uploaded_file = st.file_uploader("C:/Users/Vivek/OneDrive/Desktop/Python Mini_Project/meter_data.csv", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file, parse_dates=["time"])
    df["hour"] = df["time"].dt.hour
    df["date"] = df["time"].dt.date

    st.subheader("1. 📈 Daily Consumption (Line Chart)")
    daily = df.groupby("date")["volume"].sum()
    st.line_chart(daily)

    st.subheader("2. 🔥 Hourly Usage by Neighborhood (Heatmap)")
    pivot = df.pivot_table(values="volume", index="hour", columns="location", aggfunc="sum")
    st.write(sns.heatmap(pivot.fillna(0), cmap="Blues", annot=True, fmt=".1f"))
    st.pyplot()

    st.subheader("3. 🧍 Consumption per Household (Bar Chart)")
    household = df.groupby("household_id")["volume"].sum().sort_values(ascending=False)
    st.bar_chart(household)
