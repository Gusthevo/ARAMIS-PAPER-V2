import tiktoken

def contar_tokens_arquivo(caminho_arquivo, modelo="gpt-4o"):
    # Lê o arquivo inteiro
    with open(caminho_arquivo, "r", encoding="utf-8") as f:
        texto = f.read()

    # Carrega o tokenizador do modelo
    enc = tiktoken.encoding_for_model(modelo)

    # Tokeniza o texto
    tokens = enc.encode(texto)

    # Retorna quantidade e a lista de tokens se precisar
    return len(tokens), tokens


# Exemplo de uso:
arquivo = "../data/processed_tccs/2025_tcc_lzbviana.md"
quantidade, tokens = contar_tokens_arquivo(arquivo)

print(f"Total de tokens: {quantidade}")
