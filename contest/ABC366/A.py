# Election 2
def f(N, T, A):
    if N//2<T or N//2<A:
        return "Yes"
    return "No"
    

def main():
    N, T, A = [int(i) for i in input().split()]
    print(f(N, T, A))

if __name__=="__main__":
    main()
