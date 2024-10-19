# Hands on Ring (Easy)
def f(N, Q, HT):
    l = 1
    r = 2
    ans = 0
    for ht in HT:
        if ht[0] == "R":
            if r < l < ht[1]:
                ans += N - (ht[1] - r)
            elif r < ht[1] < l:
                ans += ht[1] - r
            elif l < r < ht[1]:
                ans += ht[1] - r
            elif l < ht[1] < r:
                ans += r - ht[1]
            elif ht[1] < r < l:
                ans += r - ht[1]
            elif ht[1] < l < r:
                ans += N - (r - ht[1])
            r = ht[1]
        if ht[0] == "L":
            if l < r < ht[1]:
                ans += N - (ht[1] - l)
            elif l < ht[1] < r:
                ans += ht[1] - l
            elif r < l < ht[1]:
                ans += ht[1] - l
            elif r < ht[1] < l:
                ans += l - ht[1]
            elif ht[1] < l < r:
                ans += l - ht[1]
            elif ht[1] < r < l:
                ans += N - (l - ht[1])
            l = ht[1]
    return ans

def main():
    N, Q = [int(i) for i in input().split()]
    HT = []
    for _ in range(Q):
        ht = list(input().split())
        ht[1] = int(ht[1])
        HT.append(ht)
    print(f(N, Q, HT))

if __name__=="__main__":
    main()
