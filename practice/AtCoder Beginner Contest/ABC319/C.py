# False Hope
from itertools import permutations
def f(cells):
    bottom = 1
    for i in range(2, 10):
        bottom *= i
    top = bottom
    lines = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]
    order = [i for i in range(9)]
    for perm in permutations(order):
        for a, b, c in lines:
            if cells[a]==cells[b] and cells[b]!= cells[c] and perm[a] < perm[c] and perm[b] < perm[c]:
                top -= 1
                break
            elif cells[a]==cells[c] and cells[c]!=cells[b] and perm[a] < perm[b] and perm[c] < perm[b]:
                top -= 1
                break
            elif cells[b]==cells[c] and cells[c]!=cells[a] and perm[b] < perm[a] and perm[c] < perm[a]:
                top -= 1
                break
    return top/bottom

def main():
    cells = []
    for _ in range(3):
        c1, c2, c3 = [int(i) for i in input().split()]
        cells.append(c1)
        cells.append(c2)
        cells.append(c3)
    print(f(cells))

if __name__=="__main__":
    main()
