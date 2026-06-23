"""
generate_dataset.py
--------------------
This script generates a realistic sample dataset (CSV file) for
Machin Automation (OPC) Private Limited, Kaithal.

Run this file once to create 'sample_dataset.csv'.
The Streamlit app (app.py) reads this CSV to build the dashboard.

Author: Data Analyst Intern Project
"""

import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Setting a fixed seed so the dataset is the same every time we run this script
random.seed(42)
np.random.seed(42)

# ---------------------------
# 1. Define possible values
# ---------------------------

# Sample client name pool (mix of individuals & small businesses - realistic for a local IT company)
client_first_names = ["Rohit", "Sanjay", "Priya", "Anita", "Vikram", "Suresh", "Neha", "Manoj",
                       "Pooja", "Ramesh", "Sunita", "Ajay", "Deepak", "Kavita", "Ashok", "Rekha",
                       "Sandeep", "Meena", "Vinod", "Sonia", "Harish", "Geeta", "Naveen", "Shalini"]

client_business_suffix = ["Traders", "Enterprises", "Computers", "Solutions", "Agency",
                           "Store", "Services", "Industries", "Distributors", "Associates"]

cities = ["Kaithal", "Hisar", "Karnal", "Kurukshetra", "Ambala",
          "Jind", "Panipat", "Rohtak", "Chandigarh", "Delhi"]

# City weights - Kaithal (home city) gets more clients since company is based there
city_weights = [0.28, 0.10, 0.12, 0.10, 0.08, 0.07, 0.08, 0.07, 0.05, 0.05]

service_types = ["Website Maintenance", "Software Support", "Data Entry Automation",
                  "Computer Service", "Digital Presentation", "Technical Support",
                  "Automation Consultation", "Dashboard Reporting"]

project_categories = ["New Project", "Renewal", "Maintenance", "Upgrade", "Support Ticket"]

statuses = ["Completed", "Pending", "In Progress", "Cancelled"]
status_weights = [0.55, 0.15, 0.20, 0.10]   # Most projects completed - realistic distribution

payment_statuses_map = {
    # Payment status depends on project status (logical relationship)
    "Completed": [("Paid", 0.80), ("Partial", 0.15), ("Pending", 0.05)],
    "In Progress": [("Pending", 0.55), ("Partial", 0.35), ("Paid", 0.10)],
    "Pending": [("Pending", 0.85), ("Partial", 0.15)],
    "Cancelled": [("Pending", 0.70), ("Partial", 0.30)]
}

assigned_staff = ["Amit Kumar", "Pankaj Sharma", "Ritu Verma", "Vishal Singh",
                   "Komal Yadav", "Tarun Goel"]

remarks_pool = {
    "Completed": ["Delivered on time", "Client satisfied", "Closed successfully",
                  "Minor revisions done", "Smooth delivery"],
    "Pending": ["Awaiting client approval", "Documents pending from client",
                "Scheduled for next week", "On hold by client request"],
    "In Progress": ["Work ongoing", "Testing phase", "Under review",
                     "60% completed", "Final stage in progress"],
    "Cancelled": ["Client cancelled request", "Budget issue", "Project postponed indefinitely"]
}

# Base price range per service type (in INR) - gives realistic revenue spread
service_price_range = {
    "Website Maintenance": (3000, 15000),
    "Software Support": (2000, 12000),
    "Data Entry Automation": (1500, 8000),
    "Computer Service": (800, 5000),
    "Digital Presentation": (1500, 7000),
    "Technical Support": (500, 4000),
    "Automation Consultation": (5000, 25000),
    "Dashboard Reporting": (4000, 18000),
}

# ---------------------------
# 2. Generate rows
# ---------------------------

NUM_ROWS = 220  # within the 150-250 requirement

start_date = datetime(2024, 1, 1)
end_date = datetime(2025, 12, 31)
date_range_days = (end_date - start_date).days

rows = []

for i in range(1, NUM_ROWS + 1):
    # Random date within the 2-year window
    random_day = random.randint(0, date_range_days)
    project_date = start_date + timedelta(days=random_day)

    # Client name: 60% chance of business name, 40% chance of individual name
    if random.random() < 0.6:
        client_name = f"{random.choice(client_first_names)} {random.choice(client_business_suffix)}"
    else:
        client_name = random.choice(client_first_names)

    city = np.random.choice(cities, p=city_weights)
    service_type = random.choice(service_types)
    project_category = random.choice(project_categories)
    status = np.random.choice(statuses, p=status_weights)

    # Payment status logically depends on project status
    options, weights = zip(*payment_statuses_map[status])
    payment_status = np.random.choice(options, p=weights)

    # Amount based on service type price range
    low, high = service_price_range[service_type]
    amount = int(np.random.randint(low, high + 1) / 10) * 10  # round to nearest 10

    assigned_to = random.choice(assigned_staff)

    # Completion days logic: Cancelled/Pending have fewer "completed" days, Completed have full cycle
    if status == "Completed":
        completion_days = random.randint(2, 30)
    elif status == "In Progress":
        completion_days = random.randint(1, 20)  # days spent so far
    elif status == "Pending":
        completion_days = 0
    else:  # Cancelled
        completion_days = random.randint(0, 10)

    remarks = random.choice(remarks_pool[status])

    rows.append({
        "Date": project_date.strftime("%Y-%m-%d"),
        "Client_Name": client_name,
        "City": city,
        "Service_Type": service_type,
        "Project_Category": project_category,
        "Status": status,
        "Amount": amount,
        "Payment_Status": payment_status,
        "Assigned_To": assigned_to,
        "Completion_Days": completion_days,
        "Remarks": remarks
    })

# ---------------------------
# 3. Create DataFrame and save
# ---------------------------

df = pd.DataFrame(rows)

# Sort by date for a clean, realistic look
df = df.sort_values("Date").reset_index(drop=True)

df.to_csv("sample_dataset.csv", index=False)

print(f"Dataset generated successfully with {len(df)} rows.")
print(df.head(10))
print("\nColumn names:", list(df.columns))
print("\nStatus distribution:\n", df["Status"].value_counts())
print("\nPayment status distribution:\n", df["Payment_Status"].value_counts())
