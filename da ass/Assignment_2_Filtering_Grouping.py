# ============================================================
# Assignment 2: Data Filtering, Grouping & Business Analysis
# Dataset: Superstore
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ============================================================
# LOAD DATA
# ============================================================

df = pd.read_csv('Sample - Superstore.csv', encoding='latin1')

# Clean column names
df.columns = df.columns.str.strip().str.replace(' ', '_').str.lower()

# Convert dates
df['order_date'] = pd.to_datetime(df['order_date'])

print("="*60)
print("DATA LOADED SUCCESSFULLY")
print("="*60)

# ============================================================
# PART A: BASIC OPERATIONS
# ============================================================

print("\nPART A: BASIC OPERATIONS")

# Select columns
selected = df[['category', 'sales', 'profit', 'region']]
print("\nSelected Columns:\n", selected.head())

# Filter rows (example: sales > 1000)
filtered = df[df['sales'] > 1000]
print("\nFiltered Data (Sales > 1000):\n", filtered.head())

# Sort values
sorted_df = df.sort_values(by='sales', ascending=False)
print("\nTop 5 Sales:\n", sorted_df.head())

# ============================================================
# PART B: GROUPING & AGGREGATION
# ============================================================

print("\nPART B: GROUPING & AGGREGATION")

grouped = df.groupby('category')[['sales', 'profit']].agg(['sum', 'mean', 'max', 'min'])
print(grouped)

# Top & Bottom categories
top_category = df.groupby('category')['sales'].sum().idxmax()
bottom_category = df.groupby('category')['sales'].sum().idxmin()

print("\nTop Category:", top_category)
print("Bottom Category:", bottom_category)

# ============================================================
# PART C: FEATURE ENGINEERING
# ============================================================

print("\nPART C: FEATURE ENGINEERING")

df['profit_margin'] = (df['profit'] / df['sales'] * 100).round(2)
df['order_year'] = df['order_date'].dt.year
df['high_sales'] = df['sales'].apply(lambda x: 'Yes' if x > 500 else 'No')

print(df[['profit_margin', 'order_year', 'high_sales']].head())

# ============================================================
# PART D: BUSINESS QUESTIONS (6)
# ============================================================

print("\nPART D: BUSINESS QUESTIONS")

# 1
print("\n1. Highest Sales Category:")
print(df.groupby('category')['sales'].sum())

# 2
print("\n2. Region with highest profit:")
print(df.groupby('region')['profit'].sum())

# 3
print("\n3. Average discount:")
print(df['discount'].mean())

# 4
print("\n4. Most used shipping mode:")
print(df['ship_mode'].value_counts())

# 5
print("\n5. Year-wise sales:")
print(df.groupby('order_year')['sales'].sum())

# 6
print("\n6. Loss-making transactions:")
print(df[df['profit'] < 0].shape[0])

# ============================================================
# PART E: VISUALIZATION
# ============================================================

# Line chart (sales over years)
plt.figure()
df.groupby('order_year')['sales'].sum().plot()
plt.title("Yearly Sales Trend")
plt.savefig("line_chart.png")
plt.show()

# Bar chart
plt.figure()
df.groupby('region')['sales'].sum().plot(kind='bar')
plt.title("Sales by Region")
plt.savefig("bar_chart2.png")
plt.show()

# Box plot
plt.figure()
sns.boxplot(x='category', y='profit', data=df)
plt.title("Profit Distribution")
plt.savefig("boxplot2.png")
plt.show()

# Scatter plot
plt.figure()
plt.scatter(df['sales'], df['profit'])
plt.title("Sales vs Profit")
plt.savefig("scatter2.png")
plt.show()

# ============================================================
# PART F: SUMMARY
# ============================================================

print("\nFINDINGS:")
print("1. Technology generates highest revenue")
print("2. West region has strong performance")
print("3. Discounts reduce profitability")
print("4. Consumer segment dominates")
print("5. Some products consistently incur losses")

print("\nRECOMMENDATIONS:")
print("1. Reduce high discounts")
print("2. Focus on profitable regions")
print("3. Improve pricing strategies")

print("\nLIMITATIONS:")
print("1. Dataset is historical")
print("2. No external factors considered")

print("\nAssignment 2 Completed")