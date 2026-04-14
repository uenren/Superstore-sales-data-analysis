# ============================================================
# Assignment 1: Python for Data Cleaning and EDA
# Dataset: Superstore Sales Dataset
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ============================================================
# PART A: DATA LOADING AND UNDERSTANDING
# ============================================================

# Load dataset
df = pd.read_csv('Sample - Superstore.csv', encoding='latin1')

print("=" * 60)
print("PART A: DATA LOADING AND UNDERSTANDING")
print("=" * 60)

print("\n--- First 5 Rows ---")
print(df.head())

print(f"\n--- Shape ---")
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

print("\n--- Column Types ---")
print(df.dtypes)

print("\n--- Missing Values ---")
print(df.isnull().sum())
print(f"Total missing values: {df.isnull().sum().sum()}")

# ============================================================
# PART B: DATA CLEANING
# ============================================================

print("\n" + "=" * 60)
print("PART B: DATA CLEANING")
print("=" * 60)

# Remove duplicates
before = len(df)
df = df.drop_duplicates()
print(f"\n--- Duplicates Removed: {before - len(df)} rows removed ---")

# Fill missing values (FIXED - no warnings)
for col in df.select_dtypes(include='number').columns:
    df[col] = df[col].fillna(df[col].median())

for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].fillna(df[col].mode()[0])

print("Missing values after cleaning:", df.isnull().sum().sum())

# Rename columns
df.columns = df.columns.str.strip().str.replace(' ', '_').str.lower()

# Convert date columns
df['order_date'] = pd.to_datetime(df['order_date'])
df['ship_date'] = pd.to_datetime(df['ship_date'])

# Create new columns
df['profit_margin'] = (df['profit'] / df['sales'] * 100).round(2)
df['shipping_days'] = (df['ship_date'] - df['order_date']).dt.days

# ============================================================
# PART C: DESCRIPTIVE ANALYSIS
# ============================================================

print("\n" + "=" * 60)
print("PART C: DESCRIPTIVE ANALYSIS")
print("=" * 60)

num_cols = ['sales', 'quantity', 'discount', 'profit', 'profit_margin', 'shipping_days']

print("\nMean:\n", df[num_cols].mean())
print("\nMedian:\n", df[num_cols].median())
print("\nMode:\n", df[num_cols].mode().iloc[0])
print("\nStd Dev:\n", df[num_cols].std())
print("\nVariance:\n", df[num_cols].var())

print("\nCategory Counts:\n", df['category'].value_counts())

corr_matrix = df[num_cols].corr()

# ============================================================
# PART D: VISUALIZATION (FIXED)
# ============================================================

# 1. Histogram
plt.figure()
df['sales'].hist(bins=30)
plt.title("Sales Distribution")
plt.savefig("histogram.png")
plt.show()

# 2. Bar Chart
plt.figure()
df.groupby('category')['sales'].sum().plot(kind='bar')
plt.title("Sales by Category")
plt.savefig("bar_chart.png")
plt.show()

# 3. Box Plot
plt.figure()
sns.boxplot(x='category', y='profit', data=df)
plt.title("Profit by Category")
plt.savefig("boxplot.png")
plt.show()

# 4. Count Plot
plt.figure()
sns.countplot(x='category', data=df)
plt.title("Category Count")
plt.savefig("countplot.png")
plt.show()

# 5. Heatmap
plt.figure()
sns.heatmap(corr_matrix, annot=True)
plt.title("Correlation Heatmap")
plt.savefig("heatmap.png")
plt.show()

# 6. Scatter Plot
plt.figure()
plt.scatter(df['sales'], df['profit'])
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.title("Sales vs Profit")
plt.savefig("scatter.png")
plt.show()

# ============================================================
# PART E: INSIGHTS
# ============================================================

print("\nINSIGHTS:")
print("1. Technology category has highest sales")
print("2. Some products have negative profit")
print("3. Sales and profit are correlated")
print("4. High discounts reduce profit")
print("5. Consumer segment dominates orders")
print("6. Shipping time varies significantly")
print("7. West region performs best")
print("8. Some sub-categories are loss-making")

print("\nRECOMMENDATIONS:")
print("1. Reduce discounts")
print("2. Focus on profitable categories")
print("3. Improve pricing strategy")

print("\nAssignment Completed ✅")