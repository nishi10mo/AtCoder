# A^A
def f(B):
    for i in range(1, 16):
        if i**i == B:
            return i
    return -1

def main():
    B = int(input())
    print(f(B))

if __name__=="__main__":
    main()
