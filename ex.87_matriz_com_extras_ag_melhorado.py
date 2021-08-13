matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = 0

for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f"Digite um valor para a posição: [{l}, {c}]: "))

        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]

print()
print('-=-' * 30)
print()

for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]', end="")

    print()


print()
print(30 * "-=-")

print(f"\nA soma de todos os números pares é: {somapar}\n")

print(30 * "-=-")

print(f"\nA soma de todos os valores da terceira coluna é: {matriz[0][2] + matriz[1][2] + matriz[2][2]}\n")

print(30 * "-=-")

print(f'\nO maior valor da segunda linha é: {max(matriz[1])}\n')

print(30 * "-=-")
