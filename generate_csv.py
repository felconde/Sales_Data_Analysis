import pandas as pd
import numpy as np

# Definir a lista de produtos em inglês
products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']

# Definir a quantidade de registros
num_records = 50

# Gerar dados aleatórios para as colunas Product e Value
data = {
    'Product': np.random.choice(products, num_records),
    'Value': np.random.randint(100, 1000, num_records)
}

# Criar o DataFrame
df = pd.DataFrame(data)

# Salvar o DataFrame em um arquivo CSV
df.to_csv('sales_data.csv', index=False)
