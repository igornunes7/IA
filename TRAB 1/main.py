Nenhum selecionado

Pular para o conteúdo
Como usar o E-mail de Ciência da Computação e Sistemas de Informação com leitores de tela

4 de 1.574
TRAB PYYYYY
Caixa de entrada

Igor Monteiro Nunes <rgm47538@comp.uems.br>
Anexos
08:46 (há 7 horas)
para mim


 1 anexo
  •  Verificados pelo Gmail
from collections import deque
import heapq

PUZZLE = (
    1, 2, 3,
    4, "B", 5,
    6, 7, 8
)

#------------------------------MENUS------------------------------

def menu_heuristica():
    return int(input(
        "ESCOLHA A HEURISTICA\n"
        "1 - PEÇAS FORA DO LUGAR (Sugestao 1)\n"
        "2 - DIFERENÇA AO QUADRADO (Sugestao 2)\n"
        "3 - DISTÂNCIA MANHATTAN (Sugestao 3)\n"
        "0 - SAIR\n"
        "Escolha: "
    ))

def menu_principal():
    return int(input(
        "\n1 - BUSCAS NAO INFORMADAS\n"
        "2 - BUSCAS INFORMADAS\n"
        "0 - VOLTAR\n"
        "Escolha: "
    ))

def menu_nao_informadas():
    return int(input(
        "\n1 - BUSCA EM LARGURA\n"
        "2 - BUSCA CUSTO UNIFORME\n"
        "3 - BUSCA EM PROFUNDIDADE\n"
        "4 - BUSCA EM PROFUNDIDADE LIMITADA\n"
        "0 - VOLTAR\n"
        "Escolha: "
    ))

def menu_informadas():
    return int(input(
        "\n1 - BUSCA GULOSA\n"
        "2 - BUSCA A*\n"
        "3 - BUSCA IDA* (Iterative deepning A*)\n"
        "0 - VOLTAR\n"
        "Escolha: "
    ))


def escolher_heuristica(op, objetivo):
    if op == 1:
        return lambda estado: heuristica_fora_do_lugar(estado, objetivo)
    elif op == 2:
        return lambda estado: heuristica_diferenca_quadrado(estado, objetivo)
    elif op == 3:
        return lambda estado: heuristica_manhattan(estado, objetivo)
    else:
        return lambda estado: heuristica_manhattan(estado, objetivo)


def menu_objetivo():
    return int(input(
        "\nESCOLHA O OBJETIVO\n"
        "1 - PADRÃO (1 2 3 / 4 B 5 / 6 7 8)\n"
        "2 - PERSONALIZADO (informar puzzle objetivo)\n"
        "Escolha: "
    ))

#------------------------------LEITURAS------------------------------

def ler_estado(titulo="inicial"):
    estado = []

    print(f"\nDigite o estado {titulo} do puzzle")
    print("Use números de 1 a 8 e B (ou b) para o espaço em branco\n")

    for linha in range(3):
        for coluna in range(3):

            valor = input(f"Digite a célula {linha}{coluna}: ").strip().upper()

            if valor == "B":
                estado.append("B")
            else:
                estado.append(int(valor))

    return tuple(estado)


def ler_objetivo():
    op = menu_objetivo()
    print("--------------------------------")

    if op == 2:
        return ler_estado("objetivo")

    return PUZZLE

#------------------------------IMPRIMIR------------------------------

def imprimir_tabuleiro(estado):
    for i in range(0, 9, 3):
        print(estado[i], estado[i + 1], estado[i + 2])
    print()


def imprimir_caminho(caminho):
    if caminho is None:
        print("Nenhum caminho encontrado")
        return

    if caminho == "cutoff":
        print("Cutoff: o limite foi atingido antes de encontrar a solução")
        return

    print(f"Quantidade de movimentos: {len(caminho) - 1}\n")

    for passo, estado in enumerate(caminho):
        print(f"Passo {passo}:")
        imprimir_tabuleiro(estado)



#------------------------------GERAR VIZINHOS------------------------------


def gerar_vizinhos(estado):
    vizinhos = []

    indice_b = estado.index("B")
    linha = indice_b // 3
    coluna = indice_b % 3

    movimentos = [
        (-1, 0),  # cima
        (1, 0),   # baixo
        (0, -1),  # esquerda
        (0, 1)    # direita
    ]

    for dl, dc in movimentos:
        nova_linha = linha + dl
        nova_coluna = coluna + dc

        if 0 <= nova_linha < 3 and 0 <= nova_coluna < 3:
            novo_indice = nova_linha * 3 + nova_coluna

            novo_estado = list(estado)
            novo_estado[indice_b], novo_estado[novo_indice] = novo_estado[novo_indice], novo_estado[indice_b]

            vizinhos.append(tuple(novo_estado))

    return vizinhos

#------------------------------HEURISTICAS------------------------------

def heuristica_fora_do_lugar(estado, objetivo):
    total = 0

    for i in range(9):
        if estado[i] != "B" and estado[i] != objetivo[i]:
            total += 1

    return total


def heuristica_diferenca_quadrado(estado, objetivo):
    total = 0

    for i in range(9):
        valor = estado[i]

        if valor != "B":
            pos_objetivo = objetivo.index(valor)
            total += (i - pos_objetivo) ** 2

    return total


def heuristica_manhattan(estado, objetivo):
    total = 0

    for i in range(9):
        valor = estado[i]

        if valor != "B":
            pos_objetivo = objetivo.index(valor)

            linha_atual = i // 3
            coluna_atual = i % 3

            linha_obj = pos_objetivo // 3
            coluna_obj = pos_objetivo % 3

            total += abs(linha_atual - linha_obj) + abs(coluna_atual - coluna_obj)

    return total

#------------------------------NAO INFORMADAS------------------------------


def busca_largura(inicio, objetivo):
    fila = deque([inicio])
    explorado = set()
    origem = {inicio: None}

    while fila:
        atual = fila.popleft()

        if atual == objetivo:
            caminho = []

            while atual is not None:
                caminho.append(atual)
                atual = origem[atual]

            return list(reversed(caminho))

        explorado.add(atual)

        for vizinho in gerar_vizinhos(atual):
            if vizinho not in explorado and vizinho not in fila:
                origem[vizinho] = atual
                fila.append(vizinho)

    return None



def busca_custo_uniforme(inicio, objetivo):
    contador = 0

    fila = [(0, contador, inicio)]
    origem = {inicio: None}
    custo = {inicio: 0}
    explorado = set()

    while fila:
        custo_atual, _, atual = heapq.heappop(fila)

        if atual in explorado:
            continue

        if atual == objetivo:
            caminho = []

            while atual is not None:
                caminho.append(atual)
                atual = origem[atual]

            return list(reversed(caminho)), custo_atual

        explorado.add(atual)

        for vizinho in gerar_vizinhos(atual):
            novo_custo = custo_atual + 1

            if vizinho not in custo or novo_custo < custo[vizinho]:
                custo[vizinho] = novo_custo
                origem[vizinho] = atual

                contador += 1
                heapq.heappush(fila, (novo_custo, contador, vizinho))

    return None, float("inf")



def busca_profundidade(inicio, objetivo):
    pilha = [inicio]
    explorado = set()
    origem = {inicio: None}

    while pilha:
        atual = pilha.pop()

        if atual == objetivo:
            caminho = []

            while atual is not None:
                caminho.append(atual)
                atual = origem[atual]

            return list(reversed(caminho))

        if atual not in explorado:
            explorado.add(atual)

            for vizinho in gerar_vizinhos(atual):
                if vizinho not in explorado and vizinho not in pilha:
                    origem[vizinho] = atual
                    pilha.append(vizinho)

    return None



def busca_profundidade_limitada(inicio, objetivo, limite):

    def dls_recursiva(atual, limite, caminho):
        if atual == objetivo:
            return caminho

        if limite == 0:
            return "cutoff"

        ocorreu_cutoff = False

        for vizinho in gerar_vizinhos(atual):
            if vizinho not in caminho:
                resultado = dls_recursiva(vizinho, limite - 1, caminho + [vizinho])

                if resultado == "cutoff":
                    ocorreu_cutoff = True
                elif resultado is not None:
                    return resultado

        if ocorreu_cutoff:
            return "cutoff"

        return None

    return dls_recursiva(inicio, limite, [inicio])

#------------------------------INFORMADAS------------------------------

def busca_gulosa(inicio, objetivo, heuristica):

    contador = 0
    fila = [(heuristica(inicio), contador, inicio)]
    origem = {inicio: None}
    explorado = set()

    while fila:
        _, _, atual = heapq.heappop(fila)

        if atual in explorado:
            continue

        if atual == objetivo:
            caminho = []

            while atual is not None:
                caminho.append(atual)
                atual = origem[atual]

            return list(reversed(caminho))

        explorado.add(atual)

        for vizinho in gerar_vizinhos(atual):
            if vizinho not in explorado:
                contador += 1
                origem[vizinho] = atual
                heapq.heappush(
                    fila,
                    (heuristica(vizinho), contador, vizinho)
                )

    return None




def busca_a_estrela(inicio, objetivo, heuristica):
    contador = 0

    fila = [(heuristica(inicio), 0, contador, inicio)]
    origem = {inicio: None}
    custo = {inicio: 0}
    explorado = set()

    while fila:
        _, custo_atual, _, atual = heapq.heappop(fila)

        if atual in explorado:
            continue

        if atual == objetivo:
            caminho = []

            while atual is not None:
                caminho.append(atual)
                atual = origem[atual]

            return list(reversed(caminho)), custo_atual

        explorado.add(atual)

        for vizinho in gerar_vizinhos(atual):
            novo_custo = custo_atual + 1

            if vizinho not in custo or novo_custo < custo[vizinho]:
                custo[vizinho] = novo_custo
                origem[vizinho] = atual

                f = novo_custo + heuristica(vizinho)

                contador += 1
                heapq.heappush(fila, (f, novo_custo, contador, vizinho))

    return None, float("inf")



def busca_ida_estrela(inicio, objetivo, heuristica):
    limite = heuristica(inicio)

    def procurar(caminho, g, limite):
        atual = caminho[-1]
        f = g + heuristica(atual)

        if f > limite:
            return f

        if atual == objetivo:
            return list(caminho)

        menor = float("inf")

        for vizinho in gerar_vizinhos(atual):
            if vizinho not in caminho:
                caminho.append(vizinho)

                resultado = procurar(caminho, g + 1, limite)

                if isinstance(resultado, list):
                    return resultado

                menor = min(menor, resultado)

                caminho.pop()

        return menor

    caminho = [inicio]

    while True:
        resultado = procurar(caminho, 0, limite)

        if isinstance(resultado, list):
            return resultado

        if resultado == float("inf"):
            return None

        limite = resultado



#------------------------------MAIN------------------------------

while True:
    op = menu_principal()
    print("--------------------------------")

    if op == 0:
        print("Saindo...")
        break

    elif op == 1:
        while True:
            sub_op = menu_nao_informadas()
            print("--------------------------------")

            if sub_op == 0:
                break

            inicio = ler_estado("inicial")
            objetivo = ler_objetivo()

            if sub_op == 1:
                caminho = busca_largura(inicio, objetivo)
                imprimir_caminho(caminho)

            elif sub_op == 2:
                caminho, custo_total = busca_custo_uniforme(inicio, objetivo)
                imprimir_caminho(caminho)
                print("Custo total:", custo_total)

            elif sub_op == 3:
                caminho = busca_profundidade(inicio, objetivo)
                imprimir_caminho(caminho)

            elif sub_op == 4:
                limite = int(input("Digite o limite: "))
                caminho = busca_profundidade_limitada(inicio, objetivo, limite)
                imprimir_caminho(caminho)

    elif op == 2:
        op_h = menu_heuristica()
        print("--------------------------------")

        if op_h == 0:
            continue

        while True:
            sub_op = menu_informadas()
            print("--------------------------------")

            if sub_op == 0:
                break

            inicio = ler_estado("inicial")
            objetivo = ler_objetivo()
            heuristica = escolher_heuristica(op_h, objetivo)

            if sub_op == 1:
                caminho = busca_gulosa(inicio, objetivo, heuristica)
                imprimir_caminho(caminho)

            elif sub_op == 2:
                caminho, custo_total = busca_a_estrela(inicio, objetivo, heuristica)
                imprimir_caminho(caminho)
                print("Custo total:", custo_total)

            elif sub_op == 3:
                caminho = busca_ida_estrela(inicio, objetivo, heuristica)
                imprimir_caminho(caminho)
trab.py
Exibindo trab.py.
