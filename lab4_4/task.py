import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import warnings
warnings.filterwarnings('ignore')

try:
    df = pd.read_excel('S7 продажи авиабилетов.xlsx')
except:
    print("ensure the data file is in the working directory")
    exit()

print(df.info())
print(df.describe())

plt.figure(figsize=(12,6))
df['Amount'].hist(bins=50)
plt.title('distribution of ticket sales amount')
plt.xlabel('amount')
plt.ylabel('frequency')
plt.show()

if 'Airport' in df.columns:
    plt.figure(figsize=(12,6))
    df['Airport'].value_counts().head(10).plot(kind='bar')
    plt.title('top 10 airports by ticket sales')
    plt.xlabel('airport')
    plt.ylabel('number of tickets')
    plt.show()

if 'Date' in df.columns:
    df['Month'] = pd.to_datetime(df['Date']).dt.month
    monthly_sales = df.groupby('Month')['Amount'].sum()
    plt.figure(figsize=(12,6))
    monthly_sales.plot(kind='line')
    plt.title('monthly ticket sales trend')
    plt.xlabel('month')
    plt.ylabel('total sales amount')
    plt.show()

if 'Passenger_Status' in df.columns:
    status_summary = df.groupby('Passenger_Status')['Amount'].agg(['mean','count'])
    print(status_summary)

if 'Payment_Method' in df.columns:
    payment_summary = df.groupby('Payment_Method')['Amount'].agg(['mean','count'])
    print(payment_summary)
    plt.figure(figsize=(12,6))
    df['Payment_Method'].value_counts().plot(kind='pie', autopct='%1.1f%%')
    plt.title('payment method distribution')
    plt.show()

if 'Date' in df.columns:
    daily_sales = df.groupby('Date')['Amount'].sum().reset_index()
    daily_sales['Day'] = range(len(daily_sales))
    
    X = daily_sales[['Day']]
    y = daily_sales['Amount']
    
    model = LinearRegression()
    model.fit(X, y)
    predictions = model.predict(X)
    
    plt.figure(figsize=(12,6))
    plt.plot(daily_sales['Date'], y, label='actual')
    plt.plot(daily_sales['Date'], predictions, label='predicted')
    plt.title('ticket sales prediction')
    plt.xlabel('date')
    plt.ylabel('sales amount')
    plt.legend()
    plt.show()

    mae = mean_absolute_error(y, predictions)
    print(f'mean absolute error for sales prediction: {mae:.2f}')