import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel("cli_melhores_compras.xlsx")


# Dados Missing e Duplicados
missing_data = df.isnull().sum()
print("Dados Missing:\n", missing_data)

duplicated_data = df.duplicated().sum()
print(f"\nDuplicated rows: {duplicated_data}")

# Remover valores 0 e negativos de "valor ticket médio"
df = df[df['valor ticket médio'] > 0]

# Remover valores 0 e negativos de "Idade"
df = df[df['Idade'] > 0]

# Remover valores de "Idade" acima de 87
df = df[df['Idade'] <= 87]

# Análise de Outliers na Coluna Idade
idade_stats = df['Idade'].describe()
print("\nEstatísticas Descritivas da Idade:\n", idade_stats)

Q1 = idade_stats['25%']
Q3 = idade_stats['75%']
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[(df['Idade'] < lower_bound) | (df['Idade'] > upper_bound)]
print("\nOutliers na Idade:\n", outliers)

# Visualização da distribuição de Idade
plt.figure(figsize=(10, 6))
plt.hist(df['Idade'], bins=50, color='skyblue', edgecolor='black')
plt.title('Distribuição da Idade')
plt.xlabel('Idade')
plt.ylabel('Frequência')
plt.show()

# Consistência dos Dados de Valor Ticket Médio
ticket_stats = df['valor ticket médio'].describe()
print("\nEstatísticas Descritivas do Valor Ticket Médio:\n", ticket_stats)

# Remover valores extremamente altos (acima do percentil 99)
df = df[df['valor ticket médio'] <= df['valor ticket médio'].quantile(0.99)]

ticket_stats_clean = df['valor ticket médio'].describe()
print("\nEstatísticas Descritivas do Valor Ticket Médio (Após Limpeza):\n", ticket_stats_clean)

# Análise por Faixa Etária
bins = [18, 24, 34, 44, 54, 64, 100]
labels = ['18-24', '25-34', '35-44', '45-54', '55-64', '65+']
df['Faixa Etária'] = pd.cut(df['Idade'], bins=bins, labels=labels, right=False)

faixa_stats = df.groupby('Faixa Etária').agg({
    'Idade': ['mean', 'var', 'std'],
    'valor ticket médio': ['mean', 'median']
}).reset_index()
print("\nEstatísticas por Faixa Etária:\n", faixa_stats)

# Ranking das vendas por faixa etária
faixa_vendas = df['Faixa Etária'].value_counts().sort_index()
print("\nRanking das Vendas por Faixa Etária:\n", faixa_vendas)

# Visualização do valor ticket médio por faixa etária
plt.figure(figsize=(12, 8))
df.boxplot(column='valor ticket médio', by='Faixa Etária', grid=False)
plt.title('Valor Ticket Médio por Faixa Etária')
plt.suptitle('')
plt.xlabel('Faixa Etária')
plt.ylabel('Valor Ticket Médio')
plt.show()

# Calcular a correlação entre Idade e valor ticket médio
correlation = df[['Idade', 'valor ticket médio']].corr()
print("\nCorrelação entre Idade e Valor Ticket Médio:\n", correlation)

# Visualização da correlação usando heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Heatmap da Correlação entre Idade e Valor Ticket Médio')
plt.show()


# Distribuição de Clientes por Região
regiao_counts = df['Região País'].value_counts()
print("\nDistribuição de Clientes por Região:\n", regiao_counts)

plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Região País', palette='viridis')
plt.title('Distribuição de Clientes por Região')
plt.xlabel('Região')
plt.ylabel('Contagem de Clientes')
plt.show()

# Valor ticket médio por Região
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='Região País', y='valor ticket médio', palette='viridis')
plt.title('Valor Ticket Médio por Região')
plt.xlabel('Região')
plt.ylabel('Valor Ticket Médio')
plt.show()

# Distribuição de Clientes por Estado
estado_counts = df['Estado'].value_counts()
print("\nDistribuição de Clientes por Estado:\n", estado_counts)

plt.figure(figsize=(12, 8))
sns.countplot(data=df, x='Estado', palette='viridis')
plt.title('Distribuição de Clientes por Estado')
plt.xlabel('Estado')
plt.ylabel('Contagem de Clientes')
plt.xticks(rotation=90)
plt.show()

# Valor ticket médio por Estado
plt.figure(figsize=(12, 8))
sns.boxplot(data=df, x='Estado', y='valor ticket médio', palette='viridis')
plt.title('Valor Ticket Médio por Estado')
plt.xlabel('Estado')
plt.ylabel('Valor Ticket Médio')
plt.xticks(rotation=90)
plt.show()

# Distribuição de Clientes por Sexo
sexo_counts = df['Sexo Informado Cliente'].value_counts()
print("\nDistribuição de Clientes por Sexo:\n", sexo_counts)

plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Sexo Informado Cliente', palette='viridis')
plt.title('Distribuição de Clientes por Sexo')
plt.xlabel('Sexo')
plt.ylabel('Contagem de Clientes')
plt.show()

# Valor ticket médio por Sexo
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='Sexo Informado Cliente', y='valor ticket médio', palette='viridis')
plt.title('Valor Ticket Médio por Sexo')
plt.xlabel('Sexo')
plt.ylabel('Valor Ticket Médio')
plt.show()