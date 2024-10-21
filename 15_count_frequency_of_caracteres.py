#15. Dada uma string, contar a frequência de cada caractere usando um dicionário.

string = 'bala'

dicionario: dict = {} 

for letra in list(string):
    if letra in dicionario:
        dicionario[letra] = dicionario[letra] + 1
    else:
        dicionario[letra] = 1

#dicionario = list(string)[0], 1

print(dicionario)