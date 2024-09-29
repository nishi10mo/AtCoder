# 11/11
def f(N, D):
    ans = 0
    for i in range(1, N+1):
        if i < 10:
            if 10*i + i <= D[i-1]:
                ans += 2
            elif i <= D[i-1] < 10*i + i:
                ans += 1
        else:
            if i//10 == i%10:
                if i <= D[i-1]:
                    ans += 2
                elif i//10 <= D[i-1] < i:
                    ans += 1
    return ans

def main():
    N = int(input())
    D = [int(i) for i in input().split()]
    print(f(N, D))

if __name__=="__main__":
    main()
