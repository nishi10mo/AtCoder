# Same Map in the RPG World
import copy
from itertools import permutations
def f(H, W, A, B):
    def vertical_shift(graph):
        graph.append(graph[0])
        del graph[0]
        return graph
    def horizontal_shift(graph):
        n = len(graph)
        for i in range(n):
            graph[i].append(graph[i][0])
            del graph[i][0]
        return graph
    for s in range(H):
        for t in range(W):
            graph = copy.deepcopy(A)
            for _ in range(s):
                graph = vertical_shift(graph)
            for _ in range(t):
                graph = horizontal_shift(graph)
            if graph == B:
                return "Yes"
    return "No"

def main():
    H, W = [int(i) for i in input().split()]
    A = []
    for _ in range(H):
        a = list(input())
        A.append(a)
    B = []
    for _ in range(H):
        b = list(input())
        B.append(b)
    print(f(H, W, A, B))

if __name__=="__main__":
    main()
