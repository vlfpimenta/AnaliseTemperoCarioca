import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title('Análise de Vendas de Bebidas')

# entrada dos dados via CSV
file_path = "trabalho_big_data.csv"
df = pd.read_csv(file_path)

df['Quantidade_Mensal_Vendida'] = df['Quantidade'] * 2

df['Margem de Lucro (%)'] = ((df['PrecoVenda'] - df['PrecoCompra']) / df['PrecoCompra']) * 100 
df['Margem de Lucro (%)'] = df['Margem de Lucro (%)'].round(2)

st.write('## Visão Geral dos Dados')
st.write(df)

# -----------------------

st.write('## Quantidade Mensal de Vendas por Produto')
bar_chart = st.bar_chart(df[['Produto', 'Quantidade_Mensal_Vendida']].set_index('Produto'))

# ------------------------

st.write('## Distribuição de Vendas por Produto')
fig, ax = plt.subplots(figsize=(11, 11))
ax.pie(df['Quantidade_Mensal_Vendida'], labels=df['Produto'], autopct='%1.0f%%', startangle=90)
ax.axis('equal')
st.pyplot(fig)

# ------------------------

produto_mais_caro = df.loc[df['PrecoVenda'].idxmax()]
produto_mais_barato = df.loc[df['PrecoVenda'].idxmin()]

st.write('## Produto Mais Caro')
st.write(produto_mais_caro)

st.write('## Produto Mais Barato')
st.write(produto_mais_barato)

# ------------------------

tipos_de_produtos = df['Produto'].apply(lambda x: x.split(' ', 1)[0]).unique()

st.write('## Comparação entre Tipos de Produtos')
for tipo in tipos_de_produtos:
     produtos_do_tipo = df[df['Produto'].str.startswith(tipo)]
     st.write(f'### {tipo.capitalize()}s')
     st.write(produtos_do_tipo[['Produto', 'Quantidade_Mensal_Vendida', 'PrecoCompra', 'PrecoVenda', 'Margem de Lucro (%)']])

# ------------------------ GRÁFICO 1 ------------------------

df_sorted = df.sort_values(by='Quantidade_Mensal_Vendida', ascending=True)

st.write('## 1 - Quantidade Mensal Vendida por Bebida')

fig, ax = plt.subplots(figsize=(10, 8))
bar_chart_preco_compra = ax.barh(df_sorted['Produto'], df_sorted['Quantidade_Mensal_Vendida'], color='skyblue')
for index, value in enumerate(df_sorted['Quantidade_Mensal_Vendida']):
    ax.text(value, index, value, ha='left', va='center', fontsize=8)

ax.set_xlabel('Quantidade')
ax.set_ylabel('Produto')
ax.set_title('Quantidade Mensal Vendida por Bebida (Ordenado do Maior para o Menor)')
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot(fig)

# ------------------------ GRÁFICO 2 ------------------------

df_sorted = df.sort_values(by='PrecoCompra', ascending=True)

st.write('## 2 - Preço Unitário de Compra por Bebida')

fig, ax = plt.subplots(figsize=(10, 8))
bar_chart_preco_compra = ax.barh(df_sorted['Produto'], df_sorted['PrecoCompra'], color='red')
for index, value in enumerate(df_sorted['PrecoCompra']):
    ax.text(value, index, f'R$ {value:.2f}', ha='left', va='center', fontsize=8)

ax.set_xlabel('Preço Unitário de Compra')
ax.set_ylabel('Produto')
ax.set_title('Preço Unitário de Compra por Bebida (Ordenado do Maior para o Menor)')
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot(fig)

# ------------------------ GRÁFICO 3 ------------------------

df_sorted = df.sort_values(by='PrecoVenda', ascending=True)

st.write('## 3 - Preço Unitário de Venda por Bebida')

fig, ax = plt.subplots(figsize=(10, 8))
bar_chart_preco_venda = ax.barh(df_sorted['Produto'], df_sorted['PrecoVenda'], color='green')
for index, value in enumerate(df_sorted['PrecoVenda']):
    ax.text(value, index, f'R$ {value:.2f}', ha='left', va='center', fontsize=8)

ax.set_xlabel('Preço Unitário de Venda')
ax.set_ylabel('Produto')
ax.set_title('Preço Unitário de Venda por Bebida (Ordenado do Maior para o Menor)')
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot(fig)

# ------------------------ GRÁFICO 4 ------------------------

df['Lucro_Unitario'] = df['PrecoVenda'] - df['PrecoCompra']
df_sorted_lucro = df.sort_values(by='Lucro_Unitario', ascending=True)

st.write('## 4 - Lucro Unitário por Bebida')

#fig, ax = plt.subplots(figsize=(10, 8))
fig_lucro, ax_lucro = plt.subplots(figsize=(10, 8))
bar_chart_lucro = ax_lucro.barh(df_sorted_lucro['Produto'], df_sorted_lucro['Lucro_Unitario'], color='aquamarine')
for index, value in enumerate(df_sorted_lucro['Lucro_Unitario']):
    ax_lucro.text(value, index, f'R$ {value:.2f}', ha='left', va='center', fontsize=8)

ax_lucro.set_xlabel('Lucro Unitário')
ax_lucro.set_ylabel('Produto')
ax_lucro.set_title('Lucro Unitário por Bebida (Ordenado do Maior para o Menor)')
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot(fig_lucro)

# ------------------------ GRÁFICO 5 ------------------------

df['Lucro_Mensal_por_Bebida'] = df['Quantidade'] * (df['PrecoVenda'] - df['PrecoCompra']) * 2

# df['Lucro Mensal Unitário'] = df['PrecoVenda'] * 2 - df['PrecoCompra']
df_sorted_lucro = df.sort_values(by='Lucro_Mensal_por_Bebida', ascending=True)

st.write('## 5 - Lucro Mensal por Bebida')

fig_lucro, ax_lucro = plt.subplots(figsize=(10, 8))
bar_chart_lucro = ax_lucro.barh(df_sorted_lucro['Produto'], df_sorted_lucro['Lucro_Mensal_por_Bebida'], color='gray')
for index, value in enumerate(df_sorted_lucro['Lucro_Mensal_por_Bebida']):
    ax_lucro.text(value, index, f'R$ {value:.2f}', ha='left', va='center', fontsize=8)

ax_lucro.set_xlabel('Lucro_Mensal_por_Bebida')
ax_lucro.set_ylabel('Produto')
ax_lucro.set_title('Lucro Mensal por Bebida (Ordenado do Maior para o Menor)')
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot(fig_lucro)

# -----------------

df['Periodo'] = (df.index // 4) + 1
df['Lucro Mensal'] = df['Quantidade_Mensal_Vendida'] * (df['PrecoVenda'] - df['PrecoCompra'])
lucro_mensal_total = df.groupby('Periodo')['Lucro Mensal'].sum().sum()
bebida_mais_lucrativa = df.groupby('Produto')['Lucro Mensal'].sum().idxmax()
bebida_menos_lucrativa = df.groupby('Produto')['Lucro Mensal'].sum().idxmin()
bebida_mais_vendida = df.groupby('Produto')['Quantidade_Mensal_Vendida'].sum().idxmax()
bebida_menos_vendida = df.groupby('Produto')['Quantidade_Mensal_Vendida'].sum().idxmin()

st.write('## Resultados da Análise')
st.write(f'**Lucro Mensal Total:** R$ {lucro_mensal_total:.2f}')
st.write(f'**Bebida Mais Lucrativa:** {bebida_mais_lucrativa} (Lucro Total: R$ {df.groupby("Produto")["Lucro Mensal"].sum().max():.2f})')
st.write(f'**Bebida Menos Lucrativa:** {bebida_menos_lucrativa} (Lucro Total: R$ {df.groupby("Produto")["Lucro Mensal"].sum().min():.2f})')
st.write(f'**Bebida Mais Vendida:** {bebida_mais_vendida} (Quantidade Vendida: {df.groupby("Produto")["Quantidade_Mensal_Vendida"].sum().max()})')
st.write(f'**Bebida Menos Vendida:** {bebida_menos_vendida} (Quantidade Vendida: {df.groupby("Produto")["Quantidade_Mensal_Vendida"].sum().min()})')

# -------------------------------