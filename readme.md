# UK Road Safety Accident Analysis

## Live Demo

Streamlit App:
https://3wfprym9pvxsgurkefg8tc.streamlit.app/

## GitHub Repository

https://github.com/yash3028/dataviz-finalproject-yashwanth

## Project Overview

This project analyzes UK Road Safety Accident data using Python, Pandas, Plotly, and Streamlit. The objective is to identify accident patterns, understand factors contributing to accidents, and build an interactive dashboard for data visualization.

---

## Dataset

Dataset:
UK Road Safety: Traffic Accidents and Vehicles

Source:
https://www.kaggle.com/datasets/tsiaras/uk-road-safety-accidents-and-vehicles

Files Used

- Accident_Information.csv
- Vehicle_Information.csv

---

## Technologies Used

- Python
- Pandas
- NumPy
- Plotly
- Streamlit

---

## Project Structure

```
Road_Accident_Analysis/

│
├── dataset/
│   ├── Accident_Information.csv
│   ├── Vehicle_Information.csv
│   ├── merged_accident_vehicle.csv
│   └── cleaned_accidents.csv
│
├── 01_Data_Loading.ipynb
├── 02_Data_Cleaning.ipynb
├── 03_EDA.ipynb
├── 04_Analytical_Questions.ipynb
├── app.py
├── requirements.txt
└── README.md
```

---

## Data Processing

The project consists of four major stages.

### Data Loading

- Load accident dataset
- Load vehicle dataset
- Merge both datasets using Accident_Index

### Data Cleaning

- Handle missing values
- Remove duplicate records
- Convert date and time columns
- Create new features

### Exploratory Data Analysis

- Accident Severity
- Road Type
- Weather Conditions
- Light Conditions
- Monthly Trend
- Daily Trend
- Vehicle Age
- Engine Capacity

### Dashboard

Interactive dashboard created using Streamlit with filters for:

- Year
- Accident Severity
- Weather Conditions

Dashboard displays:

- KPI Cards
- Bar Charts
- Pie Charts
- Line Charts
- Scatter Map

---

## Analytical Questions

The project answers questions including:

- Which accident severity occurs most frequently?
- Which road type has the highest number of accidents?
- Which weather condition contributes to more accidents?
- Which light condition has the highest accident rate?
- Which months record the highest accidents?
- Which weekdays record more accidents?
- Which time period experiences more accidents?
- Which speed limits experience more accidents?
- What vehicle age group is involved most?
- Which engine capacity group appears most frequently?

---

## Run the Dashboard

Install dependencies

```
pip install -r requirements.txt
```

Run Streamlit

```
streamlit run app.py
```

---

## Conclusion

The dashboard provides insights into accident severity, road conditions, weather effects, time patterns, vehicle characteristics, and geographical distribution of accidents. These insights can support road safety planning and policy decisions.
