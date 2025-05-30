
# 💧 **Water Consumption Monitor** 💧

A **Streamlit-powered dashboard** that visualizes household water consumption from smart meters. Designed to provide actionable insights for **homeowners**, **researchers**, and **urban planners** to promote smart water management.

---

## 🚀 **Features**

- 📥 **Upload smart meter CSV data**
- 📆 **Interactive date filter** (view reports by day or all days together)
- 📈 **Visual Reports**
  - Daily/Hourly consumption (**Line Chart**)
  - Hourly usage by neighborhood (**Heatmap**)
  - Household-wise usage (**Bar Chart**)
- 📄 **Toggle to view raw data**
- ⚡ **Auto-handles multiple days of data**

---

## 📁 **CSV Format Required**

Your uploaded CSV file should have the following format:

```csv
time,location,household_id,volume
01-05-2025 00:00,North,HH001,12.5
01-05-2025 01:00,North,HH002,10.1
...
```

- `time`: timestamp in **DD-MM-YYYY HH:MM** format
- `location`: area or region (e.g., North, South)
- `household_id`: unique identifier for each household
- `volume`: water consumed in liters

---

## 🧠 **How It Works**

➡️ Upload your smart meter CSV file  
➡️ Choose a specific day or view all days  
➡️ Analyze trends using auto-generated charts

---

## ⚙️ **Getting Started**

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/water-consumption-monitor.git
   cd water-consumption-monitor
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Launch the app**
   ```bash
   streamlit run app.py
   ```

4. Upload your CSV and start exploring the data!

---

## 📊 **Tech Stack**

- 🐍 Python
- 🌊 Streamlit
- 📊 Pandas
- 🎨 Seaborn
- 📈 Matplotlib

---

## 🏙️ **Use Cases**

- Smart city water usage dashboards
- Personal or municipal household monitoring
- Water conservation research
- Infrastructure planning

---

## 📜 **License**

This project is licensed under the **MIT License**.

---

## 🙌 **Contributions Welcome!**

Feel free to:
- 💡 Suggest new features
- 🐞 Report bugs
- 🔧 Open pull requests

---

## 📬 *Contact*

Made with ❤ by Vivek K K
📧 vivek.kk2024aiml@sece.ac.in
🌐 [GitHub](https://github.com/Vivek-the-creator)

---
