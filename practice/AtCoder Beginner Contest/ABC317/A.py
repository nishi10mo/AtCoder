# Potions 
def f(N, H, X, P):
    for i in range(N):
        if H + P[i] >= X:
            return i+1

def main():
    N, H, X = [int(i) for i in input().split()]
    P = [int(i) for i in input().split()]
    print(f(N, H, X, P))

if __name__=="__main__":
    main()
