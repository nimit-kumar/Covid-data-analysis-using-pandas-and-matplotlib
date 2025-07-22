# COVID-19 Data Analysis Project

This project analyzes the **latest COVID-19 dataset** on a country-wise level using **Pandas** for data manipulation and **Matplotlib** for visualization. The dataset includes confirmed cases, deaths, recoveries, active cases, and other metrics across 187 countries.

---

## 📁 Dataset

- **File Name**: `country_wise_latest.csv`
- **Source**: WHO/CSSE (Can be replaced with a live or updated version)
- **Fields Include**:
  - Country/Region
  - Confirmed
  - Deaths
  - Recovered
  - Active
  - New cases, new deaths, new recovered
  - WHO Region
  - Death/Recovery rates
  - Weekly changes

---

## 🔧 Technologies Used

- Python 3.x
- Pandas
- Matplotlib

---

## 📊 Analysis Performed

### 🔹 Basic Statistics
- Total Confirmed Cases
- Total Deaths
- Total Recovered
- Total Active Cases (Calculated)

### 🔹 Top 5 Countries Analysis
- Top 5 by Confirmed cases
- Top 5 by Deaths
- Top 5 by Recovered
- Top 5 by Active Cases

### 🔹 Visualizations
- 📊 **Bar Chart**: Top 5 countries with highest active cases
- 🥧 **Pie Chart**: Confirmed cases distribution by WHO region
- 📥 Charts saved as:
  - `top5_active_cases.png`
  - `Region_data.png`

### 🔹 Advanced Filtering
- Countries with **zero deaths**
- **Recovery Rate** by country
- **Death Rate** by country

---

## 📂 How to Run

1. Install the required libraries (if not already):
   ```bash
   pip install pandas matplotlib
