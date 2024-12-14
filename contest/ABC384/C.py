# Perfect Standings
from itertools import combinations

def f(a, b, c, d, e):
    scores = {"A": a, "B": b, "C": c, "D": d, "E": e}
    candidates = ["A", "B", "C", "D", "E"]
    participants = []
    for i in range(1, 6):
        for comb in combinations(candidates, i):
            participants.append("".join(comb))
    participants_scores = {}
    for participant in participants:
        score = 0
        for p in participant:
            score += scores[p]
        participants_scores[participant] = score
    participants_scores = sorted(participants_scores.items(), key=lambda x: (x[1], len(x[0])), reverse=True)
    results = []
    for i in participants_scores:
        results.append(i[0])
    return results

def main():
    a, b, c, d, e = [int(i) for i in input().split()]
    results = f(a, b, c, d, e)
    for ans in results:
        print(ans)

if __name__ == '__main__':
    main()
