## 8-Puzzle Solver com Algoritmos de Busca

Projeto desenvolvido para a disciplina de Inteligência Artificial utilizando Python.

O programa resolve o problema do **8-puzzle** utilizando algoritmos de busca informadas e não informadas.

---

# Algoritmos Implementados

## Buscas Não Informadas
- Busca em Largura (BFS)
- Busca de Custo Uniforme (UCS)
- Busca em Profundidade (DFS)
- Busca em Profundidade Limitada (DLS)

---

## Buscas Informadas
- Busca Gulosa
- Busca A*
- Busca IDA* (Iterative Deepening A*)

---

# Heurísticas Implementadas

## Peças Fora do Lugar
Conta quantas peças estão na posição errada.

---

## Diferença ao Quadrado
Calcula:
(posição\ atual - posição\ correta)^2
para cada peça do puzzle.

Quanto mais longe a peça estiver da posição correta, maior será o valor da heurística.

---

## Distância Manhattan
Calcula quantos movimentos cada peça precisa realizar para chegar até sua posição correta.

Essa heurística normalmente apresenta melhores resultados, pois representa melhor a distância real até o objetivo.

---

# Funcionamento do Programa

O funcionamento do programa segue as seguintes etapas:

1. O usuário escolhe o tipo de busca:
   - Buscas não informadas
   - Buscas informadas

2. O usuário informa os estados do puzzle:
   - Estado inicial
   - Estado objetivo

3. O programa gera novos estados possíveis movimentando o espaço em branco (`B`).

4. O algoritmo de busca explora os estados gerados até encontrar a solução.

5. Ao final, o caminho solução é exibido passo a passo.
