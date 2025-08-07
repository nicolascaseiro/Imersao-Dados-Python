import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")

linhas, colunas = df.shape[0], df.shape[1]

print(f'Linhas: {linhas}')
print(f'Colunas: {colunas}')

novos_nomes = {
    'work_year': 'ano',
    'experience_level': 'nível_experiência',
    'employment_type': 'tipo_contrato',
    'job_title': 'cargo',
    'salary': 'salário',
    'salary_currency': 'moeda_salário',
    'salary_in_usd': 'salário_em_usd',
    'employee_residence': 'residência',
    'remote_ratio': 'taxa_remoto',
    'company_location': 'localização_empresa',
    'company_size': 'tamanho_empresa'
}

df = df.rename(columns=novos_nomes)

nível_experiência = {
    'SE': 'senior',
    'MI': 'pleno',
    'EN': 'junior',
    'EX': 'executivo'
}
df['nível_experiência'] = df['nível_experiência'].replace(nível_experiência)

tipo_contrato = {
    'FT': 'integral',
    'PT': 'parcial',
    'CT': 'contrato',
    'FL': 'freelancer'
}
df['tipo_contrato'] = df['tipo_contrato'].replace(tipo_contrato)

tamanho_empresa = {
    'L': 'grande',
    'S': 'pequena',
    'M':	'media'

}
df['tamanho_empresa'] = df['tamanho_empresa'].replace(tamanho_empresa)

mapa_trabalho = {
    0: 'presencial',
    100: 'remoto',
    50: 'hibrido'
}

df['taxa_remoto'] = df['taxa_remoto'].replace(mapa_trabalho)


df.describe(include='object')

df.head()

df.isnull()

df.isnull().sum()

df['ano'].unique()

df[df.isnull().any(axis=1)]

import numpy as np

df_salarios = pd.DataFrame({
    'nome': ['Ana', 'Bruno', 'Carlos', 'Diana', 'Eduardo'],
    'salario': [4000, np.nan, 3500, np.nan, 5000]
})

df_salarios['salario_media'] = df_salarios['salario'].fillna(df_salarios['salario'].mean().round(2))

df_salarios['salario_mediana'] = df_salarios['salario'].fillna(df_salarios['salario'].median())

df_salarios

df_temperaturas = pd.DataFrame({
    'dia': ['Seg', 'Ter', 'Qua', 'Qui', 'Sex'],
    'temperatura': [30, np.nan, np.nan, 28, 27]
})

df_temperaturas['preenchido_ffill'] = df_temperaturas['temperatura'].ffill()

df_temperaturas

df_temperaturas = pd.DataFrame({
    'dia': ['Seg', 'Ter', 'Qua', 'Qui', 'Sex'],
    'temperatura': [30, np.nan, np.nan, 28, 27]
})

df_temperaturas['preenchido_bfill'] = df_temperaturas['temperatura'].bfill()

df_temperaturas

df_cidades = pd.DataFrame({
    'nome': ['Ana', 'Bruno', 'Carlos', 'Diana', 'Eduardo'],
    'cidade': ['São Paulo', np.nan, 'Curitiba', np.nan, 'Salvador']
})

df_cidades['cidade_corrigida'] = df_cidades['cidade'].fillna('Não informado')

df_cidades

df_limpo = df.dropna()

df_limpo.isnull().sum()

df_limpo.head()

df_limpo = df_limpo.assign(ano=df_limpo['ano'].astype('Int64'))
