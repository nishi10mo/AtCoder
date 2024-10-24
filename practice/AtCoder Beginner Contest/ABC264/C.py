# Matrix Reducing
def f(H1, W1, A, H2, W2, B):
    for i in range(1 << H1):
        for j in range(1 << W1):
            hvec = []
            wvec = []
            for k in range(H1):
                if (i & (1 << k)) == 0:
                    hvec.append(k)
            for k in range(W1):
                if (j & (1 << k)) == 0:
                    wvec.append(k)
            if len(hvec) != H2 or len(wvec) != W2:
                continue
            flag = True
            for k in range(H2):
                for l in range(W2):
                    if A[hvec[k]][wvec[l]] != B[k][l]:
                        flag = False
                        break
                if not flag:
                    break
            if flag:
                return "Yes"
    return "No"

def main():
    H1, W1 = [int(i) for i in input().split()]
    A = []
    for _ in range(H1):
        a = [int(i) for i in input().split()]
        A.append(a)
    H2, W2 = [int(i) for i in input().split()]
    B = []
    for _ in range(H2):
        b = [int(i) for i in input().split()]
        B.append(b)
    print(f(H1, W1, A, H2, W2, B))

if __name__=="__main__":
    main()
    
