# Buildings
def searchBuild(N, H):
    if N == 1:
        return -1
    for i in range(1, N):
        if H[i] > H[0]:
            return i + 1
        if i == N-1:
            return -1

def main():
    N = int(input())
    H = [int(i) for i in input().split()]
    print(searchBuild(N, H))

if __name__=="__main__":
    main()
