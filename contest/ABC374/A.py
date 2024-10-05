# Takahashi san 2
def f(S):
    if S[-3]=="s" and S[-2]=="a" and S[-1]=="n":
        return "Yes"
    return "No"

def main():
    S = list(input())
    print(f(S))

if __name__=="__main__":
    main()
