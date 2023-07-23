import sys
input=sys.stdin.readline

n=input().strip()

num_list=list(n)

num_list.sort(reverse=True)
str=''
for i in num_list:
    str+=i

print(str)