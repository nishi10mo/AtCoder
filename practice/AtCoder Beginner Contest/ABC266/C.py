# Convex Quadrilateral
def f(A, B, C, D):
    def Check_CrossProduct(a, o, b):
        cross_product = (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
        if cross_product > 0:
            return True
        else:
            return False
    
    if Check_CrossProduct(B, A, D) and Check_CrossProduct(C, B, A) and Check_CrossProduct(D, C, B) and Check_CrossProduct(A, D, C):
        return "Yes"
    else:
        return "No"

def main():
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    C = [int(i) for i in input().split()]
    D = [int(i) for i in input().split()]
    print(f(A, B, C, D))

if __name__=="__main__":
    main()
