# Dentist Aoki
def main():
    N, Q = map(int, input().split())
    T = list(map(int, list(input().split())))
    teeth = list(range(1, N+1))
    for i in range(Q):
        if T[i] in teeth:
            teeth.remove(T[i])
        else:
            teeth.append(T[i])
    print(len(teeth))

if __name__=="__main__":
    main()

