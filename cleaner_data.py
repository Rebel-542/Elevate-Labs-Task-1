import pandas as pd
import numpy as np

df = pd.read_csv("Mall_Customers.csv")

print("--- Initial Data Inspection ---")
print(df.info())

df = df.dropna(subset=['CustomerID', 'Gender', 'Age', 'Annual Income (k$)', 'Spending Score (1-100)'])

df = df.drop_duplicates(subset=['CustomerID'])

df.columns = df.columns.str.strip().str.lower()
df.columns = df.columns.str.replace(r'[\(\)\$\-]', '', regex=True).str.replace(' ', '_')
df = df.rename(columns={'annual_income_k': 'annual_income', 'spending_score_1100': 'spending_score'})

df['gender'] = df['gender'].astype(str).str.capitalize().str.strip()

df = df[(df['age'] >= 0) & (df['age'] <= 120)]
df['age'] = df['age'].astype(int)

df = df[(df['annual_income'] >= 0)]
df['annual_income'] = df['annual_income'].astype(int)

df = df[(df['spending_score'] >= 1) & (df['spending_score'] <= 100)]
df['spending_score'] = df['spending_score'].astype(int)

df.to_csv("cleaned_mall_customers.csv", index=False)
print("\n--- Cleaning Complete. File saved as 'cleaned_mall_customers.csv' ---")