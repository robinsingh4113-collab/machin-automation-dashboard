"""
app.py
-------
Client Service and Project Performance Analysis Dashboard
Company: Machin Automation (OPC) Private Limited, Kaithal

This Streamlit app reads client/project data from sample_dataset.csv
and displays an interactive dashboard with KPIs, charts, filters,
a data table, and auto-generated key insights.

To run locally:   streamlit run app.py
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime

# =========================================================
# 1. PAGE CONFIGURATION
# =========================================================
st.set_page_config(
    page_title="Machin Automation - Client & Project Dashboard",
    page_icon="📊",
    layout="wide"
)

# =========================================================
# 2. LOAD DATA
# =========================================================
@st.cache_data  # caches the data so the app loads faster on repeat runs
def load_data():
    df = pd.read_csv("sample_dataset.csv")
    df["Date"] = pd.to_datetime(df["Date"])          # convert text date to real date type
    df["Month"] = df["Date"].dt.to_period("M").astype(str)  # used for monthly trend chart
    return df

df = load_data()

# =========================================================
# 3. HEADER / TITLE SECTION
# =========================================================
st.title("📊 Client Service and Project Performance Analysis Dashboard")
st.subheader("Machin Automation (OPC) Private Limited, Kaithal")

st.markdown("""
This dashboard analyzes client service requests and project performance
for Machin Automation (OPC) Private Limited — a Kaithal-based company offering
computer, automation, and IT support services. It tracks project status,
revenue, payments, and client trends to support data-driven business decisions.
""")

st.markdown("---")

# =========================================================
# 4. SIDEBAR FILTERS
# =========================================================
st.sidebar.header("🔍 Filter Data")

# City filter
city_options = sorted(df["City"].unique())
selected_cities = st.sidebar.multiselect("Select City", options=city_options, default=city_options)

# Service type filter
service_options = sorted(df["Service_Type"].unique())
selected_services = st.sidebar.multiselect("Select Service Type", options=service_options, default=service_options)

# Status filter
status_options = sorted(df["Status"].unique())
selected_status = st.sidebar.multiselect("Select Project Status", options=status_options, default=status_options)

# Payment status filter
payment_options = sorted(df["Payment_Status"].unique())
selected_payment = st.sidebar.multiselect("Select Payment Status", options=payment_options, default=payment_options)

# Date range filter
min_date = df["Date"].min()
max_date = df["Date"].max()
selected_dates = st.sidebar.date_input(
    "Select Date Range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

# Handle case where user selects only one date (avoid errors)
if isinstance(selected_dates, tuple) and len(selected_dates) == 2:
    start_date, end_date = selected_dates
else:
    start_date, end_date = min_date, max_date

# =========================================================
# 5. APPLY FILTERS TO DATA
# =========================================================
filtered_df = df[
    (df["City"].isin(selected_cities)) &
    (df["Service_Type"].isin(selected_services)) &
    (df["Status"].isin(selected_status)) &
    (df["Payment_Status"].isin(selected_payment)) &
    (df["Date"] >= pd.to_datetime(start_date)) &
    (df["Date"] <= pd.to_datetime(end_date))
]

# Show a friendly message if filters return no data, instead of breaking charts
if filtered_df.empty:
    st.warning("No data available for the selected filters. Please adjust your filter selections.")
    st.stop()

# =========================================================
# 6. KPI CARDS
# =========================================================
st.markdown("### 📌 Key Performance Indicators")

total_clients = filtered_df["Client_Name"].nunique()
total_projects = len(filtered_df)
completed_projects = (filtered_df["Status"] == "Completed").sum()
pending_projects = (filtered_df["Status"] == "Pending").sum()
in_progress_projects = (filtered_df["Status"] == "In Progress").sum()
total_revenue = filtered_df["Amount"].sum()
pending_payment = filtered_df.loc[filtered_df["Payment_Status"] == "Pending", "Amount"].sum()

# Row 1 of KPIs
col1, col2, col3, col4 = st.columns(4)
col1.metric("👥 Total Clients", f"{total_clients}")
col2.metric("📁 Total Projects", f"{total_projects}")
col3.metric("✅ Completed", f"{completed_projects}")
col4.metric("⏳ Pending", f"{pending_projects}")

# Row 2 of KPIs
col5, col6, col7 = st.columns(3)
col5.metric("🔄 In Progress", f"{in_progress_projects}")
col6.metric("💰 Total Revenue", f"₹{total_revenue:,.0f}")
col7.metric("⚠️ Pending Payment", f"₹{pending_payment:,.0f}")

st.markdown("---")

# =========================================================
# 7. CHARTS SECTION
# =========================================================
st.markdown("### 📈 Visual Analysis")

# ---- Chart 1: Monthly Project Trend (Line Chart) ----
monthly_trend = filtered_df.groupby("Month").size().reset_index(name="Project_Count")
monthly_trend = monthly_trend.sort_values("Month")

fig_trend = px.line(
    monthly_trend, x="Month", y="Project_Count",
    title="Monthly Project Trend", markers=True
)
fig_trend.update_layout(xaxis_title="Month", yaxis_title="Number of Projects")
st.plotly_chart(fig_trend, use_container_width=True)

# ---- Chart 2 & 3 side by side: Service Revenue + Status Distribution ----
col_a, col_b = st.columns(2)

with col_a:
    service_revenue = filtered_df.groupby("Service_Type")["Amount"].sum().reset_index()
    service_revenue = service_revenue.sort_values("Amount", ascending=False)
    fig_service = px.bar(
        service_revenue, x="Service_Type", y="Amount",
        title="Service Type-wise Revenue", color="Service_Type"
    )
    fig_service.update_layout(xaxis_title="", yaxis_title="Revenue (₹)", showlegend=False)
    fig_service.update_xaxes(tickangle=45)
    st.plotly_chart(fig_service, use_container_width=True)

with col_b:
    status_count = filtered_df["Status"].value_counts().reset_index()
    status_count.columns = ["Status", "Count"]
    fig_status = px.pie(
        status_count, names="Status", values="Count",
        title="Status-wise Project Distribution", hole=0.4
    )
    st.plotly_chart(fig_status, use_container_width=True)

# ---- Chart 4 & 5 side by side: City-wise Projects + Top Clients ----
col_c, col_d = st.columns(2)

with col_c:
    city_count = filtered_df["City"].value_counts().reset_index()
    city_count.columns = ["City", "Project_Count"]
    fig_city = px.bar(
        city_count, x="City", y="Project_Count",
        title="City-wise Project Count", color="City"
    )
    fig_city.update_layout(xaxis_title="", yaxis_title="Number of Projects", showlegend=False)
    st.plotly_chart(fig_city, use_container_width=True)

with col_d:
    top_clients = filtered_df.groupby("Client_Name")["Amount"].sum().reset_index()
    top_clients = top_clients.sort_values("Amount", ascending=False).head(10)
    fig_top_clients = px.bar(
        top_clients, x="Amount", y="Client_Name", orientation="h",
        title="Top 10 Clients by Revenue", color="Amount", color_continuous_scale="Blues"
    )
    fig_top_clients.update_layout(xaxis_title="Revenue (₹)", yaxis_title="", yaxis={"categoryorder": "total ascending"})
    st.plotly_chart(fig_top_clients, use_container_width=True)

st.markdown("---")

# =========================================================
# 8. KEY INSIGHTS SECTION (auto-generated from filtered data)
# =========================================================
st.markdown("### 💡 Key Insights")

# Safely compute insights only when data is available
top_service = service_revenue.iloc[0]["Service_Type"] if not service_revenue.empty else "N/A"
top_city = city_count.iloc[0]["City"] if not city_count.empty else "N/A"
top_client_name = top_clients.iloc[0]["Client_Name"] if not top_clients.empty else "N/A"
completion_rate = (completed_projects / total_projects * 100) if total_projects > 0 else 0
pending_payment_pct = (pending_payment / total_revenue * 100) if total_revenue > 0 else 0

insights = f"""
- The company served **{total_clients} unique clients** across **{total_projects} projects** in the selected period.
- **{completion_rate:.1f}%** of projects were marked **Completed**, indicating overall service delivery performance.
- **{top_service}** generated the highest revenue among all service types.
- **{top_city}** recorded the highest number of projects, confirming it as a key business location.
- **{top_client_name}** is the top revenue-generating client in the current filter selection.
- Out of total revenue of **₹{total_revenue:,.0f}**, **₹{pending_payment:,.0f}** (**{pending_payment_pct:.1f}%**) is still pending as payment, which may need follow-up.
"""
st.markdown(insights)

st.markdown("---")

# =========================================================
# 9. FILTERED DATA TABLE
# =========================================================
st.markdown("### 📋 Filtered Project Data")
st.write(f"Showing **{len(filtered_df)}** records based on selected filters.")

display_df = filtered_df.drop(columns=["Month"]).sort_values("Date", ascending=False)
st.dataframe(display_df, use_container_width=True)

# Allow user to download the filtered data as CSV
csv_data = display_df.to_csv(index=False).encode("utf-8")
st.download_button(
    label="⬇️ Download Filtered Data as CSV",
    data=csv_data,
    file_name="filtered_project_data.csv",
    mime="text/csv"
)

# =========================================================
# 10. FOOTER
# =========================================================
st.markdown("---")
st.caption("Internship Project | Data Analyst Intern | Machin Automation (OPC) Private Limited, Kaithal")
st.caption(f"Dashboard last refreshed: {datetime.now().strftime('%d-%m-%Y %H:%M')}")
