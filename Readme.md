# 🦈 Shark Attack Data Cleaning with Pandas

## 📌 Objective
This project focuses on cleaning and visualizing real-world data on global shark attacks. Using `pandas`, `numpy`, and `plotly`, we transform a raw Excel file into a clean, analysis-ready dataset with powerful interactive visualizations.

## 🗂 Project Structure


## 🧼 Cleaning Steps Performed

- Dropped irrelevant or unnamed columns
- Standardized column names and values (e.g. country, fatal, activity)
- Parsed and validated dates
- Extracted year from date
- Imputed missing values for `Age` using numeric replacements and mean fill
- Removed duplicates and blank rows
- Unified country names for consistent analysis

## 📊 Visualizations Created

Using `plotly.express`, we created:

1. **Pie Chart** – Fatal vs Non-Fatal Attacks  
2. **Bar Chart** – Top 5 Countries by Shark Attacks  
3. **Line Plot** – Attacks Over the Years  
4. **Bar Chart** – Top 10 Activities Linked to Shark Attacks  
5. **Sunburst Chart** – Country → Activity → Fatality Breakdown  

> These plots offer insights into the **risk areas**, **common activities**, and **fatality trends** over time.

## ▶️ How to Run This Project

1. Clone the repo:
   ```bash
   git clone https://github.com/YOUR_USERNAME/data-cleaning-pandas.git
