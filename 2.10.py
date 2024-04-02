
def timmaxlietiep(A:list,k):
    D = []
    index_max = 0
    max  = 0
    if k > len(A):
        return A
    else:
        for i in range(0,len(A)-k+1):
            B = A[i:i+k]
            temp = sum(B)
            if max < temp:
                max = temp
                index_max = i
        for i in range(0,len(A)-k+1):
            C = A[i:i+k]
            temp1 = sum(C)
            if max == temp1:
                print(C)
                D.append(C)
        return D
if __name__ == "__main__":
    A = [10, 50, 20, 30, 40]
    print(timmaxlietiep(A,2))