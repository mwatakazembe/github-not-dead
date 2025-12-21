import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import warnings
warnings.filterwarnings('ignore')

try:
    df = pd.read_excel('lab_4_part_5.xlsx', header=1)
    print('data loaded successfully')
except FileNotFoundError:
    print('error: file lab_4_part_5.xlsx not found')
    exit()

required_columns = ['Дата', 'Год', 'Год-мес', 'точка', 'бренд', 'товар', 'Количество', 'Продажи', 'Себестоимость']
missing_columns = [col for col in required_columns if col not in df.columns]
if missing_columns:
    print(f'error: missing columns: {missing_columns}')
    exit()

df = df.rename(columns={
    'Дата': 'date',
    'Год': 'year',
    'Год-мес': 'year_month',
    'точка': 'point_id',
    'бренд': 'brand',
    'товар': 'product',
    'Количество': 'quantity',
    'Продажи': 'revenue',
    'Себестоимость': 'cost'
})

df['date'] = pd.to_datetime(df['date'])
df['profit'] = df['revenue'] - df['cost']
df['price'] = df['revenue'] / df['quantity']
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

plt.figure(figsize=(12, 8))
for product in df['product'].unique():
    product_data = product_sales[product_sales['product'] == product]
    plt.plot(product_data['date'], product_data['quantity'], label=product, marker='o')
plt.title('sales dynamics by product')
plt.xlabel('date')
plt.ylabel('quantity')
plt.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 8))
for point in df['point_id'].unique()[:5]:
    point_data = point_sales[point_sales['point_id'] == point]
    plt.plot(point_data['date'], point_data['revenue'], label=f'point {point}', marker='s')
plt.title('revenue dynamics by point')
plt.xlabel('date')
plt.ylabel('revenue')
plt.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 8))
total_turnover = df.groupby('date')['revenue'].sum()
plt.plot(total_turnover.index, total_turnover.values, color='red', linewidth=2)
plt.title('total turnover dynamics')
plt.xlabel('date')
plt.ylabel('revenue')
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 8))
price_trends = df.groupby('product')['price'].mean()
plt.bar(price_trends.index, price_trends.values)
plt.title('average prices by product')
plt.xlabel('product')
plt.ylabel('price')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

product_forecasts = {}
products = df['product'].unique()
num_products = len(products)

for i in range(0, num_products, 4):
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    axes = axes.flatten()
    
    for j in range(4):
        if i + j >= num_products:
            axes[j].set_visible(False)
            continue
            
        product = products[i + j]
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
            
            axes[j].plot(product_data['date'], y, label='historical data', marker='o')
            future_dates = [product_data['date'].max() + pd.Timedelta(days=30*i) for i in range(1, 4)]
            axes[j].plot(future_dates, forecast, label='forecast', marker='s', linestyle='--')
            axes[j].set_title(f'sales forecast for {product}')
            axes[j].set_xlabel('date')
            axes[j].set_ylabel('quantity')
            axes[j].legend()
    
    plt.tight_layout()
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

print('analysis completed')