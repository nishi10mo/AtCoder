# 9x9 Sum
def f(X):
    ans = 0
    for i in range(1, 10):
        for j in range(1, 10):
            if i * j == X:
                continue
            else:
                ans += i * j
    return ans

def main():
    X = int(input())
    print(f(X))

if __name__ == '__main__':
    main()
