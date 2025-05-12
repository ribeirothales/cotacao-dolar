import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
import duckdb

# Carrega variáveis do .env
load_dotenv()

def transform_and_load(dados):
    
    conn = duckdb.connect(database=':memory:')

    conn.execute("""
    CREATE TABLE cotacoes (
        cotacaoCompra DOUBLE, 
        cotacaoVenda DOUBLE, 
        dataHoraCotacao VARCHAR
    )
    """)

    for dado in dados:
        conn.execute("""
            INSERT INTO cotacoes VALUES (?, ?, ?)
        """, (dado['cotacaoCompra'], dado['cotacaoVenda'], dado['dataHoraCotacao']))

    query = """
    SELECT 
        ROUND(cotacaoCompra, 2) AS cotacaoCompra,
        ROUND(cotacaoVenda, 2) AS cotacaoVenda,
        strftime(CAST(dataHoraCotacao AS TIMESTAMP), '%Y-%m-%d %H:%M:%S') AS dataHoraCotacao
    FROM cotacoes
    """
    resultados = conn.execute(query).fetchdf()

    # Monta a conexão usando variáveis do ambiente
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_host = os.getenv('DB_HOST')
    db_port = os.getenv('DB_PORT')
    db_name = os.getenv('DB_NAME')

    engine = create_engine(
        f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}?client_encoding=utf8"
    )

    with engine.connect() as connection:
        resultados.to_sql('cotacoes', connection, if_exists='replace', index=False)
        
    return resultados
