import sys
input=sys.stdin.readline

sentence=list(map(str,input().strip()))

UCPC=['U','C','P','C']
index=0
for i in sentence:
    if i == UCPC[index]:
        index+=1
    if index==4:
        print("I love UCPC")
        break
else:
    print("I hate UCPC")
    