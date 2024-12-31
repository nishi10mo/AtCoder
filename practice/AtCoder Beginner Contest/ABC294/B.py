# ASCII Art
def f(H, W, A):
    S = []
    for i in range(H):
        s = []
        for j in range(W):
            if A[i][j] == 0:
                s.append(".")
            else:
                s.append(chr(A[i][j] + 64))
        S.append("".join(s))
    return S

def main():
    H, W = [int(i) for i in input().split()]
    A = []
    for _ in range(H):
        A.append([int(i) for i in input().split()])
    S = f(H, W, A)
    for s in S:
        print(s)

if __name__ == '__main__':
    main()
