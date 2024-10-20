#13. Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.

dicionario: dict = {'Chapeu' : 0, 'Sandalha' : 2, 'Bolsa' : 5}

lista_possui_estoque: list = []
lista_nao_possui_estoque: list = []

for chave, quantidade in dicionario.items():
    if quantidade > 0:
        lista_possui_estoque.append([chave, quantidade])
    else:
        lista_nao_possui_estoque.append([chave, quantidade])

print(lista_possui_estoque)

