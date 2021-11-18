def maior_elemento(lista):
    lista = sorted(set(lista))
    return lista[-1]