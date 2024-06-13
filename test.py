import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados
df = pd.read_excel("cli_melhores_compras.xlsx")

# Remover valores negativos de "valor ticket médio"
df = df[df['valor ticket médio'] >= 0]

