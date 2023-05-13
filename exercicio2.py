#  Se achar necessario, faça import de outras bibliotecas




# Enunciado
Escreva uma função chamada **cumulativo** que receba uma lista de números e retorne a soma 
cumulativa; isto é, uma nova lista onde o i-ésimo elemento é a soma dos primeiros i+1 elementos 
da lista original. 
Por exemplo:
```python
lista = [2, 3, 4, 5]
```
Deverá fornecer como retorno uma lista:
```python
[2, 5, 9, 14]


# Crie a função que será avaliada no exercício aqui
def cumulativo(lista):
    soma = 0
    nova_lista = []
    for num in lista:
        soma += num
        nova_lista.append(soma)
    return nova_lista


# Teste a sua função aqui (caso ache necessário)
lista = [2, 3, 4, 5]
nova_lista = cumulativo(lista)
print(nova_lista)












