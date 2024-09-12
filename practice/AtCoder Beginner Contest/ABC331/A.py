# Tomorrow 
def f(M, D, y, m, d):
    d += 1
    if d > D:
        d = 1
        m += 1
        if m > M:
            m = 1
            y += 1
    return [y, m, d]

def main():
    M, D = [int(i) for i in input().split()]
    y, m, d = [int(i) for i in input().split()]
    print(*f(M, D, y, m, d))

if __name__=="__main__":
    main()
