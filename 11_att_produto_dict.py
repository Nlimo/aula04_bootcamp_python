#11. Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.

lista: list = [
    {'name': 'chapeu', 'preco': 24.43},
    {'name': 'bolsa', 'preco': 40.23}
]

lista[1]['preco'] = 30.23

print(lista)