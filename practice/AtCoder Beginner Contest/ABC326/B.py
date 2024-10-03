# 326-like Numbers
def f(N):
    n = N
    while True:
        n_list = [int(i) for i in list(str(n))]
        if n_list[0]*n_list[1] == n_list[2]:
            return n
        n += 1

def main():
    N = int(input())
    print(f(N))

if __name__=="__main__":
    main()
