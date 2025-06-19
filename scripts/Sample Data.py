import pandas as pd
import numpy as np

# Setup
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

departments = {
    "Marketing": ["Digital Ads", "Sponsorships", "Influencer Partnerships", "Events & Pop-ups"],
    "Sales": ["Sales Commissions", "CRM Software", "Training & Development"],
    "Operations": ["Warehousing", "Shipping", "Manufacturing Support", "Utilities"],
    "Product Development": ["R&D Materials", "Prototyping", "Lab Testing", "Product Innovation"],
    "Administration": ["Office Supplies", "HR & Legal", "Software Licenses", "Insurance"]
}

category_budget_range = {
    "Digital Ads": (10000, 15000),
    "Sponsorships": (8000, 12000),
    "Influencer Partnerships": (7000, 10000),
    "Events & Pop-ups": (5000, 9000),
    "Sales Commissions": (6000, 9000),
    "CRM Software": (2000, 4000),
    "Training & Development": (1000, 3000),
    "Warehousing": (8000, 12000),
    "Shipping": (7000, 10000),
    "Manufacturing Support": (6000, 9000),
    "Utilities": (3000, 5000),
    "R&D Materials": (7000, 10000),
    "Prototyping": (4000, 7000),
    "Lab Testing": (3000, 5000),
    "Product Innovation": (5000, 8000),
    "Office Supplies": (1000, 2000),
    "HR & Legal": (2000, 4000),
    "Software Licenses": (1500, 3000),
    "Insurance": (1000, 2500)
}

budget_data = []
actuals_data = []

# Generate budget and actual data
for month in months:
    for dept, categories in departments.items():
        for cat in categories:
            low, high = category_budget_range[cat]
            budget = np.random.randint(low, high)
            actual = int(budget * np.random.normal(loc=1.05, scale=0.1))  # ~ +/-10%
            budget_data.append([month, dept, cat, budget])
            actuals_data.append([month, dept, cat, actual])

# Create DataFrames
budget_df = pd.DataFrame(budget_data, columns=["Month", "Department", "Category", "Budget Amount"])
actuals_df = pd.DataFrame(actuals_data, columns=["Month", "Department", "Category", "Actual Amount"])

# Merge on Month, Department, Category
merged_df = pd.merge(budget_df, actuals_df, on=["Month", "Department", "Category"])

# Calculate Variance and Variance %
merged_df['Variance'] = merged_df['Actual Amount'] - merged_df['Budget Amount']
merged_df['Variance %'] = merged_df['Variance'] / merged_df['Budget Amount']

# Optional: Format Variance % as percentage
merged_df['Variance %'] = merged_df['Variance %'].round(4) * 100  # e.g., 12.34 %

# Export merged dataset
merged_df.to_csv("apex_budget_actuals.csv", index=False)

print("Combined data with variance calculations saved as 'apex_budget_actuals.csv'.")
