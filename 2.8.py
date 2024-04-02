A = [[1,1,0,0],[1,0,1,1],[0,0,0,0],[1,1,1,0]]
B = []
for i in A:
    i = i[::-1]
    for j in range(len(i)):
        i[j] = abs(i[j]-1)
    print(i)