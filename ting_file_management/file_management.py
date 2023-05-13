import sys


def txt_importer(path_file):
    try:
        if not path_file.endswith(".txt"):
            raise ValueError("Formato inválido")

        with open(path_file) as file:
            return file.read().split("\n")
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
    except ValueError as e:
        print(str(e), file=sys.stderr)
