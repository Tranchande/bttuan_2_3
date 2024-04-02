A = [9]
s = int("".join(map(str,A)))
s +=1
a = []
while s > 0:
    temp = s%10
    a.append(temp)
    s = s//10
a = a[::-1]
print(a)