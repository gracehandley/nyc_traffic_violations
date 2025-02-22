# Author: Grace Handley
# Version 1.0
# Date created: 2025-02-22
# Date updated: 2025-02-22

import pandas as pd
pd.set_option('display.float_format', '{:.2f}'.format)

df = pd.read_csv("data/Open_Parking_and_Camera_Violations_20250220.csv")

print(df.info())
df['Issue Date'] = pd.to_datetime(df['Issue Date'])
df['Violation Time'] = pd.to_datetime(df['Violation Time'], format='%H:%M:%S', errors='coerce')
df['Judgment Entry Date'] = pd.to_datetime(df['Judgment Entry Date'], errors='coerce')

print(df.isnull().sum())
print(df.head(100))

# Recode County values
print("Unique Counties:", df['County'].unique())

borough_mapping = {
    'BX': 'Bronx',
    'Q': 'Queens',
    'K': 'Brooklyn',
    'R': 'Staten Island',
    'BK': 'Brooklyn',
    'QN': 'Queens',
    'MN': 'Manhattan',
    'Kings': 'Brooklyn',
    'Qns': 'Queens',
    'Bronx': 'Bronx',
    'Rich': 'Staten Island',
    'QUEEN': 'Queens',
    'A': 'Staten Island',  # Assuming 'A' represents Staten Island
    'BRONX': 'Bronx',
    'QNS': 'Queens',
    'NY': 'Manhattan',  # Assuming 'NY' is a mistake and should be Manhattan
    'ST': 'Staten Island'
}

df['County'] = df['County'].replace(borough_mapping)
print("Unique Counties After Recode:", df['County'].unique())

# Filter data for January 2025
date_range = (df['Issue Date'].min(), df['Issue Date'].max())
print(f"Range of Issue Dates: {date_range}")

df_filtered = df[(df['Issue Date'] >= pd.to_datetime('2025-01-01')) & (df['Issue Date'] <= pd.to_datetime('2025-02-01'))]
print(df_filtered.head())

# Describe January 2025 violation data
total_violations = df_filtered.shape[0]
print(f"Total number of violations: {total_violations}")
print(df_filtered[['Fine Amount', 'Payment Amount']].describe())
