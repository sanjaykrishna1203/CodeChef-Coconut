def Answer(Xa,xa,Xb,xb):
    typeA = Xa/xa
    typeB = Xb/xb
    print(int(typeA+typeB))
    

T = int(input())
while (not T == 0):
    x, y, X, Y = [int(x) for x in input().split()]
    Answer(X,x,Y,y)
    T-1
