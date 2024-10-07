# Same
def f(N, A):
    for i in range(N-1):
        if A[i] != A[i+1]:
            return "No"
    return "Yes"

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    print(f(N, A))

if __name__=="__main__":
    main()
