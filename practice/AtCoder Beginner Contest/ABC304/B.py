# Subscribers
def f(N):
    def ceil_n(v, n):
        factor = 10**n
        return (v//factor)*factor
    c = 0
    n = N
    while n >= 10:
        n = n//10
        c += 1
    if c < 3:
        return N
    else:
        return ceil_n(N, c-2)

def main():
    N = int(input())
    print(f(N))

if __name__=="__main__":
    main()

