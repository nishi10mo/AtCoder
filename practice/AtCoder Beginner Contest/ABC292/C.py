# Four Variables
def count_divisors(x):
    count = 0
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            count += 1
            if i != x // i:
                count += 1
    return count

def f(N):
    ans = 0
    for i in range(1, N):
        x = i
        y = N - i
        ans += count_divisors(x)*count_divisors(y)
    return ans

def main():
    N = int(input())
    print(f(N))

if __name__=="__main__":
    main()
