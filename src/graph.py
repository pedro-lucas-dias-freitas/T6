class Graph:
    def __init__(self, V_or_filename):
        """
        Construtor que aceita o número de vértices (int) ou o caminho
        para um arquivo de texto no formato Algs4 (str).
        """
        if isinstance(V_or_filename, int):
            self._V = V_or_filename
            self._E = 0
            self._adj = [[] for _ in range(self._V)]
        elif isinstance(V_or_filename, str):
            self._read_from_file(V_or_filename)
        else:
            raise ValueError("Argumento deve ser um inteiro (V) ou uma string (nome do arquivo).")

    def _read_from_file(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
            # Limpa linhas vazias e espaços em branco
            lines = [line.strip() for line in lines if line.strip()]
            
            self._V = int(lines[0])
            self._E = 0
            self._adj = [[] for _ in range(self._V)]
            
            E_expected = int(lines[1])
            for i in range(2, 2 + E_expected):
                if i < len(lines):
                    parts = lines[i].split()
                    v = int(parts[0])
                    w = int(parts[1])
                    self.add_edge(v, w)

    def V(self):
        return self._V

    def E(self):
        return self._E

    def add_edge(self, v, w):
        self._adj[v].append(w)
        self._adj[w].append(v)
        self._E += 1

    def adj(self, v):
        return self._adj[v]

    def to_string(self):
        result = [f"{self._V} vertices, {self._E} arestas"]
        for v in range(self._V):
            adj_str = " ".join(map(str, self._adj[v]))
            result.append(f"{v}: {adj_str}")
        return "\n".join(result)