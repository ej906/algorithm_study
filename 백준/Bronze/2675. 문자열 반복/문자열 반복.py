import sys
input=sys.stdin.readline

t=int(input())

for i in range(t):
    r,s=input().split()
    r=int(r)
    word=''
    for j in s:
        word+=r*j
    print(word)
        