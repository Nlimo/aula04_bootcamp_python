#16. Escreva uma função que receba uma lista de números e retorne a soma de todos os números.

lista: list = [4, 5, 6]

def somar_lista_de_numeros(numeros: list) -> list:
    result = 0
    for n in numeros:
        result = result + n
    
    return result


resultado = somar_lista_de_numeros(lista)

print(resultado)

