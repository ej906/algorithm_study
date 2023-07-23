import sys
input=sys.stdin.readline

chess_n=[1,1,2,2,2,8]
chess=list(map(int,input().split()))

for i in range(len(chess)):
    print(chess_n[i]-chess[i],end=' ')