# Buy One Carton of Milk
def f(N, S, M, L):
    ans = 10**18
    for s in range(101):
        for m in range(101):
            for l in range(101):
                if 6*s + 8*m + 12*l >= N:
                    total = s*S + m*M + l*L
                    ans = min(ans, total)
    return ans

def main():
    N, S, M, L = [int(i) for i in input().split()]
    print(f(N, S, M, L))

if __name__=="__main__":
    main()
