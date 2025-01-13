# Humidifier 3
from collections import deque

def f(H, W, D, S):
    visited = [[False]*W for _ in range(H)]
    que = deque()
    for h in range(H):
        for w in range(W):
            if S[h][w] == "H":
                que.append((h, w, 0))
                visited[h][w] = True
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while que:
        x, y, d = que.popleft()
        if d >= D:
            continue
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= H or ny < 0 or ny >= W:
                continue
            if S[nx][ny] == "#" or visited[nx][ny]:
                continue
            que.append((nx, ny, d+1))
            visited[nx][ny] = True
    
    ans = 0
    for h in range(H):
        for w in range(W):
            if visited[h][w]:
                ans += 1

    return ans

def main():
    H, W, D = [int(i) for i in input().split()]
    S = []
    for _ in range(H):
        S.append(list(input()))
    print(f(H, W, D, S))

if __name__ == '__main__':
    main()
