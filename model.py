# Importing Libraries:
import pandas as pd
import numpy as np
import pickle

# for displaying all feature from dataset:
pd.pandas.set_option('display.max_columns', None)

# Reading Dataset:
df  = pd.read_csv('consulta_cand_2020_GO.csv', delimiter=';',encoding="latin1", engine= 'python', error_bad_lines=False, decimal=',')
df1 = pd.read_csv('despesas_contratadas_candidatos_2020_GO.csv', delimiter=';',encoding="latin1", engine= 'python', error_bad_lines=False, decimal=',')
df2 = pd.read_csv('bem_candidato_2020_GO.csv', delimiter=';',encoding="latin1", engine= 'python', error_bad_lines=False, decimal=',')
df3 = pd.read_csv('votacao_candidato_munzona_2020_GO.csv', delimiter=';',encoding="latin1", engine= 'python', error_bad_lines=False, decimal=',')

# Dropping unneccsary feature :
df = df.drop(['DT_GERACAO','HH_GERACAO', 'CD_TIPO_ELEICAO','NM_TIPO_ELEICAO','NR_TURNO','CD_ELEICAO','DS_ELEICAO',
             'DT_ELEICAO','TP_ABRANGENCIA','NM_UE', 'DS_CARGO','NR_CANDIDATO','NM_SOCIAL_CANDIDATO',
             'NM_CANDIDATO','NM_URNA_CANDIDATO','NR_CPF_CANDIDATO','NM_EMAIL','DS_SITUACAO_CANDIDATURA',
             'DS_DETALHE_SITUACAO_CAND','TP_AGREMIACAO','SG_PARTIDO','NM_PARTIDO','SQ_COLIGACAO','NM_COLIGACAO',
             'DS_COMPOSICAO_COLIGACAO','CD_NACIONALIDADE','DS_NACIONALIDADE','SG_UF_NASCIMENTO','CD_MUNICIPIO_NASCIMENTO',
             'NM_MUNICIPIO_NASCIMENTO','DT_NASCIMENTO','NR_TITULO_ELEITORAL_CANDIDATO','DS_GENERO','DS_GRAU_INSTRUCAO',
             'DS_ESTADO_CIVIL','DS_COR_RACA','DS_SIT_TOT_TURNO','NR_PROTOCOLO_CANDIDATURA','NR_PROCESSO','DS_SITUACAO_CANDIDATO_PLEITO',
             'DS_SITUACAO_CANDIDATO_URNA'], axis=1)

df1 = df1.drop(['DT_GERACAO','HH_GERACAO','ANO_ELEICAO' ,'CD_TIPO_ELEICAO','NM_TIPO_ELEICAO','CD_ELEICAO','DS_ELEICAO',
                'DT_ELEICAO','ST_TURNO' ,'TP_PRESTACAO_CONTAS','DT_PRESTACAO_CONTAS','SQ_PRESTADOR_CONTAS', 'SG_UF','NM_UE',
                'NR_CNPJ_PRESTADOR_CONTA' ,'DS_CARGO','NR_CANDIDATO', 'NM_CANDIDATO',
                'NR_CPF_CANDIDATO','NR_CPF_VICE_CANDIDATO',
                'SG_PARTIDO','NM_PARTIDO','CD_TIPO_FORNECEDOR', 'DS_TIPO_FORNECEDOR', 'CD_CNAE_FORNECEDOR', 
                'DS_CNAE_FORNECEDOR', 'NR_CPF_CNPJ_FORNECEDOR', 'NM_FORNECEDOR', 'NM_FORNECEDOR_RFB', 'CD_ESFERA_PART_FORNECEDOR', 
                'DS_ESFERA_PART_FORNECEDOR', 'SG_UF_FORNECEDOR', 'CD_MUNICIPIO_FORNECEDOR', 'NM_MUNICIPIO_FORNECEDOR', 
                'SQ_CANDIDATO_FORNECEDOR', 'NR_CANDIDATO_FORNECEDOR', 'CD_CARGO_FORNECEDOR', 'DS_CARGO_FORNECEDOR', 'NR_PARTIDO_FORNECEDOR', 
                'SG_PARTIDO_FORNECEDOR', 'NM_PARTIDO_FORNECEDOR', 'DS_TIPO_DOCUMENTO', 'NR_DOCUMENTO', 'CD_ORIGEM_DESPESA', 
                'DS_ORIGEM_DESPESA', 'SQ_DESPESA', 'DT_DESPESA', 'DS_DESPESA' ],axis=1)

df2 = df2.drop(['DT_GERACAO','HH_GERACAO', 'CD_TIPO_ELEICAO','NM_TIPO_ELEICAO','CD_ELEICAO','DS_ELEICAO', 'DT_ELEICAO',
                'SG_UF','NM_UE', 'NR_ORDEM_CANDIDATO', 'CD_TIPO_BEM_CANDIDATO', 'DS_TIPO_BEM_CANDIDATO', 'DS_BEM_CANDIDATO', 
                'DT_ULTIMA_ATUALIZACAO', 'HH_ULTIMA_ATUALIZACAO' ],axis=1)

df3 = df3.drop(['DT_GERACAO','HH_GERACAO', 'CD_TIPO_ELEICAO','NM_TIPO_ELEICAO','NR_TURNO','CD_ELEICAO','DS_ELEICAO', 'DT_ELEICAO',
                'TP_ABRANGENCIA','SG_UF','NM_UE','NM_MUNICIPIO', 'DS_CARGO','NR_CANDIDATO','NM_SOCIAL_CANDIDATO', 'NM_CANDIDATO','NM_URNA_CANDIDATO',
                'DS_SITUACAO_CANDIDATURA', 'DS_DETALHE_SITUACAO_CAND','TP_AGREMIACAO','SG_PARTIDO','NM_PARTIDO','SQ_COLIGACAO','NM_COLIGACAO', 
                'DS_COMPOSICAO_COLIGACAO','CD_SIT_TOT_TURNO', 'DS_SIT_TOT_TURNO', 'ST_VOTO_EM_TRANSITO'],axis=1)

#Deletando as linhas referentes as cidades que não são objeto de estudo
indexNames = df[ (df['SG_UE'] != 93017)].index
df.drop(indexNames , inplace=True)

#Deletando as linhas referentes aos cargos que não são objeto de estudo
indexNames = df[ (df['CD_CARGO'] != 13)].index
df.drop(indexNames , inplace=True)

#Deletando as linhas referentes aos VALORES NULOS
indexNames = df[ (df['CD_SIT_TOT_TURNO'] == -1)].index
df.drop(indexNames , inplace=True)

# Fazer a substituição por valores numéricos
df['ST_REELEICAO'] = df['ST_REELEICAO'].replace(to_replace = {'S' : 1, 'N' : 0})
df['ST_DECLARAR_BENS'] = df['ST_DECLARAR_BENS'].replace(to_replace = {'S' : 1, 'N' : 0})
df['ST_CANDIDATO_INSERIDO_URNA'] = df['ST_CANDIDATO_INSERIDO_URNA'].replace(to_replace = {'SIM' : 1, 'N' : 0})

#Deletando as linhas referentes as cidades que não são objeto de estudo
indexNames = df1[ (df1['SG_UE'] != 93017)].index
df1.drop(indexNames , inplace=True)

#Deletando as linhas referentes aos cargos que não são objeto de estudo
indexNames = df1[ (df1['CD_CARGO'] != 13)].index
df1.drop(indexNames , inplace=True)

#Deletando as linhas referentes as cidades que não são objeto de estudo
indexNames = df2[ (df2['SG_UE'] != 93017)].index
df2.drop(indexNames , inplace=True)

#Deletando as linhas referentes as cidades que não são objeto de estudo
indexNames = df3[ (df3['SG_UE'] != 93017)].index
df3.drop(indexNames , inplace=True)

#Deletando as linhas referentes aos cargos que não são objeto de estudo
indexNames = df3[ (df3['CD_CARGO'] != 13)].index
df3.drop(indexNames , inplace=True)

#Deletando outras variáveis que não importam para o dataset
df1 = df1.drop(['SG_UE','CD_CARGO', 'NR_PARTIDO' ],axis=1)
df2 = df2.drop(['SG_UE','ANO_ELEICAO'],axis=1)
df3 = df3.drop(['SG_UE','CD_CARGO', 'NR_PARTIDO', 'ANO_ELEICAO', 'NR_ZONA', 'CD_SITUACAO_CANDIDATURA','CD_DETALHE_SITUACAO_CAND', 'CD_MUNICIPIO'],axis=1)

#Agrupando dados por candidato
a=df1.groupby(['SQ_CANDIDATO'], as_index=False).sum()
b=df2.groupby(['SQ_CANDIDATO'], as_index=False).sum()
c=df3.groupby(['SQ_CANDIDATO'], as_index=False).sum()

#anexando dados ao dataframe principal
df = df.set_index('SQ_CANDIDATO').join(a.set_index('SQ_CANDIDATO')).join(b.set_index('SQ_CANDIDATO')).join(c.set_index('SQ_CANDIDATO'))

#Preenchendo os valores missing por 0
df['VR_DESPESA_CONTRATADA'] = df['VR_DESPESA_CONTRATADA'].fillna(0)
df['VR_BEM_CANDIDATO'] = df['VR_BEM_CANDIDATO'].fillna(0)
df['QT_VOTOS_NOMINAIS'] = df['QT_VOTOS_NOMINAIS'].fillna(0)

#voltando index das linhas por inteiros
df = df.reset_index()

#Deletando ultimas variaveis
df = df.drop(['ANO_ELEICAO', 'SG_UF','CD_SITUACAO_CANDIDATURA','CD_DETALHE_SITUACAO_CAND','VR_DESPESA_MAX_CAMPANHA',
              'CD_SITUACAO_CANDIDATO_PLEITO','CD_SITUACAO_CANDIDATO_URNA','ST_CANDIDATO_INSERIDO_URNA','DS_OCUPACAO','ST_DECLARAR_BENS',
              'SG_UE','CD_CARGO','SQ_CANDIDATO'],axis=1)


# Separando as Variáveis Explicativas em "X" e o Target (a variável que queremos prever, em "Y"):
X = df.iloc[:, [True, True, True, True, True, True, True, False ,True,True, True,True] ]
y = df.iloc[:, 7]


# Train Test Split:
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y, test_size=0.15, random_state=33)

# RandomForestClassifier:
from sklearn.ensemble import GradientBoostingClassifier
GradientBoosting = GradientBoostingClassifier(n_estimators=1000)
GradientBoosting = GradientBoosting.fit(X_train,y_train)

# Creating a pickle file for the classifier
filename = 'maquina_preditiva.pkl'
pickle.dump(GradientBoosting, open(filename, 'wb'))