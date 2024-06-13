from etl import *

pasta_argumento: str = 'data'
formato_saida: list = ['csv','parquet']

pipeline_geracao_kpi(pasta_argumento, formato_saida)