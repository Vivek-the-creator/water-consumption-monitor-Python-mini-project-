import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("🏠💧 Water Consumption Monitor")

uploaded_file = st.file_uploader("Upload Smart Meter CSV", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file, parse_dates=["time"], dayfirst=True)
    df["hour"] = df["time"].dt.hour
    df["date"] = df["time"].dt.date

    # Sidebar date selection
    unique_dates = sorted(df["date"].unique())
    selected_date = st.sidebar.date_input("Select a date to view report", unique_dates[0], min_value=min(unique_dates), max_value=max(unique_dates))

    # Toggle to show raw data
    if st.checkbox("Show Raw Data"):
        st.subheader("📄 Raw Data")
        st.dataframe(df)

    # Filter data based on selected date
    daily_df = df[df["date"] == selected_date]

    st.subheader(f"📊 Water Consumption Report for {selected_date.strftime('%d-%m-%Y')}")

    # 1. Line Chart (Hourly Usage)
    st.markdown("**1. Hourly Consumption (Line Chart)**")
    hourly = daily_df.groupby("hour")["volume"].sum()
    st.line_chart(hourly)

    # 2. Heatmap (Hourly Usage by Location)
    st.markdown("**2. Hourly Usage by Neighborhood (Heatmap)**")
    pivot = daily_df.pivot_table(values="volume", index="hour", columns="location", aggfunc="sum")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(pivot.fillna(0), cmap="Blues", annot=True, fmt=".1f", ax=ax)
    st.pyplot(fig)

    # 3. Bar Chart (Household Usage)
    st.markdown("**3. Household Consumption (Bar Chart)**")
    household = daily_df.groupby("household_id")["volume"].sum().sort_values(ascending=False)
    st.bar_chart(household)

else:
    st.info("Please upload your smart meter CSV file to see the analysis.")
