# Coloring Matrix
import copy

def f(N, A, B):
    def rotate(x, n):
        result = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                result[i][j] = x[n-1-j][i]
        return result
    def check(a, b):
        for i in range(N):
            for j in range(N):
                if a[i][j] == 1 and b[i][j] == 0:
                    return False
        return True
    if check(A, B):
        return "Yes"
    a = copy.deepcopy(A)
    a = rotate(a, N)
    while a != A:
        if check(a, B):
            return "Yes"
        a = rotate(a, N)
    return "No"
  
def main():
    N = int(input())
    A = []
    for _ in range(N):
        a = [int(i) for i in input().split()]
        A.append(a)
    B = []
    for _ in range(N):
        b = [int(i) for i in input().split()]
        B.append(b)
    print(f(N, A, B))

if __name__ == '__main__':
    main()
