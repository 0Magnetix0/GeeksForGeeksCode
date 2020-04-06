import sys

n = int(sys.stdin.readline())
BellTower = [[1]*i for i in range(1,n+1)]

if __name__ == '__main__':
    for i in range(n):
        for j in range(i+1):
            if j == 0:
                BellTower[i][j] = BellTower[i-1][i-1]
            else:
                BellTower[i][j] = BellTower[i-1][j-1] + BellTower[i][j-1]

    for i in range(n):
        print(BellTower[i])
main()
# Can u do better ?
