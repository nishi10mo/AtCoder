# Round-Robin Tournament
def f(N, S):
    count = dict()
    for i in range(N):
        c = 0
        for j in range(N):
            if S[i][j] == "o":
                c += 1
        count[i+1] = c
    count = dict(sorted(count.items(), key=lambda x:x[1], reverse=True))
    return count.keys()

def main():
    N = int(input())
    S = []
    for _ in range(N):
        s = list(input())
        S.append(s)
    ans = f(N, S)
    print(*ans)

if __name__=="__main__":
    main()
