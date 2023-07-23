import sys
input=sys.stdin.readline

n=int(input())
word=[]

for i in range(n):
    word.append(input().strip())

set_list=set(word) #set을 통해 중복제거
word=list(set_list) #다시 list로 변환

word.sort()
word.sort(key=lambda x:len(x))

for i in range(len(word)):
    print(word[i])
