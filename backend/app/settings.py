import os
from typing import List
from pydantic_settings import BaseSettings
from pydantic import AnyHttpUrl


class Settings(BaseSettings):
    PROJECT_NAME: str = "buscaANS"
    DESCRIPTION: str = " API para buscar operadoras de saúde."
    VERSION: str = "1.0.0"

    CSV_PATH_OPERADORAS: str = os.path.join(
        os.getcwd(), "..", "sql_db", "files", "Relatorio_cadop.csv"
    )


settings = Settings()
