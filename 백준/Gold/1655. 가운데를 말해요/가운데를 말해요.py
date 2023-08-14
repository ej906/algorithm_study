
import sys
import heapq
input=sys.stdin.readline

#가운데를 말해요

n=int(input())

left_max=[]
right_min=[]


for _ in range(n):
    num=int(input())
    if len(left_max)==len(right_min):
        heapq.heappush(left_max,-num)
    else:
        heapq.heappush(right_min,num)
    if len(right_min)!=0:
        if -(left_max[0])>right_min[0]:
            left=-heapq.heappop(left_max)
            right=-heapq.heappop(right_min)
            heapq.heappush(left_max,right)
            heapq.heappush(right_min,left)
    
    print(-left_max[0])