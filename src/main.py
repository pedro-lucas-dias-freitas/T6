import sys
from graph import Graph
import tree_isomorphism as ti

def main():
    if len(sys.argv) < 3:
        print("Uso correto: python main.py <arquivo1.txt> <arquivo2.txt>")
        sys.exit(1)

    file1 = sys.argv[1]
    file2 = sys.argv[2]

    try:
        g1 = Graph(file1)
        g2 = Graph(file2)
    except Exception as e:
        print(f"Erro ao ler os arquivos de grafo: {e}")
        sys.exit(1)

    print("=== ESTRUTURAS LIDAS ===")
    print(f"--- Árvore 1 ({file1}) ---")
    print(g1.to_string())
    print()
    print(f"--- Árvore 2 ({file2}) ---")
    print(g2.to_string())

    print("\n=== VALIDAÇÃO DE ENTRADAS ===")
    valid_g1 = ti.is_tree(g1)
    valid_g2 = ti.is_tree(g2)
    
    print(f"A entrada 1 é uma árvore válida? {'Sim' if valid_g1 else 'Não'}")
    print(f"A entrada 2 é uma árvore válida? {'Sim' if valid_g2 else 'Não'}")
    
    if not valid_g1 or not valid_g2:
        print("\n[ERRO] Uma ou ambas as entradas não representam uma árvore válida.")
        print("Motivo: Um grafo deve ser conexo e possuir exatamente V-1 arestas.")
        print("Análise de isomorfismo abortada.")
        sys.exit(0)

    print("\n=== ANÁLISE DE CENTROS E CODIFICAÇÃO CANÔNICA ===")
    
    centers1 = ti.treeCenters(g1)
    code1 = ti.get_canonical_encoding(g1)
    print(f"Árvore 1 -> Centro(s) encontrado(s): {centers1}")
    print(f"Árvore 1 -> Código Canônico: {code1}")
    print()
    
    # CENTROS E CODIFICAÇÃO ÁRVORE 2
    centers2 = ti.treeCenters(g2)
    code2 = ti.get_canonical_encoding(g2)
    print(f"Árvore 2 -> Centro(s) encontrado(s): {centers2}")
    print(f"Árvore 2 -> Código Canônico: {code2}")
    
    print("\n=== RESULTADO FINAL ===")
    if code1 == code2:
        print("RESULTADO: As árvores são ISOMORFAS.")
    else:
        print("RESULTADO: As árvores NÃO são ISOMORFAS.")


if __name__ == "__main__":
    main()