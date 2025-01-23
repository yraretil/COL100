import math as m
def ed(a1, a2, a3, b1, b2, b3):
    ans = (round(m.sqrt((a1-b1)*(a1-b1)+(a2-b2)*(a2-b2)+(a3-b3)*(a3-b3)),2))
    print(f'{ans:.2f}')
v1 = str(input()).split()
v2 = str(input()).split()
ed(int(v1[0]),int(v1[1]),int(v1[2]),int(v2[0]),int(v2[1]),int(v2[2]))
