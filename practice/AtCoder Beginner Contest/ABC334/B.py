# Christmas Trees
def f(A, M, L, R):
    L -= A
    R -= A
    ans = R//M - (L-1)//M
    return ans

def main():
    A, M, L, R = [int(i) for i in input().split()]
    print(f(A, M, L, R))

if __name__=="__main__":
    main()
