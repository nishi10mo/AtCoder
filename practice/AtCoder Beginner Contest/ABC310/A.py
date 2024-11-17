# Order Something Else
def f(N, P, Q, D):
    price = Q + min(D)
    return min(P, price)

def main():
    N, P, Q = [int(i) for i in input().split()]
    D = [int(i) for i in input().split()]
    print(f(N, P, Q, D))

if __name__=="__main__":
    main()
