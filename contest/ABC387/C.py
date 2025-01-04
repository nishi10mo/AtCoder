# Snake Numbers
import pdb
def f(l_or, r_or):
    # pdb.set_trace()
    ans = 0
    l_n = len(str(l_or))
    r_n = len(str(r_or))
    if l_n == r_n == 2:
        r = [int(x) for x in list(str(r_or))]
        tmp = sum([x for x in range(1, r[0])])
        if r[0] > r[1]:
            tmp += r_or - 10*r[0] + 1
        else:
            tmp += r[1] + 1
        ans += tmp
        return ans
    for n in range(l_n, r_n+1):
        if n == l_n:
            tmp = sum([x**(n-1) for x in range(1, 10)])
            l = l_or - 1
            if len(str(l)) != n:
                ans += tmp
                continue
            min_l = 10**(n-1)
            ans += tmp - f(min_l, l)
            print("n==l_n ans", ans)
            # l = [int(x) for x in list(str(l))]
            # max_num = l[0]
            # tmp_ = sum([x**(n-1) for x in range(1, max_num)])
            # for j in range(1, n):
            #     if l[j] < max_num:
            #         product *= (l[j] + 1)
            #     else:
            #         product *= max_num
            # tmp -= product
            # ans += tmp
        elif n == r_n:
            ans += f(10**(n-1), r_or)
            print("n==r_n ans", ans)
            # r = [int(x) for x in list(str(R))]
            # max_num = r[0]
            # product = r[0]
            # for j in range(1, n):
            #     if r[j] < max_num:
            #         product *= (r[j] + 1)
            #     else:
            #         product *= max_num
            # ans += product
        else:
            ans += sum([x**(n-1) for x in range(1, 10)])
    return ans

def main():
    L, R = [int(i) for i in input().split()]
    print(f(L, R))

if __name__ == '__main__':
    main()

