import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import warnings
warnings.filterwarnings('ignore')

try:
    df = pd.read_excel('s7_data_sample_rev4_50k.xlsx')
except:
    print("ensure the data file is in the working directory")
    exit()

print(df.info())
print(df.describe())

plt.figure(figsize=(12,6))
df['REVENUE_AMOUNT'].hist(bins=50)
plt.title('Distribution of Ticket Sales Amount')
plt.xlabel('Amount')
plt.ylabel('Frequency')
plt.show()

if 'ORIG_CITY_CODE' in df.columns:
    plt.figure(figsize=(12,6))
    top_10_orig = df['ORIG_CITY_CODE'].value_counts().head(10)
    top_10_orig.plot(kind='bar')
    plt.title('Top 10 Departure Airports by Ticket Sales')
    plt.xlabel('Airport Code')
    plt.ylabel('Number of Tickets')
    plt.show()

if 'DEST_CITY_CODE' in df.columns:
    plt.figure(figsize=(12,6))
    top_10_dest = df['DEST_CITY_CODE'].value_counts().head(10)
    top_10_dest.plot(kind='bar')
    plt.title('Top 10 Arrival Airports by Ticket Sales')
    plt.xlabel('Airport Code')
    plt.ylabel('Number of Tickets')
    plt.show()

if 'ISSUE_DATE' in df.columns:
    df['ISSUE_DATE'] = pd.to_datetime(df['ISSUE_DATE'])
    df['MONTH'] = df['ISSUE_DATE'].dt.month
    df['YEAR'] = df['ISSUE_DATE'].dt.year
    
    monthly_sales = df.groupby(['YEAR', 'MONTH'])['REVENUE_AMOUNT'].sum().reset_index()
    monthly_sales['DATE'] = pd.to_datetime(monthly_sales['YEAR'].astype(str) + '-' + monthly_sales['MONTH'].astype(str))
    
    plt.figure(figsize=(15,6))
    plt.plot(monthly_sales['DATE'], monthly_sales['REVENUE_AMOUNT'])
    plt.title('Monthly Ticket Sales Trend')
    plt.xlabel('Month')
    plt.ylabel('Total Sales Amount')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()
    
    month_avg = df.groupby('MONTH')['REVENUE_AMOUNT'].mean()
    plt.figure(figsize=(12,6))
    month_avg.plot(kind='bar')
    plt.title('Average Sales by Month')
    plt.xlabel('Month')
    plt.ylabel('Average Sales Amount')
    plt.show()

if 'PAX_TYPE' in df.columns:
    pax_summary = df.groupby('PAX_TYPE')['REVENUE_AMOUNT'].agg(['mean', 'sum', 'count']).round(2)
    pax_summary.columns = ['Average Amount', 'Total Revenue', 'Ticket Count']
    print("Passenger Type Summary:")
    print(pax_summary)
    
    plt.figure(figsize=(10,6))
    pax_summary['Ticket Count'].plot(kind='pie', autopct='%1.1f%%')
    plt.title('Passenger Type Distribution')
    plt.ylabel('')
    plt.show()
    
    if 'FFP_FLAG' in df.columns:
        loyalty_summary = df.groupby('FFP_FLAG')['REVENUE_AMOUNT'].agg(['mean', 'count'])
        print("\nLoyalty Program Summary:")
        print(loyalty_summary)

if 'FOP_TYPE_CODE' in df.columns:
    payment_summary = df.groupby('FOP_TYPE_CODE')['REVENUE_AMOUNT'].agg(['mean', 'sum', 'count']).round(2)
    payment_summary.columns = ['Average Amount', 'Total Revenue', 'Transaction Count']
    print("\nPayment Method Summary:")
    print(payment_summary)
    
    plt.figure(figsize=(12,8))
    df['FOP_TYPE_CODE'].value_counts().plot(kind='pie', autopct='%1.1f%%')
    plt.title('Payment Method Distribution')
    plt.ylabel('')
    plt.show()
    
    top_payments = payment_summary.nlargest(5, 'Total Revenue')
    plt.figure(figsize=(12,6))
    top_payments['Total Revenue'].plot(kind='bar')
    plt.title('Top 5 Payment Methods by Revenue')
    plt.xlabel('Payment Method')
    plt.ylabel('Total Revenue')
    plt.xticks(rotation=45)
    plt.show()

if 'ROUTE_FLIGHT_TYPE' in df.columns:
    flight_type_summary = df.groupby('ROUTE_FLIGHT_TYPE')['REVENUE_AMOUNT'].agg(['mean', 'sum', 'count'])
    print("\nFlight Type Summary:")
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
    plt.plot(daily_sales['ISSUE_DATE'], y, label='Actual', alpha=0.7)
    plt.plot(daily_sales['ISSUE_DATE'], predictions, label='Predicted', linestyle='--')
    plt.title('Ticket Sales Prediction (Linear Regression)')
    plt.xlabel('Date')
    plt.ylabel('Sales Amount')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.show()

    mae = mean_absolute_error(y, predictions)
    print(f'Mean Absolute Error for Sales Prediction: {mae:.2f}')
    
    future_days = pd.DataFrame({
        'DAY_INDEX': range(len(daily_sales), len(daily_sales) + 30)
    })
    future_predictions = model.predict(future_days)
    print(f"Predicted sales for next 30 days: {future_predictions.mean():.2f} (average)")

numeric_cols = df.select_dtypes(include=[np.number]).columns
if len(numeric_cols) > 1:
    correlation_matrix = df[numeric_cols].corr()
    plt.figure(figsize=(10,8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
    plt.title('Correlation Matrix of Numerical Features')
    plt.show()

if 'SALE_TYPE' in df.columns:
    sale_type_summary = df.groupby('SALE_TYPE')['REVENUE_AMOUNT'].agg(['mean', 'sum', 'count'])
    print("\nSale Type Summary:")
    print(sale_type_summary)