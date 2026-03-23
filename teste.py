import pandas as pd

pd.set_option('display.max_columns', None) # tirar limite de colunas para melhor vizualização
pd.set_option('display.expand_frame_repr', False) # não ter quebra de linhas

arquivo = 'Spotify_Youtube.csv'

df = pd.read_csv(arquivo, sep=',', index_col= None)

df = df.drop(['Instrumentalness','Liveness'], axis=1)

df = df.rename(columns={'Channel':'Canal'})

#print(df.isna().sum()) # verificação de dados que faltam
'''df['Title'] = df['Title'].fillna('Não se aplica')
print(df[df['Title'] == 'Não se aplica']) preenche os dados de title que faltam com "Não se aplica" '''

# df = df.drop_duplicates() - Remove dados duplicados

'''df['Key'] = df['Key'].astype(str)
print(df.dtypes) Conversão de tipo de dados, nesse caso de um dado float para object(string) '''

'''df_filtrado = df[df['Tempo']>100]
print(df_filtrado) Filtrando informações do df (Não é aconselhavel substituir o df principal, por isso criamos a variavel do df_filtrado) '''
