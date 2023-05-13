#  Se achar necessario, faça import de outras bibliotecas





# Enunciado
Escreva uma função chamada **multiplas_operacoes**, esta função deverá receber duas variáveis 
por parâmetro e retornar as quatro operações básicas, soma, subtração, multiplicação e divisão, nesta ordem. 
Adicione uma estrutura de decisão evitar divisão por zero, caso exista divisão por zero, retorne zero.

# Crie a função que será avaliada no exercício aqui
def multiplas_operacoes(a, b):
    soma = a + b
    subtracao = a - b
    multiplicacao = a * b
    if b != 0:
        divisao = a / b
    else:
        divisao = 0
    return soma, subtracao, multiplicacao, divisao


# Teste a sua função aqui (caso ache necessário)

