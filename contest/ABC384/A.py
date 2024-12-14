# aaaadaa
def f(N, c1, c2, S):
    for i in range(N):
        if S[i] != c1:
            S[i] = c2
    return S

def main():
    N, c1, c2 = input().split()
    N = int(N)
    S = list(input())
    results = f(N, c1, c2, S)
    print("".join(results))

if __name__ == '__main__':
    main()
