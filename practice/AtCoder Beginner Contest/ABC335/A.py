# 202<s>3</s>
def f(S):
    S[-1] = "4"
    return "".join(S)

def main():
    S = list(input())
    print(f(S))

if __name__=="__main__":
    main()
