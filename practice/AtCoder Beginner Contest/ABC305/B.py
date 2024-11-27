#   ABCDEFG
def f(p, q):
    graph = {
        "A": 0,
        "B": 1,
        "C": 2,
        "D": 3,
        "E": 4,
        "F": 5,
        "G": 6
    }
    distance = [3, 1, 4, 1, 5, 9]
    start = graph[p]
    end = graph[q]
    if start > end:
        start, end = end, start
    ans = 0
    for i in range(start, end):
        ans += distance[i]
    return ans

def main():
    p, q = input().split()
    print(f(p, q))

if __name__=="__main__":
    main()
