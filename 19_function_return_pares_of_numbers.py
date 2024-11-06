#19. Implemente uma função que receba dois argumentos: uma lista de números e um número. A função deve retornar todas as combinações de pares na lista que somem ao número dado.

lista_numeros: list = [1, 2, 3, 4, 5]

variavel = 5

lista_result: list = []


def pares_que_geram_variavel(lista: list, numero: int) -> list:
    for n in lista:
        for z in lista[1:]:
            if n + z == numero:
                lista_result.append([n , z])
    return lista_result
                


resultado = pares_que_geram_variavel(lista_numeros, 5)

print(resultado)