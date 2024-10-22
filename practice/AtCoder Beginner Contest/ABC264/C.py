# Matrix Reducing
def f(H1, W1, A, H2, W2, B):
    

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
    
