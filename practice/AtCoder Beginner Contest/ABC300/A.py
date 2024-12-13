# N-choice question
def f(N, A, B, C):
    total = A + B
    for i in range(N):
        if C[i] == total:
            return i+1

def main():
    N, A, B = [int(i) for i in input().split()]
    C = [int(i) for i in input().split()]
    print(f(N, A, B, C))

if __name__ == '__main__':
    main()
    
