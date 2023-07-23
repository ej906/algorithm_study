import sys
input=sys.stdin.readline

a,b= input().split()
a=a[::-1]
b=b[::-1]

a=int(''.join(a))
b=int(''.join(b))

print(max(a,b))
