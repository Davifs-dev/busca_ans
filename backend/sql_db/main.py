import pandas as pd

# Carregar o CSV
df = pd.read_csv('E:/Davi/Projetos/Testes IntuitiveCare/backend/sql_db/files/4T2024.csv', sep=';', encoding='utf-8')
print(df.head())
print(df.columns)
# Substituir as vírgulas por ponto nas colunas numéricas
df['VL_SALDO_INICIAL'] = df['VL_SALDO_INICIAL'].astype(str).str.replace(',', '.').astype(float)
df['VL_SALDO_FINAL'] = df['VL_SALDO_FINAL'].astype(str).str.replace(',', '.').astype(float)

# Converte a coluna de data para o formato correto
# df['DATA'] = pd.to_datetime(df['DATA'], format='%d/%m/%Y').dt.strftime('%Y-%m-%d')

# Salvar novamente o CSV com os valores corrigidos
df.to_csv('E:/Davi/Projetos/Testes IntuitiveCare/backend/sql_db/files/4T2024.csv', index=False, sep=';')
  
  