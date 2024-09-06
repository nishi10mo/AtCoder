# Pentagon
def f(S, T):
    length_dict = {
        "AB": 1,
        "BC": 1,
        "CD": 1,
        "DE": 1,
        "AE": 1,
        "AC": 2,
        "AD": 2,
        "BD": 2,
        "BE": 2,
        "CE": 2
    }
    S = sorted(S)
    S = "".join(S)
    T = sorted(T)
    T = "".join(T)
    if length_dict[S]==length_dict[T]:
        return "Yes"
    else:
        return "No"

def main():
    S = input()
    T = input()
    print(f(S, T))

if __name__=="__main__":
    main()
