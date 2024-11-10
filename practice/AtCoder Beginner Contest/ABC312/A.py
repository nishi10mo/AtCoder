# Chord
def f(S):
    if S in ["ACE","BDF", "CEG", "DFA", "EGB", "FAC", "GBD"]:
        return "Yes"
    else:
        return "No"

def main():
    S = input()
    print(f(S))

if __name__=="__main__":
    main()
