#가위바위보

import sys
input=sys.stdin.readline

r=int(input())
sangeun=list(map(str,input().strip()))
n=int(input())
friend=[]
for _ in range(n):
    friend.append(list(map(str,input().strip())))

score=0

for i in range(r):
    if sangeun[i]=='S':
        win='P'
    elif sangeun[i]=='P':
        win='R'
    elif sangeun[i]=='R':
        win='S'
    else:
        pass

    for j in range(n):
        if friend[j][i]==win:
            score+=2
        elif friend[j][i]==sangeun[i]:
            score+=1
        else:
            pass

print(score)

max_score=0

for i in range(r):
    count_list=[0,0,0]
    for j in range(n):
        if friend[j][i]=='R':
            count_list[0]+=1
        elif friend[j][i]=='S':
            count_list[1]+=1
        else:
            count_list[2]+=1
    score_list=[0,0,0]
    score_list[0] += (count_list[1]*2+count_list[0])
    score_list[1] += (count_list[2]*2+count_list[1])
    score_list[2] += (count_list[0]*2+count_list[2])
    max_score+=max(score_list)

print(max_score)