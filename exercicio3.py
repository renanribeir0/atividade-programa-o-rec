#  Se achar necessario, faça import de outras bibliotecas




#Enunciado
Escreva uma função chamada **soma_dos_aninhados** que receba uma lista de listas de números 
inteiros e adicione os elementos de todas as listas aninhadas. 
Exemplo de listas aninhadas:
```python
lista = [[11, 22], [33], [44, 55, 66]]
outra_lista = [[1, 2, 3, 4], [3, 3], [4, 6]]

# Crie a função que será avaliada no exercício aqui
def soma_dos_aninhados(lista):
    soma = 0
    for sublist in lista:
        for num in sublist:
            soma += num
    return soma

# Teste a sua função aqui (caso ache necessário)
lista = [[11, 22], [33], [44, 55, 66]]
outra_lista = [[1, 2, 3, 4], [3, 3], [4, 6]]
soma1 = soma_dos_aninhados(lista)
soma2 = soma_dos_aninhados(outra_lista)
print(soma1)
print(soma2)











