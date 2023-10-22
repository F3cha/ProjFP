
def eh_territorio(territorio):
    """eh territorio(t) recebe um argumento de qualquer tipo e devolve True se o seu argu-
    mento corresponde a um território e False caso contrário, sem nunca gerar erros. Nesta
    parte do projeto, considere que um território corresponde a um tuplo de tuplos como
    descrito, e que o território contêm no minimo 1 caminho vertical e 1 caminho horizontal."""
    if not isinstance(territorio, tuple):
        return False
    if not (26>=len(territorio)>=1): #verifica se o tuplo esta compreendido entre 1-26 ou seja A-Z,
        return False
    for subtuplo in territorio:
        if not isinstance(subtuplo, tuple):
            return False
        if len(territorio[0])<1 or len(territorio[0])>99:#verifica se cada subtuplo tem entre 1 e 99 elementos
            return False
        size= len(territorio[0])
        if len(subtuplo)!=size:#compara se todos os subtuplos tem o mesmo len
            return False
        for membro in subtuplo:#vai avaliar se cada membro do subtuplo é um int e se o membro é 1/0
            if not isinstance(membro,int):
                return False
            if membro !=0 and membro!=1:
                return False
    return True
    
def obtem_ultima_intersecao(t):
    """obtem ultima intersecao(t) recebe um território e devolve a intersecao do extremo supe-
    rior direito do território."""
    return (chr(len(t) + ord('A')-1),len(t[0])) 

    


def eh_intersecao(arg):#feita
    """eh intersecao(arg) recebe um argumento de qualquer tipo e devolve True se o seu ar
    gumento corresponde a uma interseção e False caso contrário, sem nunca gerar erros.
    Nesta parte do projeto, considere que uma interseção corresponde a um tuplo como
    descrito."""
    if type(arg)!=tuple or len(arg)!=2:#vai avaliar se argumento fornecido é um tuplo e se não é fornecido + ou menos que dois parametros
        return False
    if not isinstance(arg[1], int):#avalia se o segundo elemento corresponde a um inteiro
        return False
    if not isinstance(arg[0], str):#avalia 
        return False
    if len(arg[0])!=1:
        return False
    if not(ord('A')<=ord(arg[0])<=ord('Z')):
        return False   
    if 1>arg[1] or arg[1]>99:
        return False
    else:
        return True
    




def eh_intersecao_valida(t,i):#feita
    """eh intersecao valida(t, i) recebe um território e uma interseção, e devolve True se a
    interseção corresponde a uma interseção do território, e False caso contrário."""
    if not ord('A')<=ord(i[0])<=ord('A')+len(t)-1:#avalia se a letra esta entre 1 e o numero total de subtuplos do territorio
        return False
    elif not 1<=i[1]<=len(t[0]):#avalia se o numero fornecido está dentro dos parametros do terriorio
        return False
    else: 
        return True  

def eh_intersecao_livre(t,i):#feita
    """
    eh intersecao livre(t, i) recebe um território e uma interseção do território, e devolve
    True se a interseção corresponde a uma interseção livre (não ocupada por montanhas)
    dentro do território e False caso contrário."""
    subtuplo= ord(i[0])-ord('A') 
    numero=i[1]-1 #i[1] começa a partir de 1, logo retiramos 1 para que possa contar o termo nº0
    if t[subtuplo][numero] == 1:#caso seja igual a 1 é uma montanha
        return False
    elif t[subtuplo][numero] == 0:#caso seja igual a 0 é um vale
        return True

def obtem_intersecoes_adjacentes(t,i):#feita 
    """obtem intersecoes adjacentes(t, i) recebe um território e uma interseção do território, e
    devolve o tuplo formado pelas interseções válidas adjacentes da interseção em ordem de
    leitura de um território."""
    if type(t)!=tuple or type(i)!=tuple:
        raise ValueError("Não foram fornecidos tuplos corretos")
    
    adjacentes=()
    letra= ord(i[0])-ord('A')
    numero= i[1]-1
    
    if numero>0:
        adjacentes+= ((i[0],i[1]-1),)
    if letra>0:
        adjacentes+= ((chr(ord(i[0])-1),i[1]),)
    if letra<len(t)-1:
        adjacentes+= ((chr(ord(i[0])+1),i[1]),)
    if numero<len(t[0])-1:
        adjacentes+=  ((i[0], i[1]+1),)
    return adjacentes

        

def ordena_intersecoes (arg):#feito
    """ordena intersecoes(tup) recebe um tuplo de interseções (potencialmente vazio) e devolve
    um tuplo contendo as mesmas interseções ordenadas de acordo com a ordem de leitura
    do território."""
    return tuple(sorted(arg, key= lambda x:(x[1],x[0])))
        


def territorio_para_str (territorio):#feita 
    """territorio para str(t) recebe um território e devolve a cadeia de caracteres que o repre-
    senta (a representação externa ou representação “para os nossos olhos”), de acordo com
    o exemplo na seguinte interação. Se o argumento dado for inválido, a função deve gerar
    um erro com a mensagem 'territorio_para_str: argumento invalido'."""
    
    letras=[]#lista com as letras do terriorio
    numeros=[]#lista com os numeros do territorio
    stringdoterritorio='  '
    
    for subtuplo in range(len(territorio)):
        letras+=(chr(ord('A')+subtuplo))

    for linhas in range(len(territorio[0])):
         numeros= numeros+ [linhas+1]

    for letra in letras:
        stringdoterritorio+= ' '+letra
    stringdoterritorio+= '\n'

    for numero in numeros[-1:-len(numeros)-1:-1]:
        stringdoterritorio+= f"{numero:>2}"
        for letra in letras:
            if eh_intersecao_livre(territorio,(letra,numero)):
                stringdoterritorio+= ' .'
            else:
                stringdoterritorio+= ' X'
        stringdoterritorio+= ' '+f"{numero:>2}"+'\n'
    stringdoterritorio+= '  '
    
    for letra in letras:
        stringdoterritorio+= ' '+letra
    return stringdoterritorio




def obtem_cadeia (t,i):#feito
    """obtem cadeia(t,i) recebe um território e uma interseção do território (ocupada por uma
    montanha ou livre), e devolve o tuplo formado por todas as interseções que estão cone-
    tadas a essa interseção ordenadas (incluida si própria) de acordo com a ordem de leitura
    de um território. Se algum dos argumentos dado for inválido, a função deve gerar um
    erro com a mensagem 'obtem_cadeia: argumentos invalidos'.
    """
    if not (eh_territorio(t) and eh_intersecao(i) and eh_intersecao_valida(t,i)):
        raise ValueError('obtem_cadeia: argumentos invalidos')
    
    listav=[i]
    indice=0
    candidatos= obtem_intersecoes_adjacentes(t,listav[indice])#vai devolver lista com os tuplos

    while candidatos:
        for um in candidatos:
            if um not in listav:
                if eh_intersecao_livre(t,um)==eh_intersecao_livre(t,i) :
                 listav+=[um]
        indice+=1
        if indice==len(listav):
            return tuple(ordena_intersecoes(listav))
        candidatos=obtem_intersecoes_adjacentes(t,listav[indice])



def obtem_vale(t,i):#rever
    """obtem vale(t,i) recebe um território e uma interseção do território ocupada por uma mon-
    tanha, e devolve o tuplo (potencialmente vazio) formado por todas as interseções que for-
    mam parte do vale da montanha da interseção fornecida como argumento ordenadas de
    acordo à ordem de leitura de um território. Se algum dos argumentos dado for inválido,
    a função deve gerar um erro com a mensagem 'obtem_vale: argumentos invalidos'."""

    list=[]

    if not (eh_territorio(t) and eh_intersecao(i) and eh_intersecao_valida(t,i)):
        raise ValueError('obtem_vale: argumentos invalidos')
    if eh_intersecao_livre(t,i):
        raise ValueError('obtem_vale: argumentos invalidos')

    for interseções in obtem_cadeia(t,i):
        for candidato in obtem_intersecoes_adjacentes(t,interseções):
            if eh_intersecao_livre(t,candidato):
                    if candidato not in list:
                        list+=[candidato]
    return ordena_intersecoes(tuple(list))
    # obter a cadeia do i
    # obter as interseções adjacentes de todas as interceções pertencentes à cadeia do i
    # se essas interceções forem livres adicionar a um tuplo
    # retornar o tuplo sorted 
    #return ordena_intersecoes(tuple(list))


def verifica_conexao(t,i1,i2):#rever(deve estar bem)
    """verifica_conexao(t,i1,i2) recebe um território e duas interseções do território e devolve
    True se as duas interseções estão conetadas e False caso contrário. Se algum dos
    argumentos dado for inválido, a função deve gerar um erro com a mensagem
    'verifica_conexao: argumentos invalidos'."""
    try:
        if not(eh_territorio(t) and eh_intersecao_valida(t,i1) and eh_intersecao_valida(t,i2)):
            raise ValueError('verifica_conexao: argumentos invalidos')
        if obtem_cadeia(t,i1)==obtem_cadeia(t,i2):#possivelmente o erro é derivado ao obtem_cadeia
            return True
        else:return False
    except:
        raise ValueError('verifica_conexao: argumentos invalidos')
    

def calcula_numero_montanhas(t):#feito
    """calcula_numero_montanhas(t) recebe um território e devolve o número de interseções
    ocupadas por montanhas no território. Se o argumento dado for inválido, a função deve
    gerar um erro com a mensagem 'calcula_numero_montanhas: argumento invalido'."""

    soma=0

    if not eh_territorio(t):
        raise ValueError('calcula_numero_montanhas: argumento invalido')
    for subtuplo in range(len(t)):
        for i in t[subtuplo]:#vai percorrer todas as interseções, e caso seja montanha vai adicionar mais 1
            if i==1:
                soma+=1
    return soma


def calcula_numero_cadeias_montanhas(t):#rever
    """calcula numero cadeias montanhas(t) recebe um território e devolve o número de cadeias
    de montanhas contidas no território. Se o argumento dado for inválido, a função deve ge-
    rar um erro com a mensagem 'calcula_numero_cadeias_montanhas: argumento invalido'."""
    try:
        if not eh_territorio(t):
            raise ValueError('calcula_numero_cadeias_montanhas: argumento invalido')
        if calcula_numero_montanhas(t) == 0:
            return 0

        candidatos=[]
        cadeia=()
        resultadofinal=0

        for subtuplo in range(len(t)):
            for membro in range(len(t[subtuplo])):
                if not eh_intersecao_livre(t,(chr(65+subtuplo),membro+1)):
                    candidatos+=((chr(65+subtuplo),membro+1),)#vai criar uma lista com todos os candidatos/montanhas
        for i in range(len(ordena_intersecoes(candidatos))):
            if candidatos[i] not in cadeia:
                possivel = obtem_cadeia(t, candidatos[i])#e vai ver se a cadeia do candidato ja foi registada
            if possivel not in cadeia:
                resultadofinal+=1
                cadeia+= (possivel,)
        return resultadofinal
    
    except: 
        raise ValueError('calcula_numero_cadeias_montanhas: argumento invalido')#como uma das funções utilizadas poderia gerar um erro, retornamos com o erro da propria função
    

        

def calcula_tamanho_vales(t):
    """calcula tamanho vales(t) recebe um território e devolve o número total de interseções
    diferentes que formam todos os vales do território. Por exemplo, na Figura 1c) o ta-
    manho dos vales é de 6 interseções, marcadas com pontos amarelos, verdes e verde-
    amarelos. Se o argumento dado for inválido, a função deve gerar um erro com a mensa-
    gem 'calcula_tamanho_vales: argumento invalido'."""
    if not eh_territorio(t):
        raise ValueError('calcula_tamanho_vales: argumento invalido')

    montanhas=[]
    possiveis_vales=[]
    lista=[]

    for subtuplo in range(len(t)):
        for membro in range(len(t[subtuplo])):
            if t[subtuplo][membro]==1:
               montanhas+=((chr(65+subtuplo),membro+1),)#vai gerar uma lista com todas as montanhas 
    for i in montanhas:
        possiveis_vales+=obtem_intersecoes_adjacentes(t,i)#vai obter uma lista com os membros ao lado das montanhas,incluindo as montanhas e os vales
    for candidatos in possiveis_vales:#vai percorrer todos os adjacentes e avaliar quais sao vales
        if eh_intersecao_livre(t,candidatos) and candidatos not in lista:
            lista+=(candidatos,)#caso seja vale e não esteja ja na lista vai ser adicionado
    return len(lista)
    






        

            




