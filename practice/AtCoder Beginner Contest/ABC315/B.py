# The Middle Day
def f(N, D):
    total = sum(D)
    half = (total + 1)//2
    ans = []
    cum = 0
    for i in range(N):
        cum += D[i]
        if cum >= half:
            ans.append(i+1)
            cum -= D[i]
            day = half - cum
            ans.append(day)
            return ans

def main():
    N = int(input())
    D = [int(i) for i in input().split()]
    ans = f(N, D)
    print(*ans)

if __name__=="__main__":
    main()
