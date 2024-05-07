# Airport Code
def judgeAirport(S, T):
    if T[0].lower() in S and T[1].lower() in S:
        first = S.index(T[0].lower())
        second = S.index(T[1].lower())
        if T[2].lower() in S:
            third = S.index(T[2].lower())
            if first < second < third:
                return "Yes"
            else:
                return "No"
        elif first < second and T[2]=="X":
            return "Yes"
        else:
            return "No"
    else:
        return "No"

def main():
    S = list(input())
    T = list(input())
    print(judgeAirport(S, T))

if __name__=="__main__":
    main()
