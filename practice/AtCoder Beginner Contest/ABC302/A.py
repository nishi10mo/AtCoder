# Attack 
def f(A, B):
    if A%B == 0:
        return A//B
    else:
        return A//B + 1

def main():
    A, B = [int(i) for i in input().split()]
    print(f(A, B))

if __name__=="__main__":
    main()
