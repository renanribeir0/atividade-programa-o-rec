#  Se achar necessario, faça import de outras bibliotecas




# Enunciado
Escreva uma função chamada  **tem_duplicados**  que tome uma lista e retorne True 
se houver algum elemento que apareça mais de uma vez. Ela não deve modificar a lista original.

# Crie a função que será avaliada no exercício aqui
def tem_duplicados(lista):
    return len(set(lista)) != len(lista)


# Teste a sua função aqui (caso ache necessário)
lista1 = [1, 2, 3, 4, 5]
lista2 = [1, 2, 3, 4, 5, 5]
lista3 = [1, 1, 2, 3, 4, 4, 5]
tem_dup1 = tem_duplicados(lista1)
tem_dup2 = tem_duplicados(lista2)
tem_dup3 = tem_duplicados(lista3)
print(tem_dup1)
print(tem_dup2)
print(tem_dup3)











