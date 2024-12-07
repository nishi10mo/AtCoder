# Humidifier 3
def f(H, W, D, S):
    place = set()
    for h in range(H):
        for w in range(W):
            if S[h][w] =="H":
                place.add((h, w))
    ans = 0
    for h in range(H):
        for w in range(W):
            if S[h][w] == ".":
                for p in place:
                    dis = abs(h - p[0]) + abs(w - p[1])
                    if dis <= D:
                        ans += 1
                        break
    ans += len(place)
    return ans

def main():
    H, W, D = [int(i) for i in input().split()]
    S = []
    for _ in range(H):
        s = list(input())
        S.append(s)
    print(f(H, W, D, S))

if __name__=="__main__":
    main()
