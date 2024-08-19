import sys
input = sys.stdin.readline

n = int(input())

star = [[" "]*2*n for _ in range(n)]

def sol(i,j,n):
    if n == 3:
        star[i][j] = "*"
        star[i+1][j-1] = "*"
        star[i+1][j+1] = "*"
        for k in range(-2,3):
            star[i+2][j-k] = "*"
    else:
        n //= 2
        sol(i,j,n)
        sol(i+n,j-n,n)
        sol(i+n,j+n,n)

sol(0,n-1,n)

for s in star:
    print("".join(s))