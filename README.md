# 📡 SensorShare – Community IoT Data Uploader

SensorShare is a lightweight community-driven web app built using **Streamlit** and **SQLite**, allowing users to upload and visualize IoT sensor data such as temperature, humidity, and air quality.

---

## 🛠️ Features

- 📥 **Data Upload Form:**  
  Users can submit sensor readings with type, value, location, and date.

- 📊 **Dashboard:**  
  View all uploaded sensor data in tabular format and filter by sensor type. Supports basic line chart visualization over time.

- 🗺️ **Map Visualization:**  
  If GPS coordinates are included, the app can plot data on a map.

---

## 🚀 Technologies Used

- **Python 3**
- **Streamlit**
- **Pandas**
- **SQLAlchemy**
- **SQLite**

---

Run the app

streamlit run app.py
📊 Dashboard Features

View data filtered by sensor type

See the latest 100 records

Line chart of sensor values over time

Map rendering if latitude and longitude columns are available

❤️ Made For

Made with ❤️ for community-powered sensing 🌍
Simple, accessible environmental data collection for all.

⚠️ Notes

Data is stored locally in sensor_data.db.

To persist across sessions or scale, consider integrating PostgreSQL or a cloud database.
