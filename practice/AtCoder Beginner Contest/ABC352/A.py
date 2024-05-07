# AtCoder Line
def judgeStation(N, X, Y, Z):
    if X <= Y:
        sttn = [i for i in range(X, Y+1)]
        if Z in sttn:
            return "Yes"
        else:
            return "No"
    else:
        sttn = [i for i in range(X, Y-1, -1)]
        if Z in sttn:
            return "Yes"
        else:
            return "No"

def main():
    N, X, Y, Z = [int(i) for i in input().split()]
    print(judgeStation(N, X, Y, Z))

if __name__=="__main__":
    main()
