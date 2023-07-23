import sys
input=sys.stdin.readline
alpha_list=[0]*26

word=input().strip()
word=word.upper()

for i in word:
    alpha_list[ord(i)-65]+=1

max=max(alpha_list)
cnt=0

for i in range(len(alpha_list)):
    if max==alpha_list[i]:
        cnt+=1
        alpha=chr(i+65)

if cnt>1:
    print('?')
else:
    print(alpha)