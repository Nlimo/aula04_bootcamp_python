#12. Dados dois dicionários, fundi-los em um único dicionário.

diconario_01 = {'a_nome' : 'lucas', 'a_idade' : 25}
diconario_02 = {'b_nome' : 'carol', 'b_idade' : 22}

diconario_03 = {**diconario_01, **diconario_02}

print(diconario_03)