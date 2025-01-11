# Qual B
def f(N, K, S):
    k = 0
    results = []
    for i in range(N):
        if k == K:
            results.append("x")
        else:
            if S[i] == "o":
                k += 1
                results.append("o")
            else:
                results.append("x")
    return "".join(results)

def main():
    N, K = [int(i) for i in input().split()]
    S = list(input())
    print(f(N, K, S))

if __name__ == "__main__":
    main()
