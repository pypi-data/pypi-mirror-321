import psycopg2
from typing import Optional

def conectar_db(host: str, usuario: str, senha: str, banco: str) -> Optional[psycopg2.extensions.connection]:
    """
    Função para conectar a um banco de dados PostgreSQL.

    Args:
        host (str): Endereço do servidor do banco de dados.
        usuario (str): Nome de usuário do banco de dados.
        senha (str): Senha do banco de dados.
        banco (str): Nome do banco de dados.

    Returns:
        Optional[psycopg2.extensions.connection]: Conexão com o banco de dados ou None em caso de erro.
    """    
    try:
        conexao = psycopg2.connect(host=host, user=usuario, password=senha, database=banco)
        return conexao
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None
