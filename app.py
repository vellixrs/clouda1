import streamlit as st
import pandas as pd

st.title("Qahwa Corner Sales Dashboard")

df = pd.read_csv("cafe_sales.csv")

branch = st.selectbox(
    "Select Branch",
    sorted(df["branch"].unique())
)

filtered = df[df["branch"] == branch]

st.metric(
    "Total Revenue (SAR)",
    round(filtered["total_sar"].sum(), 2)
)

revenue_product = (
    filtered.groupby("product")["total_sar"]
    .sum()
    .sort_values(ascending=False)
)

st.subheader("Revenue by Product")
st.bar_chart(revenue_product)
