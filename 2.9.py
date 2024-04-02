A = [1, 0, -1, 3, -1, -3, 2]
b =[]
c=[]
A.sort()
for i in range(len(A)):
    if i > 0 and A[i] == A[i - 1]:
        continue
    for j in range(i+1,len(A)):
        for k in range(j+1,len(A)):
            if A[i] + A[j] + A[k] == 0:
                b.append(A[i])
                b.append(A[j])
                b.append(A[k])
                c.append(b)
                b = []
print(c)