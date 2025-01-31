# Majority
def f(N, S):
    agree = S.count("For")
    if agree > N // 2:
        return "Yes"
    return "No"

def main():
    N = int(input())
    S = []
    for _ in range(N):
        S.append(input())
    print(f(N, S))

if __name__ == '__main__':
    main()

