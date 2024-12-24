# Bombs
def f(R, C, B):
    def bomb(i, j, impact):
        for x in range(1, impact+1):
            for y in range(1, impact+1):
                if i - b >= 0:
                    B[i-b][j] = "."
                if 

def main():
    R, C = [int(i) for i in input().split()]
    B = []
    for _ in range(R):
        B.append(list(input()))
