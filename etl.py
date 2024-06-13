import pandas as pd
import os
import glob

### Função para leitura e concatenação de arquivos Json

def ler_arquivos_json(pasta:str) -> pd.DataFrame:
    """
    Função para leitura e concatenação de arquivos json
    """
    arquivos_json = glob.glob(os.path.join(pasta, '*.json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_vendas_concatenado = pd.concat(df_list, ignore_index=True)
    return df_vendas_concatenado

### Função para criar KPI

def criar_kpi(df:pd.DataFrame) -> pd.DataFrame:
    """
    Função para crair o KPI de total de vendas
    """
    df['Total'] = df['Quantidade'] * df['Venda']
    return df

### Procedure para exportar arquivos em Parquet ou csv

def exportar_arquivos_parquet_csv(df:pd.DataFrame, lista:list):
    """
    Procedure para carregar dados
    """
    for formato in lista:
        if formato == 'csv':
            df.to_csv('dados.csv',index=False) 
        if formato == 'parquet':
            df.to_parquet('dados.parquet',index=False)

### Procedure para consolidar o processo

def pipeline_geracao_kpi():
    """
    Procedure para pipeline de dados de vendas
    """
    pasta_argumento: str = 'data'
    df = ler_arquivos_json(pasta_argumento)
    df_kpi = criar_kpi(df)
    lista_formato_saida = ['parquet']
    exportar_arquivos_parquet_csv(df_kpi,lista_formato_saida)