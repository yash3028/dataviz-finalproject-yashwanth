import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="UK Road Safety Dashboard",
    layout="wide"
)

df = pd.read_csv("./dataset/cleaned_accidents_small.csv", low_memory=False)
df["Date"] = pd.to_datetime(df["Date"])

st.title("UK Road Safety Accident Analysis Dashboard")

st.sidebar.header("Filters")

years = sorted(df["Year"].dropna().unique())

selected_year = st.sidebar.multiselect(
    "Select Year",
    years,
    default=years
)

severity = st.sidebar.multiselect(
    "Select Accident Severity",
    df["Accident_Severity"].dropna().unique(),
    default=df["Accident_Severity"].dropna().unique()
)

weather = st.sidebar.multiselect(
    "Select Weather",
    df["Weather_Conditions"].dropna().unique(),
    default=df["Weather_Conditions"].dropna().unique()
)

filtered_df = df[
    (df["Year"].isin(selected_year)) &
    (df["Accident_Severity"].isin(severity)) &
    (df["Weather_Conditions"].isin(weather))
]

st.subheader("Dataset Summary")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Accidents", len(filtered_df))

col2.metric(
    "Total Casualties",
    int(filtered_df["Number_of_Casualties"].sum())
)

col3.metric(
    "Average Speed Limit",
    round(filtered_df["Speed_limit"].mean(), 2)
)

col4.metric(
    "Vehicles Involved",
    int(filtered_df["Number_of_Vehicles"].sum())
)

st.markdown("---")

st.subheader("Accident Severity Distribution")

severity_df = (
    filtered_df["Accident_Severity"]
    .value_counts()
    .reset_index()
)

severity_df.columns = ["Severity", "Accidents"]

fig = px.bar(
    severity_df,
    x="Severity",
    y="Accidents",
    color="Severity"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Monthly Accident Trend")

monthly = (
    filtered_df.groupby("Month_Number")
    .size()
    .reset_index(name="Accidents")
)

fig = px.line(
    monthly,
    x="Month_Number",
    y="Accidents",
    markers=True
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Road Type Distribution")

road = (
    filtered_df.groupby("Road_Type")
    .size()
    .reset_index(name="Accidents")
)

fig = px.bar(
    road,
    x="Road_Type",
    y="Accidents",
    color="Accidents"
)

fig.update_xaxes(tickangle=45)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Weather Conditions")

weather_df = (
    filtered_df.groupby("Weather_Conditions")
    .size()
    .reset_index(name="Accidents")
)

fig = px.pie(
    weather_df,
    names="Weather_Conditions",
    values="Accidents"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Light Conditions")

light = (
    filtered_df.groupby("Light_Conditions")
    .size()
    .reset_index(name="Accidents")
)

fig = px.bar(
    light,
    x="Light_Conditions",
    y="Accidents",
    color="Accidents"
)

fig.update_xaxes(tickangle=45)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Accidents by Day")

day = (
    filtered_df.groupby("Day")
    .size()
    .reset_index(name="Accidents")
)

order = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

day["Day"] = pd.Categorical(
    day["Day"],
    categories=order,
    ordered=True
)

day = day.sort_values("Day")

fig = px.bar(
    day,
    x="Day",
    y="Accidents",
    color="Accidents"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Time Period Distribution")

time_df = (
    filtered_df.groupby("Time_Period")
    .size()
    .reset_index(name="Accidents")
)

fig = px.pie(
    time_df,
    names="Time_Period",
    values="Accidents"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Vehicle Age Groups")

vehicle = (
    filtered_df.groupby("Vehicle_Age_Group")
    .size()
    .reset_index(name="Vehicles")
)

fig = px.bar(
    vehicle,
    x="Vehicle_Age_Group",
    y="Vehicles",
    color="Vehicles"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Engine Capacity Groups")

engine = (
    filtered_df.groupby("Engine_Group")
    .size()
    .reset_index(name="Vehicles")
)

fig = px.pie(
    engine,
    names="Engine_Group",
    values="Vehicles"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Accident Locations")

fig = px.scatter_mapbox(
    filtered_df.sample(min(5000, len(filtered_df))),
    lat="Latitude",
    lon="Longitude",
    color="Accident_Severity",
    hover_data=["Road_Type", "Weather_Conditions"],
    zoom=5,
    height=600
)

fig.update_layout(mapbox_style="open-street-map")

st.plotly_chart(fig, use_container_width=True)

st.success("Dashboard Loaded Successfully")