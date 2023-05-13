#  Se achar necessario, faça import de outras bibliotecas


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
