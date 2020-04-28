#!/usr/bin/python2.7
count = 0
def tileProblem(n,x):
    global count
    if n == 2:
        print("Place the tile at the center of {0}".format(x))
        count += 1
        return ;
    print("Place the tile at the center of {0}".format(x))
    count += 1
    a = x + "1"
    tileProblem(n//2,a)
    b = x + "2"
    tileProblem(n//2,b)
    c = x + "3"
    tileProblem(n//2,c)
    d = x + "4"
    tileProblem(n//2,d)

n = int(input())
tileProblem(n,'t ')
print("no of tiles to be placed {0}.".format(count))


