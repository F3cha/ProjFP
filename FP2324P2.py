def verifica_letras(arg):
    """
    Função auxiliar criada para poder verificar se a str da interseção era verdadeira
    :param arg : coluna da intersecao
    :return :verdadeiro ou falso
    """
    if ord("A") <= ord(arg) <= ord("S"):
        return True
    else:
        return False


def verifica_numero(arg):
    """
       Função auxiliar criada para poder verificar se o inteiro da interseção era verdadeiro

       :param arg:linha da intersecao
       :return bool:verdadeiro ou falso
       """
    if 1 <= arg <= 19:
        return True
    else:
        return False


def cria_intersecao(col, lin):
    """
        Recebe a coluna e linha e devolve a intersecao correspondente a essa col e linha
        :param col:coluna da intersecao
        :param lin:linha da intersecao
        :return : (coluna,linha)
        """
    i = (col, lin)
    if eh_intersecao(i):
        return i
    else:
        raise ValueError("cria_intersecao: argumentos invalidos")


def obtem_col(intersecao):
    """
        obtem col(i) devolve a coluna col da interseção i.
        :param intersecao:
        :return :coluna da intersecao
        """
    return intersecao[0]


def obtem_lin(intersecao):
    """
        obtem lin(i) devolve a linha lin da interseção i.
        :param intersecao:
        :return :linha da intersecao
        """
    return intersecao[1]


def eh_intersecao(intersecao):
    """
        eh intersecao(arg) devolve True caso o seu argumento seja um TAD intersecao
    e False caso contrário.
        :param :intersecao
        :return :bool
        """
    if isinstance(intersecao, tuple) and len(intersecao) == 2:
        if isinstance(obtem_col(intersecao), str) and len(obtem_col(intersecao)) == 1 and isinstance(
                obtem_lin(intersecao), int) and not isinstance(obtem_lin(intersecao), bool):
            if verifica_letras(obtem_col(intersecao)) and verifica_numero(obtem_lin(intersecao)):
                return True
    else:
        return False


def intersecoes_iguais(intersecao1, intersecao2):
    """
        intersecoes iguais(i1, i2) devolve True apenas se i1 e i2 são interseções e são
    iguais, e False caso contrário.
        :param intersecao1:
        :param intersecao2:
        :return bool: verdadeiro ou falso
        """
    if eh_intersecao(intersecao1) and eh_intersecao(intersecao2):
        if obtem_col(intersecao1) == obtem_col(intersecao2) and obtem_lin(intersecao1) == obtem_lin(intersecao2):
            return True
    else:
        return False


def str_para_intersecao(string):
    """
        str para intersecao(s) devolve a interseção representada pelo seu argumento.
        :param string:
        :return (str,int):
        """
    return string[0], int(string[1:])


def intersecao_para_str(i):
    """
      intersecao para str(i) devolve a cadeia de caracteres que representa a intersecao
      :param i:intersecao
      :return :string da intersecao
      """
    intersecao = ""
    for num in range(len(i)):
        intersecao = intersecao + str(i[num])
    return intersecao


def obtem_intersecoes_adjacentes(i, ultima_intersecao):
    """
    Recebe uma intersecao, e a ultima_intersecao do goban, e devolve as intersecoes adjacentes á intersecao
        :param i:intersecao
        :param ultima_intersecao:intersecao do cnato superior direito do tabuleiro
        :return:tuplo de intersecoes adjacentes a i
        """
    letra = ord(obtem_col(i))
    numero = obtem_lin(i)
    adjacentes = ()
    if numero > 1:  # antes estava 0
        adjacentes += ((obtem_col(i), obtem_lin(i) - 1),)
    if letra > 65:
        adjacentes += ((chr(ord(obtem_col(i)) - 1), obtem_lin(i)),)
    if letra < ord(ultima_intersecao[0]):
        adjacentes += ((chr(ord(obtem_col(i)) + 1), obtem_lin(i)),)
    if numero < ultima_intersecao[1]:
        adjacentes += ((obtem_col(i), obtem_lin(i) + 1),)
    return adjacentes


def ordena_intersecoes(arg):
    """
    recebe um tuplo de intersecoes do tabuleiro goban, e devovle um tuplo com as intersecoes organizadas por ordem
    de leitura, ordenando primeiro pela linha(numero) e após isso ordena pela coluna(letra)
    :param arg: tuplo de intersecões
    :return: tuplo de intersecoes organizado por ordem de leitura
    """
    return tuple(sorted(arg, key=lambda x: (obtem_lin(x), obtem_col(x))))


def cria_pedra_branca():
    """
    cria pedra branca() devolve uma pedra pertencente ao jogador branco.
    :return:"B"
    """
    return "B"


def cria_pedra_preta():
    """
    cria pedra preta() devolve uma pedra pertencente ao jogador preto.
    :return:"P"
    """
    return "P"


def cria_pedra_neutra():
    """
    cria pedra neutra() devolve uma pedra neutra.
    :return:"N"
    """
    return "N"


def eh_pedra(pedra):
    """
    eh pedra(arg) devolve True caso o seu argumento seja uma pedra e False
caso contrário.
    :param pedra: pedra
    :return: Verdadeiro if Tad Pedra
    """
    if pedra in (cria_pedra_branca(), cria_pedra_preta(), cria_pedra_neutra()):
        return True
    else:
        return False


def eh_pedra_branca(pedra):
    """
    eh pedra branca(p) devolve True caso a pedra p seja do jogador branco e False
caso contrário.
    :param pedra: pedra
    :return: True caso seja uma Pedra branca
    """
    if pedra == cria_pedra_branca():
        return True
    return False


def eh_pedra_preta(pedra):
    """
    eh pedra preta(p) devolve True caso a pedra p seja do jogador preto e False
caso contrário.
    :param pedra:
    :return:
    """
    if pedra == cria_pedra_preta():
        return True
    return False


def pedras_iguais(p1, p2):
    """
    pedras iguais(p1, p2) devolve True apenas se p1 e p2 são pedras e são iguais.
    :param p1: pedra1
    :param p2: pedra2
    :return: Verdadeiro caso as pedras sejam iguais
    """
    if p1 == p2:
        return True
    else:
        return False


def pedra_para_str(pedra):
    """
    Recebe uma pedra, e devolve a str que representa essa pedra no tabuleiro
    :param pedra:
    :return:string da pedra
    """
    if eh_pedra_branca(pedra):
        return "O"
    if eh_pedra_preta(pedra):
        return "X"
    if not eh_pedra_jogador(pedra):
        return "."


def eh_pedra_jogador(pedra):
    """
    eh pedra jogador(p) devolve True caso a pedra p seja de um jogador e False caso
contrário.
    :param pedra:
    :return: bool
    """
    if eh_pedra_branca(pedra) or eh_pedra_preta(pedra):
        return True
    return False


def cria_goban_vazio(numerotabuleiro):
    """
    Recebe um numero, e irá gerar uma tabuleiro composto por pedras 'N' neutras, sendo a sua dimensão n*n.
    O numero deve ser 9x9, 13x13, 19x19 caso não seja irá gerar um erro

    :param numerotabuleiro: recebe um numero que representa as dimensões do tabuleiro
    :return: devolve tabuleiro vazio
    """
    if numerotabuleiro in (9, 13, 19) and isinstance(numerotabuleiro, int):
        tabuleiro = [["N"] * numerotabuleiro]
        for i in range(1, numerotabuleiro):
            tabuleiro.append(["N"] * numerotabuleiro)
        return tuple(tabuleiro)
    else:
        raise ValueError("cria_goban_vazio: argumento invalido")


def num_coluna(intersecao):
    """
    Função auxiliar criada para poder obter o representante da coluna mais rapidamente
    :param intersecao: uma intersecao
    :return: o representante da coluna como indice do tuplo 'A'->0
    """
    return ord(obtem_col(intersecao)) - 65


def num_linha(intersecao):
    """
    Função auxiliar criada para poder obter o representante da linha mais rapidamente
    :param intersecao: um intersecao
    :return: o representante da linha como indice de lista '1'->0
    """
    return obtem_lin(intersecao) - 1


def cria_goban(n, ib, ip):
    """
    Recebe um numero e ira criar um goban_vazio, E recebe dois tuplos, um com intersecoes representantes de pedras
    pretas e o outro de pedras brancas. Ira substituir no tabuleiro devolvendo assim um tabuleiro goban prenchido
    Caso o n não esteja entre 9,13,19 ira gerar um erro, assim como se as intersecoes não forem validas
    :param n: tabuleiro de goban
    :param ib: tuplo de intersecoes de pedras brancas
    :param ip: tuplo de intersecoes de pedras pretas
    :return: de um tabuleiro ocupado com as intersecoes pretas e brancas
    """
    try:
        goban = cria_goban_vazio(n)
        if not isinstance(ib, tuple) or not isinstance(ip, tuple):
            raise ValueError("cria_goban: argumentos invalidos")
        for intersecoes in ib:
            if not eh_intersecao(intersecoes) or intersecoes in ip:
                raise ValueError("cria_goban: argumentos invalidos")
            goban[num_coluna(intersecoes)][num_linha(intersecoes)] = "B"
        for intersecoes in ip:
            if not eh_intersecao(intersecoes):
                raise ValueError("cria_goban: argumentos invalidos")
            goban[num_coluna(intersecoes)][num_linha(intersecoes)] = "P"
        return goban
    except ValueError:
        raise ValueError("cria_goban: argumentos invalidos")


def cria_copia_goban(g):
    """
    Recebe um tabuleiro goban n*n e devolve um tabuleiro goban n*n mas com ids diferentes
    :param g: goban n*n
    :return: tabuleiro igual mas com id diferente
    """
    listarep = []
    for i in g:
        listarep.append(i)
    return tuple(listarep)


def obtem_ultima_intersecao(g):
    """
    Recebe um goban e devolve a intersecao representante do canto superior direito
    :param g: goban n*n
    :return: intersecao do conto superior direito do tabuleiro
    """
    return (chr(len(g) + 64), len(g[0]))


def obtem_pedra(g, i):
    """
    Função recebe um tabuleiro n*n e uma intersecao, e devolve qual a pedra nessa mesma intersecao
    :param g: goban n*n
    :param i: intersecao
    :return: pedra
    """
    return g[num_coluna(i)][num_linha(i)]


def obtem_cadeia(goban, intersecao):
    """
    Recebe um tabuleiro goban n*n, e uma intersecão. Caso a intersecao esteja ligada a mais intersecoes com o mesmo tipo
    de pedra, irá devolver um tuplo com todas as intersecoes que estejam conectadas entre si
    :param goban: tabuleiro n*n
    :param intersecao:
    :return: tuplo de intersecoes iguais adjacentes
    """
    indice = 0
    listav = [intersecao]
    candidatos = obtem_intersecoes_adjacentes(
        intersecao, obtem_ultima_intersecao(goban)
    )
    while candidatos:
        for um in candidatos:
            if um not in listav:
                if (
                        goban[ord(um[0]) - 65][um[1] - 1]
                        == goban[ord(intersecao[0]) - 65][intersecao[1] - 1]
                ):
                    listav += [um]
        indice += 1
        if indice == len(listav):
            return tuple(ordena_intersecoes(listav))
        candidatos = obtem_intersecoes_adjacentes(
            listav[indice], obtem_ultima_intersecao(goban)
        )


def coloca_pedra(goban, intersecao, pedra):
    """
    A função recebe um tabuleiro n*n, e um intersecao onde ira colocar a pedra fornecida
    :param goban: tabuleiro n*n
    :param intersecao:
    :param pedra:
    :return:
    """
    if eh_pedra_branca(pedra):
        goban[num_coluna(intersecao)][intersecao[1] - 1] = cria_pedra_branca()
    if eh_pedra_preta(pedra):
        goban[num_coluna(intersecao)][intersecao[1] - 1] = cria_pedra_preta()
    return goban


def remove_pedra(goban, intersecao):
    """
    recebe um tabuleiro goban n*n. E ira remover a pedra da intersecao ficando assim uma pedra neutra
    :param goban:
    :param intersecao:
    :return:
    """
    goban[num_coluna(intersecao)][num_linha(intersecao)] = cria_pedra_neutra()
    return goban


def remove_cadeia(goban, tuplointercoes):
    """
    Recebe um tabuleiro goban n*n, e ira remover todas as pedras que se encontrem nas intersecoes do tuplo fornecido
    :param goban: tabuleiro n*n
    :param tuplointercoes: tuplo de intersecoes
    :return: tabuleiro n*n modificado
    """
    for intersecao in tuplointercoes:
        remove_pedra(goban, intersecao)
    return goban


def eh_goban(arg):
    """
    Avalia se o tabuleiro fornecido é uma tabuleiro goban ou não
    :param arg: tabuleiro goban n*n
    :return: True or False
    """
    if isinstance(arg, tuple):
        comprimento = len(arg)
        if comprimento in (9, 13, 19):
            for lista in arg:
                if isinstance(lista, list) and len(lista) == comprimento:
                    for membros in lista:
                        if eh_pedra(membros):
                            return True
    else:
        return False


def eh_intersecao_valida(goban, intersecao):
    """
    Recebe um tabuleiro goban, e uma intersecao e verifica se a intersecao esta compreendida no tabuleiro
    :param goban: tabuleiro goban
    :param intersecao:
    :return: True se pertencer ao tabuleiro, false caso contrario
    """
    letras = ord(obtem_col(intersecao))
    linha = obtem_lin(intersecao)
    if 65 <= letras <= 64 + len(goban) and 1 <= linha <= len(goban):
        return True
    else:
        return False


def gobans_iguais(g1, g2):
    """
    A função recebe dois tabuleiros goban, e devolve true caso os dois tabuleiros sejam iguais
    :param g1: tabuleiro 1 goban
    :param g2: tabuleiro 2 goban
    :return: True or false
    """
    if g1 == g2:
        return True
    else:
        return False


def goban_para_str(goban):
    """
    Recebe um tabuleiro e devolve o tabuleiro em string
    :param goban: tabuleiro goban
    :return: string da representação do tabuleiro
    """
    letras = []  # lista com as letras do terriorio
    numeros = []  # lista com os numeros do territorio
    string_do_territorio = "  "

    for subtuplo in range(obtem_lin(obtem_ultima_intersecao(goban))):
        letras += chr(ord("A") + subtuplo)

    for i in range(1, len(goban) + 1):
        numeros += [i]

    for letra in letras:
        string_do_territorio += " " + letra
    string_do_territorio += "\n"

    for numero in numeros[-1: -len(numeros) - 1: -1]:
        string_do_territorio += f"{numero:>2}"
        for letra in letras:
            if eh_pedra_preta(goban[ord(letra) - 65][numero - 1]):
                string_do_territorio += " X"
            if eh_pedra_branca(goban[ord(letra) - 65][numero - 1]):
                string_do_territorio += " O"
            if not eh_pedra_jogador(goban[ord(letra) - 65][numero - 1]):
                string_do_territorio += " ."
        string_do_territorio += " " + f"{numero:>2}" + "\n"
    string_do_territorio += "  "

    for letra in letras:
        string_do_territorio += " " + letra
    return string_do_territorio


def obtem_territorios(goban):
    """
    Recebe um tabuleiro goban n*n, e devolve um tuplo com todos os territorio do goban
    :param goban: goban n*n
    :return: tuplo de territorios
    """
    candidatos = ()
    final = ()
    for coluna in range(obtem_lin(obtem_ultima_intersecao(goban))):
        for indice_linha in range(len(goban[coluna])):
            intersecao = ((chr(ord("A") + coluna)), indice_linha + 1)
            if not eh_pedra_jogador(goban[coluna][indice_linha]) and obtem_cadeia(goban, intersecao) not in candidatos:
                candidatos += (obtem_cadeia(goban, intersecao),)
    return candidatos


def eh_pedra_intersecao_jogador(g, intersecao):
    """
    Recebe um tabuleiro goban n*n, e uma intersecao. E verificar na intersecao se é uma pedra de um dos jogadores
    ou uma pedra neutra
    :param g: goban n*n
    :param intersecao: intersecao
    :return: True se a pedra for de um jogador, false caso neutra
    """
    coluna = num_coluna(intersecao)
    linha = num_linha(intersecao)
    if eh_pedra_preta(g[coluna][linha]) or eh_pedra_branca(g[coluna][linha]):
        return True
    else:
        return False


def obtem_adjacentes_diferentes(goban, intersecoes):  # maybe fixed??
    """
    Recebe um tabuleiro de goban n*n, e um tuplo de intersecoes. Devolve um tuplo das intersecoes adjacentes que sejam
    diferentes do tipo fornecido
    :param goban:tabuleiro goban n*n
    :param intersecoes:tuplo de intersecoes
    :return:
    """
    listat = []
    for intersecao in intersecoes:
        if intersecao not in listat:
            if eh_pedra_intersecao_jogador(goban, intersecao):
                for i in intersecoes_livres(goban, intersecao):
                    if i not in listat:
                        listat += (i,)
            if not eh_pedra_intersecao_jogador(goban, intersecao):
                for i in intersecoes_ocupadas(goban, intersecao):
                    if i not in listat:
                        listat += (i,)
    return ordena_intersecoes(listat)


def intersecoes_livres(goban, intersecao):
    """
    Função auxiliar que caso receba uma intersecão que seja livre irá devolver as ocupadas por jogador ao seu lado
    :param goban: tabuleiro de goban
    :param intersecao:
    :return: tuplo com as intersecoes adjacentes
    """
    candidatos = obtem_intersecoes_adjacentes(intersecao, obtem_ultima_intersecao(goban))
    return [candidato for candidato in candidatos if not eh_pedra_intersecao_jogador(goban, candidato)]


def intersecoes_ocupadas(goban, intersecao):
    """
    Função auxiliar que caso receba uma intersecão que seja ocupada irá devolver as livres ao seu lado
    :param goban: tabuleiro de goban
    :param intersecao:
    :return: tuplo com as intersecoes adjacentes
    """
    candidatos = obtem_intersecoes_adjacentes(intersecao, obtem_ultima_intersecao(goban))
    return [candidato for candidato in candidatos if eh_pedra_intersecao_jogador(goban, candidato)]


def jogada(goban, intersecao, pedra):
    """
    Recebe um tabuleiro n*n, na intersecao ira colocar a pedra, e caso as adjacentes fiquem sem liberdade ira remove-las
    :param goban: tabuleiro goban n*n
    :param intersecao:
    :param pedra:
    :return: tabuleiro modificado
    """
    coloca_pedra(goban, intersecao, pedra)
    for intersecoes in obtem_intersecoes_adjacentes(intersecao, obtem_ultima_intersecao(goban)):
        candidatos = obtem_cadeia(goban, intersecoes)
        for intersecoes2 in candidatos:
            if not obtem_adjacentes_diferentes(goban, candidatos):
                remove_cadeia(goban, candidatos)

    return goban


def obtem_pedras_jogadores(g):
    """
    Vai percorrer o tabuleiro e contando as peças de jogador que encontrar, no fim dá return de quantas peças
    cada jogador tem no tabuleiro
    :param g:Tabuleiro goban n*n
    :return: (numero de pedras jogador branco, numero de pedras jogador preto)
    """
    countpreto = 0
    countbranco = 0
    for lista in g:
        for intersecao in lista:
            if eh_pedra_preta(intersecao):
                countpreto += 1
            if eh_pedra_branca(intersecao):
                countbranco += 1
    return (countbranco, countpreto)


def calcula_pontos(goban):
    """
    Vai receber um tabuleiro, e contar todas as peças dos jogadores pois 1 peça equivalente a 1 ponto, e verificar se
    os territorios são restringidos por um so tipo de peça transformando assim em pontos
    :param goban:
    :return: (numero de pontos jogador branco, numero de pontos jogador preto)
    """
    pontosbrancos, pontospretos = obtem_pedras_jogadores(goban)  # cada pedra 1 ponto
    territorios = obtem_territorios(goban)
    for territorio in territorios:
        candidatos = obtem_adjacentes_diferentes(goban, territorio)
        listav = [obtem_pedra(goban, i) for i in candidatos]
        if all(x == listav[0] for x in listav):
            if eh_pedra_preta(listav[0]):
                pontospretos += len(territorio)
            elif eh_pedra_branca(listav[0]):
                pontosbrancos += len(territorio)
    return pontosbrancos, pontospretos


def eh_jogada_legal(goban, intersecao, pedra, verificagoban):
    """
    Verifica se a jogada do jogador é legal, ou seja se não é suicidio ou repetida
    :param goban: tabuleiro goban
    :param intersecao:
    :param pedra:
    :param verificagoban: copia goban
    :return: bool
    """
    if not eh_intersecao_valida(goban, intersecao) or eh_pedra_jogador(obtem_pedra(goban, intersecao)):
        return False
    copiadogoban = cria_copia_goban(goban)
    jogada(copiadogoban, intersecao, pedra)
    if len(obtem_adjacentes_diferentes(copiadogoban, obtem_cadeia(copiadogoban, intersecao))) == 0:
        return False
    if not gobans_iguais(copiadogoban, verificagoban):
        return True
    else:
        return False


def verifica_string(stringintersecao):
    """
    A função verifica se a str introduzida pelo jogador é um intersecao valida
    :param stringintersecao:
    :return:bool
    """
    if not isinstance(stringintersecao, str):
        return False
    if len(stringintersecao) not in (3, 2):
        return False
    intersecao_a_validar = str_para_intersecao(stringintersecao)
    if eh_intersecao(intersecao_a_validar):
        return True
    else:
        return False


def turno_jogador(goban, pedra, verificagoban):
    """
    Recebe um goban n*n, e dependendo do jogador, pede uma interseção para colocar a pedra ou 'P', caso receba o 'P'
    devolve False o que significa que o jogador passou a vez, ou então modifica o goban de forma destrutiva.
    :param goban:Tabuleiro goban n*n
    :param pedra:
    :param verificagoban:
    :return:bool
    """
    indice = 1
    while indice == 1:
        if eh_pedra_preta(pedra):
            jogada_jogador = input("Escreva uma intersecao ou 'P' para passar [X]:")
        elif eh_pedra_branca(pedra):
            jogada_jogador = input("Escreva uma intersecao ou 'P' para passar [O]:")
        if jogada_jogador == 'P':
            return False
        if verifica_string(jogada_jogador):
            intersecaojogador = str_para_intersecao(jogada_jogador)
            if eh_intersecao_valida(goban, intersecaojogador):
                copygoban = cria_copia_goban(goban)
                if eh_jogada_legal(copygoban, intersecaojogador, pedra, verificagoban):
                    jogada(goban, intersecaojogador, pedra)
                    indice -= 1
    return True


def go(n, tb, tp):
    pass
