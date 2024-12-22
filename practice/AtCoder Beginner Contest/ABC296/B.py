# Chessboard
def f(S):
    columns = ["a", "b", "c", "d", "e", "f", "g", "h"]
    rows = ["8", "7", "6", "5", "4", "3", "2", "1"]
    for i in range(8):
        for j in range(8):
            if S[i][j] == "*":
                return columns[j] + rows[i]

def main():
    S = []
    for _ in range(8):
        S.append(list(input()))
    print(f(S))

if __name__ == '__main__':
    main()
