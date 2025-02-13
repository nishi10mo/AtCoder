# Yellow and Red Card
def f(N, Q, event):
    scores = [0]*N
    results = []
    for i in range(Q):
        if event[i][0] == 1:
            scores[event[i][1]-1] += 1
        elif event[i][0] == 2:
            scores[event[i][1]-1] += 2
        else:
            if scores[event[i][1]-1] >= 2:
                results.append("Yes")
            else:
                results.append("No")
    return results

def main():
    N, Q = [int(i) for i in input().split()]
    event = []
    for _ in range(Q):
        event.append([int(i) for i in input().split()])
    results = f(N, Q, event)
    for ans in results:
        print(ans)

if __name__ == '__main__':
    main()
