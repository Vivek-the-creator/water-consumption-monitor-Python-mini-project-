```
# 💧 Water Consumption Monitor 💧

A Streamlit-based dashboard to visualize and analyze household water consumption data from smart meters. This tool helps users, researchers, and city planners understand usage patterns and optimize water management.

## 🚀 Features

- 📥 Upload smart meter CSV data
- 📆 View daily reports with a sidebar date selector
- 📊 Visualize:
  - Daily or hourly water usage (Line Chart)
  - Hourly usage by neighborhood (Heatmap)
  - Household-level consumption (Bar Chart)
- 📄 View raw data on toggle
- 📅 Compare data across all days or view specific day’s report


## 📁 Sample CSV Format

Make sure your CSV follows this structure:

time,location,household_id,volume  
01-05-2025 00:00,North,HH001,12.5  
01-05-2025 01:00,North,HH002,10.1  
...  

- `time`: timestamp (e.g., `01-05-2025 00:00`)
- `location`: region name (e.g., North, South)
- `household_id`: unique ID for each household
- `volume`: water consumed (liters)

## ⚙️ How to Run

1. Clone this repo:
   git clone https://github.com/your-username/water-consumption-monitor.git
   cd water-consumption-monitor

2. Install dependencies:
   pip install -r requirements.txt

3. Run the app:
   streamlit run app.py

4. Upload your CSV and explore the insights!

## 🧰 Tech Stack

- Python
- Streamlit
- Pandas
- Seaborn
- Matplotlib

## 📈 Use Cases

- Smart city water analytics
- Household water monitoring
- Environmental research
- Urban infrastructure planning


📬 Feel free to contribute, raise issues, or suggest new features!
```
