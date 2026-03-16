import pandas as pd

# Define the data for all 10 pages
data_map = {
    "Project_Management": {
        "Task ID": [101, 102, 103, 104],
        "Task Name": ["Setup FastAPI", "DB Schema", "API Auth", "Frontend"],
        "Owner": ["Alice", "Bob", "Charlie", "Alice"],
        "Status": ["Done", "In Progress", "To Do", "To Do"],
        "% Complete": [100, 60, 0, 0]
    },
    "Financial_Tracker": {
        "Category": ["Rent", "Groceries", "Utilities", "Internet"],
        "Budgeted": [2000, 500, 150, 80],
        "Actual": [2000, 612, 142, 80],
        "Date": ["2026-03-01", "2026-03-10", "2026-03-12", "2026-03-15"]
    },
    "CRM_Contacts": {
        "Name": ["John Doe", "Jane Smith", "Bob Lee", "Sarah Jen"],
        "Company": ["TechCorp", "DesignHub", "BuildIt", "CloudNet"],
        "Email": ["john@t.com", "jane@d.io", "bob@b.com", "s@c.net"],
        "Status": ["Warm", "Customer", "Cold", "Warm"]
    },
    "Inventory": {
        "SKU": ["APP-01", "MON-05", "KEY-02", "MOU-09"],
        "Item": ["MacBook", "4K Monitor", "Keyboard", "Mouse"],
        "Quantity": [5, 12, 25, 30],
        "Price": [2400, 400, 120, 80]
    },
    "Content_Calendar": {
        "Date": ["2026-03-20", "2026-03-22", "2026-03-25", "2026-03-30"],
        "Platform": ["LinkedIn", "YouTube", "Blog", "Twitter"],
        "Topic": ["System Design", "FastAPI Tips", "Python vs Go", "AI News"],
        "Status": ["Draft", "Planned", "Research", "Done"]
    },
    "Health_Log": {
        "Date": ["2026-03-14", "2026-03-15", "2026-03-16", "2026-03-17"],
        "Workout": ["Run", "Weights", "Yoga", "Swim"],
        "Duration": [45, 60, 30, 40],
        "Sleep_Hrs": [7.5, 6.0, 8.0, 7.2]
    },
    "Subscriptions": {
        "Service": ["AWS", "Netflix", "ChatGPT", "Spotify"],
        "Cost": [45.00, 15.99, 20.00, 9.99],
        "Renew_Date": ["25th", "12th", "05th", "19th"],
        "Auto_Renew": ["Yes", "Yes", "Yes", "No"]
    },
    "Travel_Planner": {
        "Day": [1, 1, 2, 2],
        "Activity": ["Flight", "Hotel Check-in", "Conference", "Dinner"],
        "Location": ["SFO", "Hilton", "Moscone", "Original Joes"],
        "Cost": [450, 200, 0, 60]
    },
    "Documentation": {
        "Topic": ["API Specs", "Security", "UI Guide", "Deploy"],
        "Version": ["1.2", "2.0", "1.0", "1.1"],
        "Last_Updated": ["2026-03-10", "2026-01-15", "2025-11-20", "2026-02-01"]
    },
    "Master_Dashboard": {
        "Metric": ["Avg Progress", "Total Spend", "Inventory Value", "Sub Total"],
        "Value": ["40%", "$2834.00", "$22,200", "$90.98"],
        "Trend": ["Up", "Stable", "Stable", "Down"]
    }
}

# Create the Excel file with 10 sheets
with pd.ExcelWriter("Paytm_System_Testing.xlsx") as writer:
    for sheet_name, content in data_map.items():
        df = pd.DataFrame(content)
        df.to_excel(writer, sheet_name=sheet_name, index=False)

print("✅ 'Paytm_System_Testing.xlsx' has been created with 10 pages of info!")