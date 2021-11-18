def remove_repetidos(lista):
    lista.sort()
    copia = lista
    final = []
    for i in lista:
        for j in copia:
            if i == j:
                if i not in final:
                    final.append(i)
    lista = final
    return lista
