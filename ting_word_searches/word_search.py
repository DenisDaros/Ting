def exists_word(word, instance):
    lista = []
    for i in range(len(instance)):
        file = instance.search(i)

        linha = [
            {"linha": index + 1}
            for index, value in enumerate(file["linhas_do_arquivo"])
            if word.lower() in value.lower()
        ]
        if len(linha) >= 1:
            data = {
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": linha,
            }
            lista.append(data)
    return lista


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
