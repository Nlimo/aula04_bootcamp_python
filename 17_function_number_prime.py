#17. Crie uma função que receba um número como argumento e retorne `True` se o número for primo e `False` caso contrário.

num = int(9)
# Negative numbers, 0 and 1 are not primes
if num > 1:
    num_for = num
    for n in range(2, num_for-1):
        if num_for % n == 0:
            result = f'{num} não é primo'
            break
        else:
            result = f'{num} é primo'

print(result)

