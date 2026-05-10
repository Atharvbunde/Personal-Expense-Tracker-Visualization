import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

os.makedirs("data", exist_ok=True)
os.makedirs("outputs", exist_ok=True)
os.makedirs("images", exist_ok=True)
os.makedirs("reports", exist_ok=True)

# Create synthetic expense data
data = {
    "Date": pd.date_range(start="2026-01-01", periods=60, freq="D"),
    "Category": np.random.choice(["Food", "Travel", "Shopping", "Bills", "Education", "Entertainment"], 60),
    "Amount": np.random.randint(50, 2000, 60),
    "Payment_Method": np.random.choice(["Cash", "UPI", "Card"], 60),
    "Note": np.random.choice(["Daily use", "Important", "Personal", "College", "Family"], 60)
}

df = pd.DataFrame(data)
df.to_csv("data/expenses.csv", index=False)

# Load data
df = pd.read_csv("data/expenses.csv")
df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.strftime("%Y-%m")

# Analysis
total_spending = df["Amount"].sum()
avg_daily = df.groupby("Date")["Amount"].sum().mean()
category_spending = df.groupby("Category")["Amount"].sum().sort_values(ascending=False)
monthly_spending = df.groupby("Month")["Amount"].sum()
payment_spending = df.groupby("Payment_Method")["Amount"].sum()
highest_category = category_spending.idxmax()

# Save analysis CSV
category_spending.to_csv("outputs/category_spending.csv")
monthly_spending.to_csv("outputs/monthly_spending.csv")
payment_spending.to_csv("outputs/payment_method_spending.csv")

# Charts
plt.figure(figsize=(8,5))
category_spending.plot(kind="bar")
plt.title("Category-wise Expense Analysis")
plt.xlabel("Category")
plt.ylabel("Amount")
plt.tight_layout()
plt.savefig("images/category_wise_expense.png")
plt.close()

plt.figure(figsize=(8,5))
monthly_spending.plot(kind="line", marker="o")
plt.title("Monthly Spending Trend")
plt.xlabel("Month")
plt.ylabel("Amount")
plt.tight_layout()
plt.savefig("images/monthly_spending_trend.png")
plt.close()

plt.figure(figsize=(6,6))
payment_spending.plot(kind="pie", autopct="%1.1f%%")
plt.title("Payment Method Analysis")
plt.ylabel("")
plt.tight_layout()
plt.savefig("images/payment_method_pie.png")
plt.close()

daily_spending = df.groupby("Date")["Amount"].sum()
plt.figure(figsize=(10,5))
daily_spending.plot(kind="line")
plt.title("Daily Spending Trend")
plt.xlabel("Date")
plt.ylabel("Amount")
plt.tight_layout()
plt.savefig("images/daily_spending_trend.png")
plt.close()

# Report
report = f"""
PERSONAL EXPENSE TRACKER REPORT

Total Spending: ₹{total_spending}
Average Daily Spending: ₹{avg_daily:.2f}
Highest Spending Category: {highest_category}

Category-wise Spending:
{category_spending.to_string()}

Monthly Spending:
{monthly_spending.to_string()}

Payment Method Spending:
{payment_spending.to_string()}
"""

with open("reports/expense_report.txt", "w", encoding="utf-8") as f:
    f.write(report)

print("Project executed successfully!")
print(f"Total Spending: ₹{total_spending}")
print(f"Average Daily Spending: ₹{avg_daily:.2f}")
print(f"Highest Spending Category: {highest_category}")
print("Charts saved in images folder.")
print("Report saved in reports folder.")