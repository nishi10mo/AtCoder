# Extended ABC
def f(S):
    pre = "A"
    for s in S:
        if s != pre:
            if (pre=="A" and (s=="B" or s=="C")) or (pre=="B" and s=="C"):
                pre = s
            else:
                return "No"
    return "Yes"

def main():
    S = list(input())
    print(f(S))

if __name__=="__main__":
    main()
