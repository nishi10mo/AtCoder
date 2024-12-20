# Double Click
def f(N, D, T):
    for i in range(N-1):
        duration = T[i+1] - T[i]
        if duration <= D:
            return T[i+1]
    return -1

def main():
    N, D = [int(i) for i in input().split()]
    T = [int(i) for i in input().split()]
    print(f(N, D, T))

if __name__ == '__main__':
    main()
