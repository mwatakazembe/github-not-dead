import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import warnings
warnings.filterwarnings('ignore')

try:
    df = pd.read_excel('lab_4_part5.xlsx')
    print('data loaded successfully')
except FileNotFoundError:
    print('error: file lab_4_part5.xlsx not found')
    exit()

print(f'dataset shape: {df.shape}')
print(df.head())

df['date'] = pd.to_datetime(df['date'])
df['revenue'] = df['quantity'] * df['price']
df['profit'] = df['revenue'] - df['cost']
df['average_price'] = df['price']
df['sales_per_point'] = df['quantity'] / df['point_id'].nunique()

product_sales = df.groupby(['product', 'date']).agg({
    'quantity': 'sum',
    'revenue': 'sum',
    'cost': 'sum',
    'price': 'mean'
}).reset_index()

point_sales = df.groupby(['point_id', 'date']).agg({
    'quantity': 'sum',
    'revenue': 'sum',
    'cost': 'sum',
    'price': 'mean'
}).reset_index()

plt.figure(figsize=(15, 10))

plt.subplot(2, 2, 1)
for product in df['product'].unique():
    product_data = product_sales[product_sales['product'] == product]
    plt.plot(product_data['date'], product_data['quantity'], label=product, marker='o')
plt.title('sales dynamics by product')
plt.xlabel('date')
plt.ylabel('quantity')
plt.legend()

plt.subplot(2, 2, 2)
for point in df['point_id'].unique()[:5]:
    point_data = point_sales[point_sales['point_id'] == point]
    plt.plot(point_data['date'], point_data['revenue'], label=f'point {point}', marker='s')
plt.title('revenue dynamics by point')
plt.xlabel('date')
plt.ylabel('revenue')
plt.legend()

plt.subplot(2, 2, 3)
total_turnover = df.groupby('date')['revenue'].sum()
plt.plot(total_turnover.index, total_turnover.values, color='red', linewidth=2)
plt.title('total turnover dynamics')
plt.xlabel('date')
plt.ylabel('revenue')

plt.subplot(2, 2, 4)
price_trends = df.groupby('product')['price'].mean()
plt.bar(price_trends.index, price_trends.values)
plt.title('average prices by product')
plt.xlabel('product')
plt.ylabel('price')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

product_forecasts = {}
for product in df['product'].unique():
    product_data = product_sales[product_sales['product'] == product].copy()
    product_data['days'] = (product_data['date'] - product_data['date'].min()).dt.days
    
    if len(product_data) > 1:
        X = product_data[['days']]
        y = product_data['quantity']
        
        model = LinearRegression()
        model.fit(X, y)
        future_days = np.array([X['days'].max() + i*30 for i in range(1, 4)]).reshape(-1, 1)
        forecast = model.predict(future_days)
        product_forecasts[product] = forecast
        
        plt.figure(figsize=(10, 4))
        plt.plot(product_data['date'], y, label='historical data', marker='o')
        future_dates = [product_data['date'].max() + pd.Timedelta(days=30*i) for i in range(1, 4)]
        plt.plot(future_dates, forecast, label='forecast', marker='s', linestyle='--')
        plt.title(f'sales forecast for {product}')
        plt.xlabel('date')
        plt.ylabel('quantity')
        plt.legend()
        plt.show()

growth_analysis = df.groupby('product').agg({
    'quantity': ['sum', 'mean'],
    'revenue': 'sum',
    'cost': 'sum'
}).round(2)
growth_analysis.columns = ['total_quantity', 'avg_quantity', 'total_revenue', 'total_cost']
growth_analysis['profit_margin'] = ((growth_analysis['total_revenue'] - growth_analysis['total_cost']) / growth_analysis['total_revenue'] * 100).round(2)

print(growth_analysis)

point_efficiency = df.groupby('point_id').agg({
    'quantity': 'sum',
    'revenue': 'sum',
    'profit': 'sum'
}).round(2)
point_efficiency['efficiency'] = (point_efficiency['profit'] / point_efficiency['revenue'] * 100).round(2)

plt.figure(figsize=(12, 6))
plt.bar(point_efficiency.index.astype(str), point_efficiency['efficiency'])
plt.title('profit efficiency by point')
plt.xlabel('point id')
plt.ylabel('efficiency (%)')
plt.show()

print('analysis completed')