def find_k(A:list,k):
    A.sort()
    return A[len(A)-k]
A = [3, 30, 34, 5, 9]
k = 5
print(find_k(A,k))