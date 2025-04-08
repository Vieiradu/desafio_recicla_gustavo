# Desafio - Encontrar o Maior Número em uma Lista

Este projeto foi feito para resolver um desafio simples: encontrar o maior número dentro de uma lista.


# O que o código faz

- Recebe uma lista de números.
- Compara os números e guarda o maior encontrado.
- Mostra o resultado na tela com uma mensagem amigável.

---

## Explicando o código de forma simples
 -Criei dois prints iniciais para informar o que o programa faz utilizando \n para quebrar a linha pra deixar bonitinho! =) 
numeros = [1, 10, 50, 67, 100, 3, -5, 8, 11, 55, 0]
#Criei uma lista com os números informados.


def seleciona_maior(lista):
#Aqui criei uma função chamada “seleciona_maior”.


    maior = lista[0]
#Começo assumindo que o primeiro número é o maior, pensei como eu faria, olharia numero por numero a partir do primeiro.


    for n in lista:
        if n > maior:
            maior = n
#Passo por cada número da lista e comparo com o "maior atual". Se achar um maior, atualizo.


    return maior
#Depois de verificar tudo, devolvo o maior número que encontrei.


res = seleciona_maior(numeros)
print(f"maior número encontrado: {res}") 

#Aqui eu chamo a função com minha lista e mostro o resultado usando f-string, que é uma forma que ensinam muito na FIAP (rsrs) e limpa de mostrar mensagens com variáveis, confesso que fervi um pouco aqui nesse final mas a cabeça e os pdfs das aulas ajudaram kkk.
