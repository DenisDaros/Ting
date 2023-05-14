from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    dict1 = {
        "nome_do_arquivo": "arquivo_teste.txt",
        "qtd_linhas": 1,
        "linhas_do_arquivo": ['1']
    }

    dict2 = {
        "nome_do_arquivo": "arquivo_teste.txt3",
        "qtd_linhas": 2,
        "linhas_do_arquivo": ['1', '2']
    }

    dict3 = {
        "nome_do_arquivo": "arquivo_teste.txt2",
        "qtd_linhas": 6,
        "linhas_do_arquivo": ['1', '2', '3', '4', '5', '6']
    }

    teste = PriorityQueue()

    assert teste.is_priority(dict1) is True
    assert teste.is_priority(dict2) is True
    assert teste.is_priority(dict3) is False

    teste.enqueue(dict1)
    teste.enqueue(dict2)
    teste.enqueue(dict3)
    assert len(teste) == 3
    assert teste.search(0) is dict1

    value_removed = teste.dequeue()
    assert len(teste) == 2
    assert value_removed == dict1
    assert teste.search(0) is dict2

    value_removed = teste.dequeue()
    assert len(teste) == 1
    assert value_removed == dict2
    assert teste.search(0) is dict3

    value_removed = teste.dequeue()
    assert len(teste) == 0
    assert value_removed == dict3

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        teste.search(0)
