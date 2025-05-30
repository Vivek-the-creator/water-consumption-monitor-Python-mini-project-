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

    # Sidebar date selection with "All Days" option
    unique_dates = sorted(df["date"].unique())
    date_options = ["All Days"] + [str(date) for date in unique_dates]
    selected_option = st.sidebar.selectbox("Select a date (or view all)", date_options)

    # Toggle to show raw data
    if st.checkbox("Show Raw Data"):
        st.subheader("📄 Raw Data")
        st.dataframe(df)

    # Filter data
    if selected_option == "All Days":
        filtered_df = df
        title_suffix = " (All Days)"
    else:
        selected_date = pd.to_datetime(selected_option).date()
        filtered_df = df[df["date"] == selected_date]
        title_suffix = f" ({selected_date.strftime('%d-%m-%Y')})"

    st.subheader(f"📊 Water Consumption Report{title_suffix}")

    # 1. Line Chart (Hourly or Daily)
    if selected_option == "All Days":
        st.markdown("**1. Daily Total Consumption (Line Chart)**")
        daily = filtered_df.groupby("date")["volume"].sum()
        st.line_chart(daily)
    else:
        st.markdown("**1. Hourly Consumption (Line Chart)**")
        hourly = filtered_df.groupby("hour")["volume"].sum()
        st.line_chart(hourly)

    # 2. Heatmap (Hourly Usage by Location)
    st.markdown("**2. Hourly Usage by Neighborhood (Heatmap)**")
    pivot = filtered_df.pivot_table(values="volume", index="hour", columns="location", aggfunc="sum")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(pivot.fillna(0), cmap="Blues", annot=True, fmt=".1f", ax=ax)
    st.pyplot(fig)

    # 3. Bar Chart (Household Usage)
    st.markdown("**3. Household Consumption (Bar Chart)**")
    household = filtered_df.groupby("household_id")["volume"].sum().sort_values(ascending=False)
    st.bar_chart(household)

else:
    st.info("Please upload your smart meter CSV file to see the analysis.")
