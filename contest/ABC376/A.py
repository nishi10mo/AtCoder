# Candy Button
def f(N, C, T):
    pre = T[0]
    ans = 1
    for t in T:
        if t - pre >= C:
            ans += 1
            pre = t
    return ans

def main():
    N, C = [int(i) for i in input().split()]
    T = [int(i) for i in input().split()]
    print(f(N, C, T))

if __name__=="__main__":
    main()
