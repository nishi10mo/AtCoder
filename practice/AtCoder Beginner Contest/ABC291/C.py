# LRUD Instructions 2
def f(N, S):
    history = set()
    x = 0
    y = 0
    history.add((x, y))
    for s in S:
        if s=="R":
            x += 1
        elif s=="L":
            x -= 1
        elif s=="U":
            y += 1
        elif s=="D":
            y -= 1
        if (x, y) in history:
            return "Yes"
        history.add((x, y))
    return "No"

def main():
    N = int(input())
    S = list(input())
    print(f(N, S))

if __name__=="__main__":
    main()
