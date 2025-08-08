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

df_limpo.head()

df_limpo['nível_experiência'].value_counts().plot(kind='bar', title="Distribuição de senioridade")

import seaborn as sns

sns.barplot(data=df_limpo, x='nível_experiência', y='salário_em_usd')

import matplotlib.pyplot as plt

plt.figure(figsize=(8,5))
sns.barplot(data=df_limpo, x='nível_experiência', y='salário_em_usd')
plt.title("Salário médio por senioridade")
plt.xlabel("Senioridade")
plt.ylabel("Salário médio anual (USD)")
plt.show()

df_limpo.groupby('nível_experiência')['salário_em_usd'].mean().sort_values(ascending=False)

ordem = df_limpo.groupby('nível_experiência')['salário_em_usd'].mean().sort_values(ascending=True).index

ordem

plt.figure(figsize=(8,5))
sns.barplot(data=df_limpo, x='nível_experiência', y='salário_em_usd', order=ordem)
plt.title("Salário médio por senioridade")
plt.xlabel("Senioridade")
plt.ylabel("Salário médio anual (USD)")
plt.show()

plt.figure(figsize=(10,5))
sns.histplot(df_limpo['salário_em_usd'], bins = 50, kde=True)
plt.title("Distribuição dos salários anuais")
plt.xlabel("Salário em USD")
plt.ylabel("Frequência")
plt.show()

plt.figure(figsize=(8,5))
sns.boxplot(x=df_limpo['salário_em_usd'])
plt.title("Boxplot Salário")
plt.xlabel("Salário em USD")
plt.show()

ordem_senioridade = ['junior', 'pleno', 'senior', 'executivo']

plt.figure(figsize=(8,5))
sns.boxplot(x='nível_experiência', y='salário_em_usd', data=df_limpo, order=ordem_senioridade)
plt.title("Boxplot da distribuição por senioridade")
plt.xlabel("Salário em USD")
plt.show()

ordem_senioridade = ['junior', 'pleno', 'senior', 'executivo']

plt.figure(figsize=(8,5))
sns.boxplot(x='nível_experiência', y='salário_em_usd', data=df_limpo, order=ordem_senioridade, palette='Set2', hue='nível_experiência')
plt.title("Boxplot da distribuição por senioridade")
plt.xlabel("Salário em USD")
plt.show()

import plotly.express as px

senioridade_media_salario = df_limpo.groupby('nível_experiência')['salário_em_usd'].mean().sort_values(ascending=False).reset_index()

fig = px.bar(senioridade_media_salario,
             x='nível_experiência',
             y='salário_em_usd',
             title='Média Salarial por Senioridade',
             labels={'nível_experiência': 'Nível de Senioridade', 'salário_em_usd': 'Média Salarial Anual (USD)'})

fig.show()

remoto_contagem = df_limpo['taxa_remoto'].value_counts().reset_index()
remoto_contagem.columns = ['tipo_trabalho', 'quantidade']

fig = px.pie(remoto_contagem,
             names='tipo_trabalho',
             values='quantidade',
             title='Proporção dos tipos de trabalho'
          )

fig.show()

remoto_contagem = df_limpo['taxa_remoto'].value_counts().reset_index()
remoto_contagem.columns = ['tipo_trabalho', 'quantidade']

fig = px.pie(remoto_contagem,
             names='tipo_trabalho',
             values='quantidade',
             title='Proporção dos tipos de trabalho',
             hole=0.5
          )

fig.show()

remoto_contagem = df_limpo['taxa_remoto'].value_counts().reset_index()
remoto_contagem.columns = ['tipo_trabalho', 'quantidade']

fig = px.pie(remoto_contagem,
             names='tipo_trabalho',
             values='quantidade',
             title='Proporção dos tipos de trabalho',
             hole=0.5
          )
fig.update_traces(textinfo='percent+label')
fig.show()

df.head()

pip install pycountry

import pycountry

def iso2_to_iso3(code):
    try:
        return pycountry.countries.get(alpha_2=code).alpha_3
    except:
        return None

df_limpo['residencia_iso3'] = df_limpo['residência'].apply(iso2_to_iso3)

df_ds = df_limpo[df_limpo['cargo'] == 'Data Scientist']
media_ds_pais = df_ds.groupby('residencia_iso3')['salário_em_usd'].mean().reset_index()

fig = px.choropleth(media_ds_pais,
                    locations='residencia_iso3',
                    color='salário_em_usd',
                    color_continuous_scale='rdylgn',
                    title='Salário médio de Cientista de Dados por país',
                    labels={'salário_em_usd': 'Salário médio (USD)', 'residencia_iso3': 'País'})

fig.show()

df_limpo.head()

df_limpo.to_csv('dados-imersao-final.csv', index=False)
