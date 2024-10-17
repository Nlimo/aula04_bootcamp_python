#5. Dada a lista `["maçã", "banana", "cereja"]` e o dicionário `{"maçã": 0.45, "banana": 0.30, "cereja": 0.65}`, calcule o preço total da lista de compras.

lista: list = ["maçã", "banana", "cereja"]

dicionario: dict = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}

valor_total: float = 0.0

for chave, valor in dicionario.items():
    valor_total = valor_total + valor

print(valor_total)