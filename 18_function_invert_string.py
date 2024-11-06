#18. Desenvolva uma função que receba uma string como argumento e retorne essa string revertida.

def string_revertida(palavra: str) -> str:
    palavra = palavra[::-1]
    return palavra


print(string_revertida('lucas'))