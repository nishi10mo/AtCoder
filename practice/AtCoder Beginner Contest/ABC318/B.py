# Overlapping sheets
def f(ABCD):
    graph = [[False]*100 for _ in range(100)]
    for abcd in ABCD:
        for x in range(abcd[0], abcd[1]):
            for y in range(abcd[2], abcd[3]):
                graph[x][y] = True
    c = 0
    for i in graph:
        c += i.count(True)
    return c

def main():
    N = int(input())
    ABCD = []
    for _ in range(N):
        abcd = [int(i) for i in input().split()]
        ABCD.append(abcd)
    print(f(ABCD))

if __name__=="__main__":
    main()
    
