# Max Even
def f(N, A):
    A = sorted(A, reverse=True)
    c1 = 0
    cand1 = 0
    for a in A:
        if c1 == 2:
            break
        if a % 2 == 0:
            c1 += 1
            cand1 += a
    c2 = 0
    cand2 = 0
    for a in A:
        if c2 == 2:
            break
        if a % 2 == 1:
            c2 += 1
            cand2 += a
    if c1 < 2 and c2 < 2:
        return -1
    return max(cand1, cand2)

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    print(f(N, A))

if __name__=="__main__":
    main()
