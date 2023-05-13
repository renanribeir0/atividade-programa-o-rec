from exercicio1 import multiplas_operacoes
from exercicio2 import cumulativo
from exercicio3 import soma_dos_aninhados
from exercicio4 import tem_duplicados




def test_multiplas_operacoes():

    # soma, subtração, multiplicação e divisão
    assert multiplas_operacoes(6, 2) == (8, 4, 12, 3)
    assert multiplas_operacoes(2, 4) == (6, -2, 8, 0.5)
    assert multiplas_operacoes(9, 0) == (9, 9, 0, 0)


def test_cumulativo():

    # soma cumulativa
    assert cumulativo([1, 2, 3]) == [1, 3, 6]
    assert cumulativo([1, -2, 3]) == [1, -1, 2]
    assert cumulativo([3, 3, -2, 408, 3, 0]) == [3, 6, 4, 412, 415, 415]


def test_soma_dos_aninhados():

    # soma dos aninhados
    lista = [[11, 22], [33], [44, 55, 66]]
    outra_lista = [[1, 2, 3, 4], [3, 3], [4, 6]]
    assert soma_dos_aninhados(lista) == 231
    assert soma_dos_aninhados(outra_lista) == 27


def test_tem_duplicados():

    # tem duplicados
    assert tem_duplicados([1, 2, 3, 2]) == True
    assert tem_duplicados([1, 2, 3, 4]) == False
    assert tem_duplicados([]) == False
    assert tem_duplicados([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True
    assert tem_duplicados([0, 0, 0, 0, 0]) == True
