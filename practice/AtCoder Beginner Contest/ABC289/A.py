# flip
def f(s):
    results = []
    for i in s:
        if i == "0":
            results.append("1")
        else:
            results.append("0")
    return "".join(results)

def main():
    s = list(input())
    print(f(s))

if __name__ == '__main__':
    main()
