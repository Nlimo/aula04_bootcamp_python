#14. Dado um dicionário, criar listas separadas para suas chaves e valores.

dicionario:dict = {'cahve1' : 'valor1', 'chave2' : 'valor2', 'chave3' : 'valor3' }

listas:list = []

for chave, valor in dicionario.items():
   listas.append([chave, valor])

n = 1

for lista in listas:
    exec(f'lista{n} = lista')
    n += 1

print(lista1)
print(lista2)
print(lista3)