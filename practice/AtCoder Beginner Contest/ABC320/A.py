# Leyland Number
def f(A, B):
    return A**B + B**A

def main():
    A, B = [int(i) for i in input().split()]
    print(f(A, B))

if __name__=="__main__":
    main()
