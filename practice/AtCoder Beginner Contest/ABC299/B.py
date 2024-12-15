# Trick Taking
def f(N, T, C, R):
    maxr = 0
    if T in C:
        for i in range(N):
            if C[i] == T:
                maxr = max(maxr, R[i])
                if maxr == R[i]:
                    ans = i+1
    else:
        t = C[0]
        for i in range(N):
            if C[i]  == t:
                maxr = max(maxr, R[i])
                if maxr == R[i]:
                    ans = i+1
    return ans

def main():
    N, T = [int(i) for i in input().split()]
    C = [int(i) for i in input().split()]
    R = [int(i) for i in input().split()]
    print(f(N, T, C, R))

if __name__ == '__main__':
    main()
