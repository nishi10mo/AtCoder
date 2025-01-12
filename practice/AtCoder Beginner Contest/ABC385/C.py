# Illuminate Buildings
def f(N, H):
    ans = 1
    for i in range(N):
        for j in range(1, N):
            tmp = 1
            k = 1
            while i + j*k < N:
                if H[i] == H[i + j*k]:
                    tmp += 1
                    k += 1
                else:
                    break
            ans = max(ans, tmp)
    return ans

def main():
    N = int(input())
    H = [int(i) for i in input().split()]  
    print(f(N, H))

if __name__ == '__main__':
    main()
