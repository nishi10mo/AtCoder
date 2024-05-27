# AtCoder Magics
class Card:
    def __init__(self, a, c, i):
        self.a = a
        self.c = c
        self.i = i

def calc(N, cards):
    cards = sorted(cards, key=lambda card: card.c)
    ans = []
    v = 0
    for i in range(N):
        if v < cards[i].a:
            ans.append(cards[i].i)
            v = cards[i].a
    ans = sorted(ans)
    return len(ans), ans        

def main():
    N = int(input())
    cards = []
    for i in range(1, N+1):
        a, c = [int(i) for i in input().split()]
        card = Card(a, c, i)
        cards.append(card)
    m, index = calc(N, cards)
    index = [str(i) for i in index]
    print(m)
    print(" ".join(index))

if __name__=="__main__":
    main()
    