def sapxep(A:list,B:list):
    A.extend(B)
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            if A[i]>A[j]:
                A[i],A[j] = A[j],A[i]
    print(A)
C =[2,4,6,8,10,13]
D =[1,3,5,7,9,12]
sapxep(C,D)