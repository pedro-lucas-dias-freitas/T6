# Trabalho Prático 6 - Isomorfismo em Árvores

**Disciplina:** Resolução de Problemas com Grafos  
**Orientador:** Prof. Me Ricardo Carubbi  
**Grupo:** A  
**Alunos do grupo:**
* Pedro Lucas Dias Freitas (2320480)
* Elísio Soares Raulino Filho (2315449)
* Lucas Gabriel Bezerra Pinto Brigagão (2410386)

---

## 🎥 Vídeo Explicativo
[**CLIQUE AQUI PARA ASSISTIR AO VÍDEO EXPLICATIVO**](COLOQUE_O_LINK_AQUI)

---

## 📌 Sobre o Projeto
Este projeto implementa a verificação de isomorfismo entre duas árvores não direcionadas. A solução não utiliza abordagens heurísticas ou comparações visuais, mas sim o método estrutural correto: a **codificação canônica** de árvores. 

O programa encontra o(s) centro(s) da árvore, realiza o enraizamento, gera os códigos recursivamente ordenando os filhos de forma lexicográfica e, por fim, compara as strings resultantes para emitir o veredito.

## 🚀 Como executar

O programa foi desenvolvido em **Python** e não utiliza bibliotecas externas. Para executá-lo, utilize a linha de comando passando o caminho dos dois arquivos de texto que contêm as árvores no formato `algs4`.

**Comando de execução:**
```bash
python src/main.py dados/arquivo1.txt dados/arquivo2.txt