import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

# تنظیمات صفحه
st.set_page_config(page_title="Dashboard", layout="wide")

# ارتباط با پایگاه داده
conn = sqlite3.connect("data.db")  # جایگزین کن با نام دیتابیس خودت
query = "SELECT * FROM production_data"  # جدول واقعی‌ات را جایگزین کن
df = pd.read_sql(query, conn)

# نمایش شاخص‌های کلیدی عملکرد (KPIs)
col1, col2, col3 = st.columns(3)
col1.metric("Total Production", df["production"].sum())
col2.metric("Average Rate", round(df["rate"].mean(), 2))
col3.metric("Total Errors", df["errors"].sum())

# **📊 نمودار تولیدات ماهانه**
fig = px.line(df, x="date", y="production", title="Production Over Time")
st.plotly_chart(fig, use_container_width=True)

# **📊 نمودار درصد خرابی‌ها**
fig2 = px.pie(df, names="error_type", values="errors", title="Error Distribution")
st.plotly_chart(fig2, use_container_width=True)

conn.close()
