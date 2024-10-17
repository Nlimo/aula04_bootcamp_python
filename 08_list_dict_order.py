#8. Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.
from operator import itemgetter, attrgetter

pessoas = [
    {'nome': 'lucas', 'idade': 25},
    {'nome': 'carol', 'idade': 21},
    {'nome': 'lais', 'idade': 22}
]


print(sorted(pessoas, key= lambda pessoa: pessoa['nome']))

