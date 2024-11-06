#20. Escreva uma função que receba um dicionário e retorne uma lista de chaves ordenadas

dicionario: dict = {'chave1': 'valor1', 'chave2': 'valor2'}

def transforme_dict_key_in_list(dicionario:dict) -> list:
    lista: list = []
    keys = dicionario.keys()
    lista = list(keys)
    lista.sort() 
    return lista

print(transforme_dict_key_in_list(dicionario))
