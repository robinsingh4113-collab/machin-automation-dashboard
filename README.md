# Client Service and Project Performance Analysis Dashboard
### Machin Automation (OPC) Private Limited, Kaithal

A Streamlit-based interactive data analysis dashboard built during a Data Analyst internship to track client service requests, project status, revenue, and payment performance.

---

## 📌 Project Overview

Machin Automation (OPC) Private Limited is a Kaithal-based company offering computer, automation, and IT support services. This dashboard analyzes historical client/project data to help the company understand:

- How many clients and projects are being handled
- Which projects are completed, pending, or in progress
- Revenue earned and payments still pending
- Which services and cities generate the most business
- Who the top revenue-generating clients are

---

## 🗂️ Project Files

| File | Description |
|------|-------------|
| `app.py` | Main Streamlit dashboard application |
| `generate_dataset.py` | Script to auto-generate the sample dataset |
| `sample_dataset.csv` | Sample dataset (220 records) used by the dashboard |
| `requirements.txt` | Python libraries needed to run the project |
| `README.md` | Project documentation (this file) |

---

## 📊 Dataset Description

The dataset contains **220 records** with the following columns:

| Column | Description |
|--------|-------------|
| Date | Date the project/service request was logged |
| Client_Name | Name of the client or business |
| City | City where the client is located |
| Service_Type | Type of IT/automation service provided |
| Project_Category | New Project, Renewal, Maintenance, Upgrade, or Support Ticket |
| Status | Completed, Pending, In Progress, or Cancelled |
| Amount | Project/service amount in INR (₹) |
| Payment_Status | Paid, Pending, or Partial |
| Assigned_To | Staff member handling the project |
| Completion_Days | Number of days taken/spent on the project |
| Remarks | Short note about the project |

The dataset is synthetically generated but designed to reflect realistic patterns (e.g., Kaithal has the most clients since the company is based there; payment status is logically linked to project status).

---

## 🚀 Features of the Dashboard

1. Company title and short description
2. Sidebar filters: City, Service Type, Status, Payment Status, Date Range
3. KPI cards: Total Clients, Total Projects, Completed, Pending, In Progress, Total Revenue, Pending Payment
4. Charts:
   - Monthly Project Trend (line chart)
   - Service Type-wise Revenue (bar chart)
   - Status-wise Project Distribution (donut chart)
   - City-wise Project Count (bar chart)
   - Top 10 Clients by Revenue (horizontal bar chart)
5. Auto-generated Key Insights section
6. Filtered data table with CSV download option

---

## 💻 How to Run Locally

### Step 1: Install Python
Make sure Python 3.9+ is installed on your system.

### Step 2: Open terminal in the project folder
```bash
cd machin_dashboard
```

### Step 3: Install required libraries
```bash
pip install -r requirements.txt
```

### Step 4: (Optional) Re-generate the dataset
The `sample_dataset.csv` is already included, but if you want to regenerate it:
```bash
python generate_dataset.py
```

### Step 5: Run the Streamlit app
```bash
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`

---

## ☁️ Deployment

See `DEPLOYMENT_GUIDE.md` for step-by-step instructions to host this dashboard live on **Streamlit Community Cloud** for free.

---

## 🛠️ Tools & Technologies Used

- **Python** – Programming language
- **Pandas** – Data manipulation and analysis
- **NumPy** – Numerical operations and random data generation
- **Plotly Express** – Interactive charts and visualizations
- **Streamlit** – Web app framework for the dashboard
- **GitHub** – Version control and hosting source code
- **Streamlit Community Cloud** – Free dashboard hosting/deployment

---

## 👤 Submitted By

Data Analyst Intern
Machin Automation (OPC) Private Limited, Kaithal
