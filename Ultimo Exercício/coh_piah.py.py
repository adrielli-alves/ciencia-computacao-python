import re

def le_assinatura():
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")
    print()

    wal = float(input("Entre o tamanho médio de palavra: "))
    ttr = float(input("Entre a relação Type-Token: "))
    hlr = float(input("Entre a Razão Hapax Legomana: "))
    sal = float(input("Entre o tamanho médio de sentença: "))
    sac = float(input("Entre a complexidade média da sentença: "))
    pal = float(input("Entre o tamanho medio de frase: "))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    print()
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair): ")
    while texto:
        textos.append(texto)
        i += 1
        print()
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair): ")

    return textos

def separa_sentencas(texto):
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    return frase.split()

def n_palavras_unicas(lista_palavras):
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    base = 0
    comparacao = []
    while base < len(as_a):
        comparacao.append(abs(as_a[base] - as_b[base]))
        base += 1
    similaridade = sum(comparacao) / 6
    return similaridade

def calcula_assinatura(texto):
    lista_palavras = []
    total_letras = 0
    total_frases = 0
    total_letras_sentenca = 0
    total_letras_frase = 0
    as_a = []
    
    sentencas_texto = separa_sentencas(texto)
    total_sentencas = len(sentencas_texto)
    for ordem_sentenca in range(len(sentencas_texto)):
        sentenca = sentencas_texto[ordem_sentenca]
        total_letras_sentenca += len(sentenca)
        frase_sentenca = separa_frases(sentenca)
        total_frases += len(frase_sentenca)
        for ordem_frase in range(len(frase_sentenca)):
            frase = frase_sentenca[ordem_frase]
            total_letras_frase += len(frase)
            palavras = separa_palavras(frase)
            for palavra in palavras:
                lista_palavras.append(palavra)
                
    total_unicas = n_palavras_unicas(lista_palavras)
    total_diferentes = n_palavras_diferentes(lista_palavras)
    total_palavras = len(lista_palavras)
    for palavra in lista_palavras:
        total_letras += len(palavra)

    tamanho_medio_palavra = total_letras / total_palavras
    type_token = total_diferentes / total_palavras
    hapax_legomana = total_unicas / total_palavras
    tamanho_medio_sentencas = total_letras_sentenca / total_sentencas
    complexidade_sentencas = total_frases / total_sentencas
    tamanho_medio_frases = total_letras_frase / total_frases

    as_a.append(tamanho_medio_palavra)
    as_a.append(type_token)
    as_a.append(hapax_legomana)
    as_a.append(tamanho_medio_sentencas)
    as_a.append(complexidade_sentencas)
    as_a.append(tamanho_medio_frases)
    
    return as_a

def avalia_textos(textos, ass_cp):

    as_correta = ass_cp[0]
    for assinatura in range(len(ass_cp)):
        if ass_cp[assinatura] < as_correta:
            as_correta = ass_cp[assinatura]

    for posicao in range(len(ass_cp)):
        if as_correta == ass_cp[posicao]:
            texto = posicao
    
    return texto

as_b = le_assinatura()
textos = le_textos()

ass_cp = []

for ordem_texto in range(len(textos)):
    texto = textos[ordem_texto]

    as_a = calcula_assinatura(texto)

    similaridade = compara_assinatura(as_a, as_b)
    
    ass_cp.append(similaridade)

autor = avalia_textos(textos, ass_cp)
print()
print('O autor do texto', autor, 'está infectado com COH-PIAH')
