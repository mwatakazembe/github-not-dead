import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

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
df['product_type'] = df['product'].str[:2]
df['profit'] = df['revenue'] - df['cost']
df['price'] = df['revenue'] / df['quantity']
df['sales_per_point'] = df['quantity'] / df['point_id'].nunique()

product_sales = df.groupby(['product_type', 'date']).agg({
    'quantity': 'sum',
    'revenue': 'sum',
    'cost': 'sum',
    'price': 'mean'
}).reset_index()

point_sales = df.groupby(['point_id', 'date']).agg({
    'quantity': 'sum',
    'revenue': 'sum',
    'cost': 'sum',
    'price': 'mean',
    'profit': 'sum'
}).reset_index()

plt.figure(figsize=(12, 8))
for product_type in df['product_type'].unique():
    product_data = product_sales[product_sales['product_type'] == product_type]
    plt.plot(product_data['date'], product_data['quantity'], label=product_type, marker='o')
plt.title('sales dynamics by product type')
plt.xlabel('date')
plt.ylabel('quantity')
plt.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 8))
for point in df['point_id'].unique()[:5]:
    point_data = point_sales[point_sales['point_id'] == point]
    plt.plot(point_data['date'], point_data['profit'], label=f'point {point}', marker='s') 
plt.title('profit by points')                    
plt.xlabel('date')
plt.ylabel('profit')                             
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
avg_price_by_type = df.groupby('product_type')['price'].mean().sort_values()
plt.bar(avg_price_by_type.index, avg_price_by_type.values)
plt.title('average prices by product type')
plt.xlabel('product type')
plt.ylabel('price')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

product_forecasts = {}
product_types = df['product_type'].unique()
num_types = len(product_types)

for i in range(0, num_types, 4):
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    axes = axes.flatten()
    
    for j in range(4):
        if i + j >= num_types:
            axes[j].set_visible(False)
            continue
            
        prod_type = product_types[i + j]
        prod_data = product_sales[product_sales['product_type'] == prod_type].copy()
        prod_data = prod_data.sort_values('date')
        prod_data['day_index'] = range(len(prod_data))
        
        if len(prod_data) > 1:
            X = prod_data[['day_index']]
            y = prod_data['quantity']
            
            model = LinearRegression()
            model.fit(X, y)
            
            historical_pred = model.predict(X)
            last_day = prod_data['day_index'].max()
            future_days = np.arange(last_day + 1, last_day + 31).reshape(-1, 1)
            future_pred = model.predict(future_days)
            future_dates = pd.date_range(start=prod_data['date'].max() + pd.Timedelta(days=1), periods=30)
            
            axes[j].plot(prod_data['date'], y, 'o-', label='actual', markersize=4)
            axes[j].plot(prod_data['date'], historical_pred, '--', label='trend (historical fit)', color='red')
            axes[j].plot(future_dates, future_pred, '--', label='forecast (30 days)', color='green')
            axes[j].set_title(f'sales forecast for type {prod_type}')
            axes[j].set_xlabel('date')
            axes[j].set_ylabel('quantity')
            axes[j].legend()
            
            product_forecasts[prod_type] = future_pred.mean()
        else:
            axes[j].text(0.5, 0.5, 'insufficient data', ha='center', va='center')
            axes[j].set_title(f'type {prod_type}')
    
    plt.tight_layout()
    plt.show()

print('\n30-day average sales forecast by product type:')
for prod_type, forecast_mean in product_forecasts.items():
    print(f'{prod_type}: {forecast_mean:.2f}')

point_efficiency = df.groupby('point_id').agg({
    'quantity': 'sum',
    'revenue': 'sum',
    'profit': 'sum'
}).round(2)
point_efficiency['efficiency'] = (point_efficiency['profit'] / point_efficiency['revenue'] * 100).round(2)

print('\npoint efficiency:')
print(point_efficiency)

print('\nanalysis completed.')