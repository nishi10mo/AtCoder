# Convex Quadrilateral
import numpy as np
import math
def f(A, B, C, D):
    vector = [[] for _ in range(4)]
    vector[0].append(B - A)
    vector[0].append(D - A)
    vector[1].append(A - B)
    vector[1].append(D - A)
    vector[2].append(B - C)
    vector[2].append(D - C)
    vector[3].append(C - D)
    vector[3].append(A - D)
    angles = []
    for i in range(4):
        inner_product = vector[i][0] @ vector[i][1]
        product = sum(vector[i][0]) * sum(vector[i][1])
        print(f"cos: {inner_product/product}")
        print(f"acos: {math.acos(inner_product/product)}")
        degree = math.degrees(math.acos(inner_product / product))
        print(f"degree: {degree}")
        angles.append(degree)
    print(angles)
    if sum(angles) == 360:
        return "Yes"
    return "No"

def main():
    A = np.array([int(i) for i in input().split()])
    B = np.array([int(i) for i in input().split()])
    C = np.array([int(i) for i in input().split()])
    D = np.array([int(i) for i in input().split()])
    print(f(A, B, C, D))

if __name__=="__main__":
    main()
