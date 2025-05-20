# Solicita ao usuário um número inteiro positivo n
n = int(input("Digite a quantidade de números inteiros que deseja adicionar à lista: "))

# Inicializa uma lista vazia
lista = []

# Lê n números inteiros e os adiciona à lista
for _ in range(n):
    numero = int(input("Digite um número inteiro: "))
    lista.append(numero)

# Solicita um número inteiro x para verificar se está na lista
x = int(input("Digite um número inteiro para verificar se está na lista: "))

# Verifica se x pertence à lista
if x in lista:
    print(f"O número {x} está na lista.")
else:
    print(f"O número {x} não está na lista.")
