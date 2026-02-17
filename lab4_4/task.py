import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

try:
    df = pd.read_excel('s7_data_sample_rev4_50k.xlsx')
except:
    print("ensure the data file is in the working directory")
    exit()

print(df.describe())

plt.figure(figsize=(12,6))
plt.hist(df['REVENUE_AMOUNT'], bins=50)
plt.title('distribution of ticket sales amount')
plt.xlabel('amount')
plt.ylabel('frequency')
plt.show()

if 'ORIG_CITY_CODE' in df.columns:
    plt.figure(figsize=(12,6))
    top_10_orig = df['ORIG_CITY_CODE'].value_counts().head(10)
    plt.bar(range(len(top_10_orig)), top_10_orig.values)
    plt.xticks(range(len(top_10_orig)), top_10_orig.index, rotation=45)
    plt.title('top 10 departure airports by ticket sales')
    plt.xlabel('airport code')
    plt.ylabel('number of tickets')
    plt.show()

if 'DEST_CITY_CODE' in df.columns:
    plt.figure(figsize=(12,6))
    top_10_dest = df['DEST_CITY_CODE'].value_counts().head(10)
    plt.bar(range(len(top_10_dest)), top_10_dest.values)
    plt.xticks(range(len(top_10_dest)), top_10_dest.index, rotation=45)
    plt.title('top 10 arrival airports by ticket sales')
    plt.xlabel('airport code')
    plt.ylabel('number of tickets')
    plt.show()

if 'ISSUE_DATE' in df.columns:
    df['ISSUE_DATE'] = pd.to_datetime(df['ISSUE_DATE'])
    df['MONTH'] = df['ISSUE_DATE'].dt.month
    df['YEAR'] = df['ISSUE_DATE'].dt.year
    
    monthly_sales = df.groupby(['YEAR', 'MONTH'])['REVENUE_AMOUNT'].sum().reset_index()
    monthly_sales['DATE'] = pd.to_datetime(monthly_sales['YEAR'].astype(str) + '-' + monthly_sales['MONTH'].astype(str))
    
    plt.figure(figsize=(15,6))
    plt.plot(monthly_sales['DATE'], monthly_sales['REVENUE_AMOUNT'])
    plt.title('monthly ticket sales trend')
    plt.xlabel('month')
    plt.ylabel('total sales amount')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()

if 'PAX_TYPE' in df.columns:
    pax_summary = df.groupby('PAX_TYPE')['REVENUE_AMOUNT'].agg(['mean', 'sum', 'count']).round(2)
    pax_summary.columns = ['average amount', 'total revenue', 'ticket count']
    print("passenger type summary:")
    print(pax_summary)
    
    plt.figure(figsize=(10,6))
    plt.pie(pax_summary['ticket count'], labels=pax_summary.index, autopct='%1.1f%%')
    plt.title('passenger type distribution')
    plt.ylabel('')
    plt.show()
    
    if 'FFP_FLAG' in df.columns:
        loyalty_summary = df.groupby('FFP_FLAG')['REVENUE_AMOUNT'].agg(['mean', 'count'])
        print("\nloyalty program summary:")
        print(loyalty_summary)

if 'FOP_TYPE_CODE' in df.columns:
    payment_summary = df.groupby('FOP_TYPE_CODE')['REVENUE_AMOUNT'].agg(['mean', 'sum', 'count']).round(2)
    payment_summary.columns = ['average amount', 'total revenue', 'transaction count']
    print("\npayment method summary:")
    print(payment_summary)
    
    plt.figure(figsize=(12,8))
    freq = df['FOP_TYPE_CODE'].value_counts()
    top5 = freq.head(5)
    if len(freq) > 5:
        other_count = freq[5:].sum()
        top5['other'] = other_count
    plt.pie(top5.values, labels=top5.index, autopct='%1.1f%%')
    plt.title('payment method distribution')
    plt.ylabel('')
    plt.show()

if 'ROUTE_FLIGHT_TYPE' in df.columns:
    flight_type_summary = df.groupby('ROUTE_FLIGHT_TYPE')['REVENUE_AMOUNT'].agg(['mean', 'sum', 'count'])
    print("\nflight type summary:")
    print(flight_type_summary)

if 'ISSUE_DATE' in df.columns:
    daily_sales = df.groupby('ISSUE_DATE')['REVENUE_AMOUNT'].sum().reset_index()
    daily_sales = daily_sales.sort_values('ISSUE_DATE')
    daily_sales['DAY_INDEX'] = range(len(daily_sales))
    
    X = daily_sales[['DAY_INDEX']]
    y = daily_sales['REVENUE_AMOUNT']
    
    model = LinearRegression()
    model.fit(X, y)
    predictions = model.predict(X)
    
    plt.figure(figsize=(15,6))
    plt.plot(daily_sales['ISSUE_DATE'], y, label='actual', alpha=0.7)
    plt.plot(daily_sales['ISSUE_DATE'], predictions, label='predicted', linestyle='--')
    plt.title('ticket sales prediction')
    plt.xlabel('date')
    plt.ylabel('sales amount')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.show()
    
    future_days = pd.DataFrame({
        'DAY_INDEX': range(len(daily_sales), len(daily_sales) + 30)
    })
    future_predictions = model.predict(future_days)
    print(f"predicted sales for next 30 days: {future_predictions.mean():.2f} (average)")

if 'SALE_TYPE' in df.columns:
    sale_type_summary = df.groupby('SALE_TYPE')['REVENUE_AMOUNT'].agg(['mean', 'sum', 'count'])
    print("\nsale type summary:")
    print(sale_type_summary)