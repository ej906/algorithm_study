a=int(input())
b=int(input())

b_str=str(b)

three = int(b_str[2])*a
four = int(b_str[1])*a
five = int(b_str[0])*a
print(three)
print(four)
print(five)
print(three+10*four+100*five)