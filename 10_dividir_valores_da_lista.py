#10. Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.

lista: list = list(range(1, 11))

lista_par:list = []

lista_impar:list = []

for numero in lista:
    if numero % 2 == 0:
        lista_par.append(numero)
    else:
        lista_impar.append(numero)

print(lista_par)
print(lista_impar) 