# Airport Code
def judgeAirport(S, T):
    T = [i.lower() for i in T]
    S.append("x")
    c = 0
    for i in range(len(S)):
        if T[c]==S[i]:
            c += 1
        if c == 3:
            return "Yes"
    return "No"

def main():
    S = list(input())
    T = list(input())
    print(judgeAirport(S, T))

if __name__=="__main__":
    main()
