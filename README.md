# Análise de Dados de Clientes - Melhores Compras

Este projeto realiza uma análise detalhada do dataset `cli_melhores_compras.xlsx`, explorando características como idade, valor ticket médio, região, estado e sexo informado dos clientes. O objetivo é fornecer insights úteis para estratégias de negócio.

---

## 📁 Estrutura do Projeto

### 1. Tratamento de Dados
- Remoção de valores duplicados e dados inconsistentes.
- Limpeza de valores:
  - Exclusão de entradas com idade ou valor de ticket médio inválidos (negativos ou zero).
  - Limitação de idades a um máximo de 87 anos.
  - Exclusão de valores de ticket médio acima do percentil 99.

### 2. Análise Descritiva e Estatística
- Estatísticas descritivas para `Idade` e `valor ticket médio`.
- Identificação e tratamento de outliers na coluna `Idade`.
- Criação de faixas etárias para análise comparativa.

### 3. Visualizações
- **Distribuição de idade**: Histograma.
- **Correlação**: Heatmap entre `Idade` e `valor ticket médio`.
- **Faixas etárias**:
  - Boxplot do valor ticket médio.
  - Gráfico de barras com ranking por faixa etária.
- **Regiões, Estados e Sexo**:
  - Distribuição de clientes e análise do valor ticket médio.
  - Gráficos categóricos e comparativos.

---

## 🧰 Ferramentas Utilizadas

- **Linguagem**: Python
- **Bibliotecas**:
  - `pandas`: Manipulação de dados.
  - `numpy`: Análise numérica.
  - `matplotlib` e `seaborn`: Visualizações gráficas.

---

## 🗂️ Dataset

O dataset `cli_melhores_compras.xlsx` contém as seguintes colunas principais:
- **Idade**: Idade do cliente.
- **valor ticket médio**: Valor médio gasto pelo cliente.
- **Região País**: Região do cliente no país.
- **Estado**: Estado do cliente.
- **Sexo Informado Cliente**: Sexo do cliente.

---

## 📊 Análises Realizadas

### 1. **Tratamento de Missing e Duplicados**
- Contagem de valores ausentes e duplicados no dataset.
- Remoção de inconsistências nos dados.

### 2. **Distribuição de Idade**
- Estatísticas descritivas e visualizações da distribuição.
- Identificação de outliers utilizando o método IQR (Interquartile Range).

### 3. **Valor Ticket Médio**
- Estatísticas descritivas antes e após a limpeza de valores extremos.
- Visualização comparativa por faixa etária, região, estado e sexo.

### 4. **Correlação**
- Análise da correlação entre idade e valor ticket médio.
- Heatmap para visualização de correlações.

### 5. **Análise Categórica**
- Contagem e distribuição de clientes por:
  - Região
  - Estado
  - Sexo
- Boxplots para análise do valor ticket médio em cada categoria.

---

## 📈 Principais Visualizações

1. **Distribuição da Idade**:
   - Histograma com 50 intervalos.
2. **Correlação entre Idade e Valor Ticket Médio**:
   - Heatmap com valores de correlação.
3. **Valor Ticket Médio por Faixa Etária**:
   - Boxplot comparativo.
4. **Distribuição de Clientes por Região, Estado e Sexo**:
   - Gráficos de barras.
5. **Valor Ticket Médio por Categoria**:
   - Boxplots para análises detalhadas.

---

## 📌 Resultados e Insights

1. **Idade**:
   - A maior concentração de clientes está entre 25 e 44 anos.
   - Valores extremos (outliers) foram encontrados acima de 87 anos.

2. **Valor Ticket Médio**:
   - Valores extremos acima do percentil 99 foram removidos.
   - Faixas etárias mais jovens apresentam menor ticket médio, enquanto clientes de 45+ anos possuem maior valor médio.

3. **Distribuição Regional e por Estado**:
   - Algumas regiões possuem concentração significativamente maior de clientes.
   - Estados mais populosos lideram em número de clientes e valor ticket médio.

4. **Análise de Gênero**:
   - Diferenças observadas no ticket médio entre sexos indicam potencial para segmentação de marketing.

---

## 🚀 Como Executar o Projeto

1. **Clone o Repositório**:
   ```bash
   git clone https://github.com/JackCaolho/Analise-exploratoria-dataset-vendas.git
