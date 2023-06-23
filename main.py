import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the CSV file with sales data
sales_data = pd.read_csv('sales_data.csv')

# Display the first few rows of the DataFrame to verify if the data was loaded correctly
print(sales_data.head())

# Calculate and display basic statistics of the sales data
print('\nBasic sales statistics:')
print('Mean sales:', sales_data['Value'].mean())
print('Maximum sales:', sales_data['Value'].max())
print('Minimum sales:', sales_data['Value'].min())
print('Total sales:', sales_data['Value'].sum())

# Create a bar chart to visualize sales by product
products = sales_data['Product']
sales = sales_data['Value']

plt.bar(products, sales)
plt.xlabel('Product')
plt.ylabel('Sales Value')
plt.title('Sales by Product')
plt.xticks(rotation=45)
plt.show()
