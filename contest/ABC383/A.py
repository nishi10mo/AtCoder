# Humidifier 1
def f(N, T, V):
    ans = 0
    index = 0
    for i in range(1, T[-1]+1):
        if i == T[index]:
            ans += V[index]
            index += 1
        if ans != 0 and i != T[-1]:
            ans -= 1
    return ans

def main():
    N = int(input())
    T = []
    V = []
    for _ in range(N):
        t, v = [int(i) for i in input().split()]
        T.append(t)
        V.append(v)
    print(f(N, T, V))

if __name__=="__main__":
    main()
