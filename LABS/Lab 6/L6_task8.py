import pandas as pd

# a
p = pd.read_csv("product.csv")
o = pd.read_csv("order.csv")

# b
print(p.head(), o.head())
print(p.tail(10), o.tail(10))


# c
merged = pd.merge(p, o, how="inner", on="ProductID")

total_revenue = (merged['Quantity'] * merged['Price']).sum()
print(total_revenue)


# f
category = p.groupby('Category')
print(category['Price'].mean()) 

# i

print(merged.dropna())


# g

merged['Date'] = pd.to_datetime(merged['Date']) 
merged['Day'] = merged['Date'].dt.day
merged['Month'] = merged['Date'].dt.month
merged['Year'] = merged['Date'].dt.year

daily_revenue = merged.groupby(['Year', 'Month', 'Day'])[['Quantity', 'Price']].apply(lambda x: (x['Quantity'] * x['Price']).sum()).reset_index(name='TotalRevenue')
daily_revenue_max = daily_revenue.loc[daily_revenue['TotalRevenue'].idxmax()]

print("Day, Month, Year with highest total revenue:")
print(f"Day: {daily_revenue_max['Day']}, Month: {daily_revenue_max['Month']}, Year: {daily_revenue_max['Year']}")

 # h
monthly_revenue = merged.groupby(['Year', 'Month'])[['Quantity', 'Price']].apply(lambda x: (x['Quantity'] * x['Price']).sum()).reset_index(name='TotalRevenue')
print("\nMonthly revenue:")
print(monthly_revenue)



product_sales = merged.groupby('ProductID')['Quantity'].sum().reset_index(name='TotalQuantity')
product_sales.sort_values(by='TotalQuantity', ascending=False, inplace=True)

print("\nTop 5 best-selling products:")
print(product_sales.head(5))

print("\nTop 5 low-selling products:")
print(product_sales.tail(5))

top_products = product_sales.head(5)
top_product_categories = merged[merged['ProductID'].isin(top_products['ProductID'])].groupby('Category').size().reset_index(name='Count')
top_product_categories.sort_values(by='Count', ascending=False, inplace=True)

print("\nMost common product category among top 5 best-selling products:")
print(top_product_categories.head(1))