import csv
import os

def ler_csv(arquivo: str) -> list:
    """
    Função para ler um arquivo CSV e retornar o conteúdo como uma lista de dicionários.
         
    Args:
        arquivo (str): Caminho do arquivo CSV.

    Returns:
        list: Lista de dicionários com o conteúdo do CSV.
    """
    dados = []

    if not os.path.exists(arquivo):
        raise FileNotFoundError(f"O arquivo {arquivo} não foi encontrado.")
    with open(arquivo, mode='r', newline='', encoding='utf-8') as file:
        leitor = csv.DictReader(file)
        for linha in leitor:
            dados.append(linha)
    
    return dados
