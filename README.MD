
# Projeto Cotação do Dólar - ETL

Este projeto é uma aplicação simples em Python para realizar operações de ETL (Extração, Transformação e Carregamento) de dados sobre a cotação do dólar. O objetivo é extrair dados da API do Banco Central, realizar uma transformação nos dados e, em seguida, armazená-los em um banco de dados PostgreSQL.

## Funcionalidades

**Extract:**
   - O projeto faz uma requisição para a API do Banco Central para obter as cotações do dólar em um determinado intervalo de datas.

**Transformation:** 
   - Após a extração dos dados, eles são processados e transformados. A transformação inclui a formatação da data e a arredondagem das cotações.

**Load:**
   - Os dados transformados são inseridos em um banco de dados PostgreSQL para armazenamento persistente.

## Tecnologias Utilizadas

- **Python:** Linguagem principal do projeto.
- **Requests:** Biblioteca para fazer a requisição HTTP a API do Banco Central.
- **DuckDB:** Usado para processar e transformar os dados localmente em memória.
- **SQLAlchemy:** Usado para conectar e interagir com o banco de dados PostgreSQL.
- **PostgreSQL:** Banco de dados para armazenar as cotações do dólar.
- **Pandas:** Usado para manipular e formatar os dados em DataFrame.

## Como Rodar o Projeto

### Pré-requisitos

- Python 3.8 ou superior
- Banco de dados PostgreSQL rodando localmente

### Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/ribeirothales/cotacao-dolar.git
   cd cotacao-dolar
   ```

2. **Crie um ambiente virtual:**

   Se você ainda não tiver um ambiente virtual, crie um:

   ```bash
   python -m venv venv
   ```

3. **Ative o ambiente virtual:**

   - No Windows:

     ```bash
     venv\Scripts\activate
     ```

   - No Linux/macOS:

     ```bash
     source venv/bin/activate
     ```

4. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Configuração do Banco de Dados:**

   - Crie um banco de dados PostgreSQL chamado `cotacaoDolar`:

     ```bash
     psql -U postgres
     CREATE DATABASE cotacaoDolar;
     ```

   - Configure a string de conexão do banco de dados no código (se necessário), especificamente no arquivo `transformData.py`, onde está configurada a conexão com o PostgreSQL.

### Executando o Projeto

1. Para rodar o projeto, basta executar o arquivo `main.py`:

   ```bash
   python main.py
   ```

   Isso vai fazer a extração dos dados da API, a transformação dos dados e o carregamento no banco de dados PostgreSQL.

## Estrutura de Diretórios

```plaintext
cotacao-dolar/
├── venv/                  # Ambiente virtual
├── main.py                # Arquivo principal que executa o fluxo ETL
├── transformData.py       # Arquivo de transformação e carregamento dos dados
├── requirements.txt       # Dependências do projeto
└── README.md              # Documentação do projeto
```

## Como Funciona

### 1. Extração

O primeiro passo do processo é a extração dos dados da API do Banco Central. A função `extract()` realiza uma requisição HTTP para a URL da API, passando os parâmetros de data para obter as cotações do dólar em um intervalo específico. A resposta é um JSON que contém as cotações.

### 2. Transformação

Após a extração, os dados são passados para a função `transform_and_load()`, que os armazena temporariamente em uma tabela no DuckDB. A transformação realizada inclui:

- Arredondamento dos valores de `cotacaoCompra` e `cotacaoVenda` para duas casas decimais.
- Formatação da coluna `dataHoraCotacao` para o formato `YYYY-MM-DD HH:MM:SS`.

### 3. Carregamento

Finalmente, os dados transformados são carregados no banco de dados PostgreSQL usando SQLAlchemy. O código cria uma conexão com o banco de dados e usa o método `to_sql()` para armazenar os dados na tabela `cotacoes`.

## Possíveis Melhorias

- **Automatização do Processo:** A automação do processo de ETL pode ser realizada com ferramentas como Airflow ou cron jobs.
- **Validação de Dados:** Melhorias na validação dos dados extraídos da API antes de carregá-los no banco de dados.
- **Aprimoramento da Transformação:** Outras transformações podem ser aplicadas aos dados, como a agregação de informações ou a criação de relatórios.

## Contato  

<div>
    <a href="https://www.linkedin.com/in/ribeirothales/" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a>
    <a href="mailto:thales.o.ribeiro@gmail.com" target="_blank"><img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" target="_blank"></a>
</div>

