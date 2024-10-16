# 1) Solicita ao usuário que digite seu nome

cotniuar_nome: str = False

while not cotniuar_nome:

    nome: str = input("Digite seu nome: ")

    if nome.isdigit():
        print("Valor invalido para um nome, digite outro")
    elif len(nome) == 0:
        print("É necessário escrever um nome")
    elif nome.isspace():
        print("Não é permitido digitar somente espaço em branco")
    else:
        cotniuar_nome = True

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante

cotniuar_salario: bool = False

while not cotniuar_salario:
    try:
        salario: float = float(input("Digite seu salário: "))
        cotniuar_salario = "true"
    except ValueError:
        print("Digite um valor válido, um número")
    
        

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante

cotniuar_bonus: bool = False

while not cotniuar_bonus:
    try:
        bonus: float = float(input("Digite o bônus recebido: "))
        cotniuar_bonus = True
    except ValueError:
        print("Digite um valor válido, um número")
        exit()

# 4) Calcule o valor do bônus final
result = 1000 + salario * bonus

# 5) Imprima cálculo do KPI para o usuário
print(result)

# 6) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
print(f" {nome} seu salário com o bônus fica: {result}")

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?