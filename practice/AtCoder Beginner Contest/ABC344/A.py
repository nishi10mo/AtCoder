# Spoiler
def calc(S):
    ans = []
    flag = 0
    for s in S:
        if flag==0:
            if s != "|":
                ans.append(s)
            else:
                flag += 1
        elif flag == 1:
            if s != "|":
                continue
            else:
                flag += 1
        else:
            ans.append(s)
    return "".join(ans)

def main():
    S = list(input())
    print(calc(S))

if __name__=="__main__":
    main()
