# Glass and Mug
def f(K, G, M):
    glass = 0
    mug = 0
    k = 0
    while k < K:
        if glass == G:
            glass = 0
        elif mug == 0:
            mug = M
        else:
            if G >= (glass + mug):
                glass += mug
                mug = 0
            else:
                mug -= (G - glass)
                glass = G
        k += 1
    return glass, mug

def main():
    K, G, M = [int(i) for i in input().split()]
    print(*f(K, G, M))

if __name__=="__main__":
    main()

