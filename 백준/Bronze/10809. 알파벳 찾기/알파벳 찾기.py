s=input()

for i in range(ord('a'),ord('z')+1):
    char=chr(i)
    try:
        print(s.index(char),end=' ')
    except ValueError:
        print(-1,end=' ')
