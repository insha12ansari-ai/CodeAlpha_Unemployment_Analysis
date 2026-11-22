#Import Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Load Dataset
df=pd.read_csv("Unemployment_in_India.csv")
# Display frist 5 row
print(df.head())
print("\nDatabase Shape:")
print(df.shape)
print("\nColumn Names:")
print(df.columns)
print("\nDataset Information:")
print(df.info())
print("\nStatistical Summary:")
print(df.describe())
#Remove extra spaces from column names
df.columns = df.columns.str.strip()
#Check missing values
print("\nMissing Values:")
print(df.isnull().sum())
#Check duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())
#Remove duplicate rows
df = df.drop_duplicates()
#Remove rows with missing values
df = df.dropna()
print("\nCleaned Dataset Shape:")
print(df.shape)
print("\nCleaned Dataset:")
print(df.head())
#Data Conversion
df['Data']=pd.to_datetime(df['Date'],dayfirst=True)
print("\nDate Column:")
print(df['Data'].head())
#Convert numeric columns into numeric format
df['Estimated Unemployment Rate (%)']=pd.to_numeric(
    df['Estimated Unemployment Rate (%)'],errors='coerce'
)
df['Estimate Employed']=pd.to_numeric(
    df['Estimated Employed'],errors='coerce'
)
df['Estimated Labour Participation Rate (%)'] = pd.to_numeric(
    df['Estimated Labour Participation Rate (%)'],
    errors='coerce'
)
#Remove rows with missing numerical values
df=df.dropna()
print("\nData is ready for analysis!")
print(df.head())
#Overall Unemployment Analysis
average_unemployment = df['Estimated Unemployment Rate (%)'].mean()
highest_unemployement = df['Estimated Unemployment Rate (%)'].max()
lowest_unemployment = df['Estimated Unemployment Rate (%)'].min()
print("\n===== Unemployment Analysis =====")
print("Average Unemployment Rate:",round(average_unemployment,2),"%" )
print("Highest Unemployment Rate:",round(highest_unemployement,2),"%")
print("Lowest Unemployment Rate:",round(lowest_unemployment,2),"%")

#COVID-19 Impact Analysis
# Step 9: COVID-19 Impact Analysis

# Convert Date into proper date format
df['Date'] = pd.to_datetime(
    df['Date'].astype(str).str.strip(),
    dayfirst=True,
    errors='coerce'
)

# Remove invalid dates
df = df.dropna(subset=['Date'])

# Separate COVID periods
df['Period'] = 'During COVID'

df.loc[
    df['Date'] < pd.Timestamp('2020-03-01'),
    'Period'
] = 'Before COVID'

# Calculate average unemployment
covid_analysis = df.groupby('Period')[
    'Estimated Unemployment Rate (%)'
].mean()

print("\n===== COVID-19 Impact Analysis =====")
print(covid_analysis)
# Step 10: State-wise Unemployment Analysis

state_unemployment = df.groupby('Region')[
    'Estimated Unemployment Rate (%)'
].mean().sort_values(ascending=False)

print("\n===== State-wise Unemployment Analysis =====")

print("\nTop 10 Regions with Highest Unemployment:")
print(state_unemployment.head(10))

print("\nTop 10 Regions with Lowest Unemployment:")
print(state_unemployment.tail(10))
# Step 11: Monthly Analysis

df['Month'] = df['Date'].dt.month

monthly_unemployment = df.groupby('Month')[
    'Estimated Unemployment Rate (%)'
].mean()

print("\n===== Monthly Unemployment Analysis =====")
print(monthly_unemployment)
# Step 12: Monthly Unemployment Graph

plt.figure(figsize=(10, 5))

plt.plot(
    monthly_unemployment.index,
    monthly_unemployment.values,
    marker='o'
)

plt.title('Monthly Unemployment Rate in India')
plt.xlabel('Month')
plt.ylabel('Unemployment Rate (%)')

plt.xticks(range(1, 13))
plt.grid(True)

plt.show()
# Step 13: COVID-19 Impact Graph

plt.figure(figsize=(8, 5))

covid_analysis.plot(
    kind='bar',
    color=['skyblue', 'orange']
)

plt.title('Impact of COVID-19 on Unemployment')
plt.xlabel('Period')
plt.ylabel('Average Unemployment Rate (%)')

plt.xticks(rotation=0)
plt.grid(axis='y')

plt.tight_layout()
plt.show()
# Step 14: State-wise Unemployment Graph

plt.figure(figsize=(12, 6))

state_unemployment.head(10).plot(
    kind='bar',
    color='lightgreen'
)

plt.title('Top 10 Regions with Highest Unemployment')
plt.xlabel('States / Regions')
plt.ylabel('Unemployment Rate (%)')

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
# Step 15: Employment Analysis

average_employed = df['Estimated Employed'].mean()

highest_employed = df['Estimated Employed'].max()

lowest_employed = df['Estimated Employed'].min()

print("\n===== Employment Analysis =====")

print("Average Employed People:",
      round(average_employed, 2))

print("Highest Estimated Employment:",
      round(highest_employed, 2))

print("Lowest Estimated Employment:",
      round(lowest_employed, 2))
# Step 16: Final Project Insights

print("\n========== FINAL PROJECT REPORT ==========")

print("Average Unemployment Rate:",
      round(average_unemployment, 2), "%")

print("Highest Unemployment Region:",
      state_unemployment.index[0])

print("Lowest Unemployment Region:",
      state_unemployment.index[-1])

print("\nCOVID-19 Impact:")
print(covid_analysis)

print("\nAverage Employment:",
      round(average_employed, 2))

print("\n========== PROJECT COMPLETED ==========")