print("Vamos descobrir o maior número da sequência a baixo:\n")
print("[1, 10, 50, 67, 100, 3, -5, 8, 11, 55, 0]\n")
print("--------------------------------------------")

numeros = [1, 10, 50, 67, 100, 3, -5, 8, 11, 55, 0]

def seleciona_maior(lista):

    maior = lista[0]

    for n in lista:
        if n > maior:
            maior = n

    return maior

res = seleciona_maior(numeros)
print(f"maior número encontrado: {res}")
