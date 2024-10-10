# Weak Beats
def f(S):
    for i in range(8):
        if S[2*i+1] == 1:
            return "No"
    return "Yes"

def main():
    S = [int(i) for i in list(input())]
    print(f(S))

if __name__=="__main__":
    main()
