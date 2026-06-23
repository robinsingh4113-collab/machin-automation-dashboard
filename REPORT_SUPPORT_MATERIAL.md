# Internship Report Support Material

## Project Title
**Client Service and Project Performance Analysis Dashboard for Machin Automation (OPC) Private Limited, Kaithal**

---

## 1. Project Abstract

Machin Automation (OPC) Private Limited, Kaithal, provides computer, automation, and IT-related services to clients across multiple cities in Haryana and nearby regions. The company handles a large number of client service requests and projects, including website maintenance, software support, data entry automation, and technical support, making it difficult to track performance, revenue, and pending payments manually.

This project presents an interactive **Client Service and Project Performance Analysis Dashboard** built using Python and Streamlit to address this challenge. The dashboard consolidates client and project data — including service type, project status, revenue, and payment status — into a single visual interface. It enables management to monitor key metrics such as total clients, completed/pending/in-progress projects, total revenue, and pending payments at a glance.

The dashboard includes interactive filters for city, service type, project status, payment status, and date range, allowing focused analysis of any subset of data. Visualizations such as monthly trend lines, revenue-by-service bar charts, status distribution donut charts, city-wise project charts, and a top-clients ranking provide quick, actionable insights. An auto-generated "Key Insights" section summarizes the most important findings in plain language.

The project was developed using Python, Pandas, NumPy, and Plotly for data processing and visualization, with Streamlit as the web framework, and deployed live on Streamlit Community Cloud. This project demonstrates practical skills in data cleaning, exploratory data analysis, dashboard design, and cloud deployment — core competencies for a Data Analyst role.

---

## 2. Project Objectives

1. To analyze client service and project performance data of Machin Automation (OPC) Private Limited.
2. To track the total number of clients, projects, and their completion status.
3. To calculate total revenue generated and identify pending payments.
4. To study monthly project trends over time.
5. To identify which service types generate the highest revenue.
6. To analyze city-wise distribution of clients and projects.
7. To identify top revenue-generating clients.
8. To build an interactive, filterable dashboard for real-time data exploration.
9. To deploy the dashboard online for live access and demonstration.
10. To present data-driven insights that can support business decision-making.

---

## 3. Work Done During Internship

1. Studied the business operations and service offerings of Machin Automation (OPC) Private Limited to understand the type of data relevant to client and project tracking.
2. Designed a structured dataset schema covering client details, service type, project status, revenue, and payment information.
3. Generated and cleaned a sample dataset of 220 records representing realistic client/project records using Python (Pandas and NumPy).
4. Performed exploratory data analysis (EDA) to study project status distribution, revenue patterns, and city-wise trends.
5. Built KPI metrics for total clients, total projects, completed/pending/in-progress projects, total revenue, and pending payments.
6. Designed and developed interactive visualizations (line chart, bar charts, donut chart) using Plotly to represent monthly trends, service-wise revenue, status distribution, and city-wise data.
7. Developed a complete interactive dashboard using the Streamlit framework with sidebar filters for city, service type, status, payment status, and date range.
8. Implemented a dynamic "Key Insights" section that auto-generates summary observations based on filtered data.
9. Tested the dashboard for different filter combinations to ensure accuracy and error-free functioning.
10. Deployed the final dashboard on Streamlit Community Cloud and obtained a live shareable link for demonstration.

---

## 4. Viva Explanation (In Simple Words)

**Q: What is your project about?**
"My project is a dashboard that analyzes client and project data for Machin Automation, a Kaithal-based IT and automation services company. It shows how many clients they have, how many projects are completed or pending, how much revenue they've earned, and which payments are still due."

**Q: Why did you choose this project?**
"Since the company provides IT and automation services to many clients, tracking project status and payments manually is time-consuming. A dashboard makes it easy to see all this information visually in one place."

**Q: What data did you use?**
"I created a realistic sample dataset with 220 records, including fields like client name, city, service type, project status, amount, and payment status — based on the type of services the company actually offers, like website maintenance, software support, and technical support."

**Q: What tools did you use?**
"I used Python for data handling, Pandas and NumPy to process the data, Plotly to create charts, and Streamlit to build the web dashboard. I deployed it online using Streamlit Community Cloud, which is free."

**Q: What can the dashboard do?**
"It shows KPI cards like total clients and total revenue, charts like monthly project trends and top clients by revenue, and lets the user filter the data by city, service type, status, payment status, and date. There's also a table at the bottom showing the actual filtered records, and a summary of key insights generated automatically from the data."

**Q: What did you learn from this project?**
"I learned how to clean and structure data, build visualizations that communicate insights clearly, design an interactive dashboard, and deploy a Python web application online — all important skills for a Data Analyst."

**Q: How is the payment status decided in your data?**
"It's logically linked to the project status — for example, completed projects are mostly marked as paid, while in-progress or pending projects are more likely to have pending or partial payments. This makes the dataset behave realistically."

**Q: Can this be used with real company data?**
"Yes — the structure is designed so that if the company exports its real project records into the same column format, the same dashboard would work directly on real data without any code changes."

---

## 5. Screenshots to Include in Your Internship Report

Take these screenshots from your live deployed dashboard (or local run) and include them in your report:

1. **Full dashboard top view** — showing the title, company name, and short description
2. **KPI cards section** — showing all 7 metric cards together
3. **Sidebar filters panel** — showing all filter options expanded
4. **Monthly Project Trend chart** (line chart)
5. **Service Type-wise Revenue chart** (bar chart)
6. **Status-wise Project Distribution chart** (donut/pie chart)
7. **City-wise Project Count chart** (bar chart)
8. **Top 10 Clients by Revenue chart**
9. **Key Insights section** (text-based auto insights)
10. **Filtered data table** at the bottom with the download button visible
11. **One screenshot showing filters applied** (e.g., select only "Kaithal" city and one service type) to demonstrate interactivity
12. **Browser address bar showing your live Streamlit Cloud URL** — important to prove it's hosted online

**Tip:** Take screenshots in full-screen browser mode for a clean, professional look. Use Windows Snipping Tool (Win + Shift + S) or your browser's screenshot extension.

---

## 6. Suggested Report Structure (Chapter-wise)

1. Introduction / Company Profile
2. Objectives of the Project
3. Tools and Technologies Used
4. System Requirements
5. Dataset Description
6. Methodology / Approach
7. Dashboard Design and Features (with screenshots)
8. Key Insights and Findings
9. Deployment Process
10. Conclusion and Learnings
11. Future Scope (e.g., connecting to live database, adding login system, email alerts for pending payments)
12. References
