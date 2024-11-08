# To Be Saikyo
def f(N, P):
    now = P[0]
    maxp = max(P)
    if now == maxp:
        if P.count(maxp) > 1:
            return 1
        else:
            return 0
    else:
        return maxp - now + 1

def main():
    N = int(input())
    P = [int(i) for i in input().split()]
    print(f(N, P))

if __name__=="__main__":
    main()
