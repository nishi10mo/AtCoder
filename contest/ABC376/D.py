# Cycle
def f(N, M, graph):
    def distance(start, end):
        if graph[start][end]:
            return 1
        dis = False
        for i in range(N):
            if graph[start][i]:
                if distance(i, end) != False:
                    if dis != False:
                        dis = min(dis, distance(i, end)) + 1
                    else:
                        dis = distance(i, end) + 1
                else:
                    dis = False
        return dis
    dis = distance(0, 0)
    if dis == False:
        return -1
    return dis

def main():
    N, M = [int(i) for i in input().split()]
    graph = [[False]*N for _ in range(N)]
    for _ in range(M):
        a, b = [int(i)-1 for i in input().split()]
        graph[a][b] = True
    print(f(N, M, graph))

if __name__=="__main__":
    main()
