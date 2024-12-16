# Treasure Chest
def f(N, S):
    flag = False
    for s in S:
        if s == "|":
            if flag == False:
                flag = True
            else:
                flag = False
        if s == "*":
            if flag == True:
                return "in"
            else:
                return "out"

def main():
    N = int(input())
    S = list(input())
    print(f(N, S))

if __name__ == '__main__':
    main()
