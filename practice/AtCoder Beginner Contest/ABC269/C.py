# Submask
def f(N):
    ans = []
    i = N
    while True:
        ans.append(i)
        if i == 0:
            break
        i = (i-1) & N
    return ans[::-1]

def main():
    N = int(input())
    for ans in f(N):
        print(ans)

if __name__ == '__main__':
    main()
