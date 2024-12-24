# Probably English
def f(N, W):
    candidates = ["and", "not", "that", "the", "you"]
    for w in W:
        if w in candidates:
            return "Yes"
    return "No"

def main():
    N = int(input())
    W = list(input().split())
    print(f(N, W))

if __name__ == '__main__':
    main()
