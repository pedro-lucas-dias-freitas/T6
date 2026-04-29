from graph import Graph

def is_tree(g):
    """
    Verifica se o grafo é uma árvore válida.
    Condições: Grafo deve ser conexo e ter exatamente V - 1 arestas.
    """
    if g.V() == 0:
        return False
    
    if g.E() != g.V() - 1:
        return False

    visited = [False] * g.V()
    
    def dfs(v):
        visited[v] = True
        for w in g.adj(v):
            if not visited[w]:
                dfs(w)

    dfs(0)
    
    return all(visited)


def treeCenters(g):
    """
    Algoritmo de remoção iterativa de folhas para encontrar o(s) centro(s).
    Retorna uma lista com 1 ou 2 vértices.
    """
    n = g.V()
    if n == 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]

    degrees = [0] * n
    for v in range(n):
        degrees[v] = len(g.adj(v))

    L = [v for v in range(n) if degrees[v] <= 1]
    
    processados = len(L)

    while processados < n:
        novasFolhas = []
        for u in L:
            for v in g.adj(u):
                degrees[v] -= 1
                if degrees[v] == 1:
                    novasFolhas.append(v)
        
        processados += len(novasFolhas)
        L = novasFolhas

    return L


def encode(g, root, parent):
    """
    Percorre a árvore recursivamente gerando o código canônico
    através da ordenação lexicográfica dos filhos.
    """
    children_codes = []
    
    for c in g.adj(root):
        if c != parent:
            children_codes.append(encode(g, c, root))
            
    if not children_codes:
        return "()"
        
    children_codes.sort()
    
    concatenacao = "".join(children_codes)
    
    return "(" + concatenacao + ")"


def get_canonical_encoding(g):
    """
    Encontra os centros, enraíza e gera a representação estrutural única.
    Trata corretamente o caso de árvores bicêntricas.
    """
    centers = treeCenters(g)
    
    if len(centers) == 1:
        return encode(g, centers[0], -1)
    else:
        code1 = encode(g, centers[0], -1)
        code2 = encode(g, centers[1], -1)
        return min(code1, code2)