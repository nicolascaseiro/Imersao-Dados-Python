import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")

df.head(10)

df.info()

df.describe()

df.shape

linhas, colunas = df.shape[0], df.shape[1]
print(f'Linhas: {linhas}')
print(f'Colunas: {colunas}')

df.columns

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

df.head(10)

df['nível_experiência'].value_counts()

df['tipo_contrato'].value_counts()

df['taxa_remoto'].value_counts()

df['tamanho_empresa'].value_counts()

nível_experiência = {
    'SE': 'senior',
    'MI': 'pleno',
    'EN': 'junior',
    'EX': 'executivo'
}
df['nível_experiência'] = df['nível_experiência'].replace(nível_experiência)
df['nível_experiência'].value_counts()

tipo_contrato = {
    'FT': 'integral',
    'PT': 'parcial',
    'CT': 'contrato',
    'FL': 'freelancer'
}
df['tipo_contrato'] = df['tipo_contrato'].replace(tipo_contrato)
df['tipo_contrato'].value_counts()

tamanho_empresa = {
    'L': 'grande',
    'S': 'pequena',
    'M':	'media'

}
df['tamanho_empresa'] = df['tamanho_empresa'].replace(tamanho_empresa)
df['tamanho_empresa'].value_counts()

mapa_trabalho = {
    0: 'presencial',
    100: 'remoto',
    50: 'hibrido'
}

df['taxa_remoto'] = df['taxa_remoto'].replace(mapa_trabalho)
df['taxa_remoto'].value_counts()

df.head(10)

df.describe(include='object')
