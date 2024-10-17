#7. Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.

lista: list = [18, 17, 14, 21, 25, 30]

lista_maior = []
lista_menor = []

for idade in lista:
    if idade >= 18:
        lista_maior.append(idade)
    else:
        lista_menor.append(idade)

print(lista_maior)