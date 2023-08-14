
import sys
import heapq
input=sys.stdin.readline

#절댓값 힙

n=int(input())

pq=[]

for _ in range(n):
    x=int(input())
    if x==0:
        try:
            print(heapq.heappop(pq)[1])
        except:
            print(0)
    else:
        heapq.heappush(pq,(abs(x),x))
