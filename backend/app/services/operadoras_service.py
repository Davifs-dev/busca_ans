import pandas as pd
from settings import settings
import numpy as np


def buscar_operadoras_por_texto(query: str):
    # Carrega o CSV das operadoras
    df_operadoras = pd.read_csv(settings.CSV_PATH_OPERADORAS, delimiter=";")

    df_operadoras = df_operadoras.fillna("")

    # Substituir Nome Fantasia vazio por "Não informado"
    df_operadoras["Nome_Fantasia"] = df_operadoras["Nome_Fantasia"].replace(
        "", "Não informado"
    )

    # Realiza a busca nas colunas de interesse (ajuste conforme necessário)
    cols_para_busca = [
        "Razao_Social",
        "Nome_Fantasia",
        "CNPJ",
        "Modalidade",
        "Bairro",
        "Cidade",
    ]
    for col in cols_para_busca:
        df_operadoras[col] = df_operadoras[col].astype(str)

    # Realiza a busca nas colunas de interesse
    filtered = df_operadoras[
        df_operadoras["Razao_Social"].str.contains(
            query, case=False, na=False
        )  # Busca em Razao_Social
        | df_operadoras["Nome_Fantasia"].str.contains(
            query, case=False, na=False
        )  # Busca em Nome_Fantasia
        | df_operadoras["CNPJ"].str.contains(
            query, case=False, na=False
        )  # Busca em CNPJ
        | df_operadoras["Modalidade"].str.contains(
            query, case=False, na=False
        )  # Busca em Modalidade
        | df_operadoras["Bairro"].str.contains(
            query, case=False, na=False
        )  # Busca em Bairro
        | df_operadoras["Cidade"].str.contains(
            query, case=False, na=False
        )  # Busca em Cidade
        | df_operadoras["Registro_ANS"]
        .astype(str)
        .str.contains(query, case=False, na=False)
    ]
    filtered = filtered.replace([np.nan, np.inf, -np.inf], "")
    # Retorna os resultados em formato de lista de dicionários
    return filtered.to_dict(orient="records")
