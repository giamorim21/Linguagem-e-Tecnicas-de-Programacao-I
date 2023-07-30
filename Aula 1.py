"""Exercicio"""
""" a) ACHAR O VALOR MAXIMO E O MINIMO EM UMA UNICA LISTA """
lista = [5, 6, 8, 2, 10, 15, 0, 7]

"""Inicializando as variaveis de controle para o valor maximo e minimo"""

valor_maximo = lista[0]
valor_minimo = lista[0]

"""Percorrer a lista"""

for valor in lista:
    if valor > valor_maximo:
        valor_maximo = valor
    if valor < valor_minimo:
        valor_minimo = valor
print("Resultado da letra A:\n")
print(f"\tValor maximo: {valor_maximo}")
print(f"\tValor minimo: {valor_minimo}\n")

""" b) INVERTER A LISTA"""

lista_invertida = []

for i in range (len(lista) - 1, -1, -1):
    lista_invertida.append(lista[i])
print("Resultado da letra B:\n")
print(f"\tA lista invertida é: {lista_invertida}")

""" c) SOMA DOS VALORES NA LISTA """

soma = 0

for i in lista:
    soma += i

print("Resultado da letra C:\n")
print(f"O valor da soma é: {soma}")