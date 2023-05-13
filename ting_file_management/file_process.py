from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    file = txt_importer(path_file)
    instance.enqueue(path_file)
    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file
    }
    return sys.stdout.write(str(data))


def remove(instance):
    if not len(instance):
        return sys.stdout.write('Não há elementos\n')
    path_file = instance.dequeue()
    print(f'Arquivo {path_file} removido com sucesso')


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
