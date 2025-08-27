import datetime
import os

import pandas as pd
import streamlit as st
from sqlalchemy import Column, Date, Float, MetaData, String, Table, create_engine

# ----------------- Setup -----------------

# Print where the DB is being created
st.text(f"📁 Working directory: {os.getcwd()}")

# SQLite database setup
DB_PATH = "sqlite:///sensor_data.db"
engine = create_engine(DB_PATH, echo=False)
metadata = MetaData()

# Define the table schema
sensor_table = Table(
    "sensors", metadata,
    Column("sensor_type", String),
    Column("value", Float),
    Column("location", String),
    Column("timestamp", Date)
)

# Create the table if it doesn't exist
metadata.create_all(engine)

st.set_page_config(page_title="SensorShare", layout="centered")
st.title("📡 SensorShare – Community IoT Data Uploader")

# ----------------- Data Form -----------------

st.subheader("📥 Submit Your Sensor Reading")

with st.form("sensor_form"):
    sensor_type = st.selectbox("Sensor Type", ["Temperature", "Humidity", "Air Quality", "Soil Moisture", "Other"])
    value = st.number_input("Sensor Value", step=0.1, format="%.2f")
    location = st.text_input("Location (e.g., City or GPS)")
    timestamp = st.date_input("Date", value=datetime.date.today())
    submit = st.form_submit_button("Upload Reading")

    if submit:
        try:
            with engine.begin() as conn:  # begin() ensures the transaction is committed
                conn.execute(sensor_table.insert().values(
                    sensor_type=sensor_type,
                    value=value,
                    location=location,
                    timestamp=timestamp
                ))
            st.success(f"✅ Uploaded: {sensor_type} = {value} at {location} on {timestamp}")
        except Exception as e:
            st.error(f"❌ Error saving to database: {e}")

# ----------------- Dashboard -----------------

st.subheader("📊 Community Data Dashboard")

try:
    with engine.connect() as conn:
        result = conn.execute(sensor_table.select())
        rows = result.fetchall()
        columns = result.keys()

    df = pd.DataFrame(rows, columns=columns)

    if not df.empty:
        selected_type = st.selectbox("Filter by Sensor Type", ["All"] + sorted(df["sensor_type"].unique()))
        if selected_type != "All":
            df = df[df["sensor_type"] == selected_type]

        st.write(f"Showing {len(df)} records")
        st.dataframe(df.tail(100))

        if selected_type != "All":
            chart_data = df.sort_values("timestamp")
            st.line_chart(chart_data.set_index("timestamp")["value"])
    else:
        st.info("No sensor data available yet.")
except Exception as e:
    st.error(f"❌ Failed to load data: {e}")

# ----------------- Footer -----------------

st.markdown("---")
st.markdown("Made with ❤️ for community-powered sensing 🌍")

st.warning(f"Writing to: {os.path.abspath('sensor_data.db')}")
if "latitude" in df.columns and "longitude" in df.columns:
    st.map(df[['latitude', 'longitude']])