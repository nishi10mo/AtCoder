    # FF
    def f(N, Q, TAB):
        follows = set()
        ans = []
        for tab in TAB:
            if tab[0] == 1:
                follows.add((tab[1], tab[2]))
            elif tab[0] == 2:
                follows.discard((tab[1], tab[2]))
            else:
                if ((tab[1], tab[2]) in follows) and ((tab[2], tab[1]) in follows):
                    ans.append("Yes")
                else:
                    ans.append("No")
        return ans

    def main():
        N, Q = [int(i) for i in input().split()]
        TAB = []
        for _ in range(Q):
            tab = [int(i) for i in input().split()]
            TAB.append(tab)
        result = f(N, Q, TAB)
        for ans in result:
            print(ans)

    if __name__=="__main__":
        main()
