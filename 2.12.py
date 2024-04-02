def findtruepair(A:list,k):
    A.sort()
    B = []
    B.extend(A)
    trai, phai = 0, len(A) - 1
    while trai < phai:
        sum = A[trai] + A[phai]
        if sum == k:
            B.remove(A[trai])
            B.remove(A[phai])
            trai += 1
            phai -= 1
        elif sum < k:
            trai += 1
        else:
            phai -= 1
    return B == []
if __name__ == "__main__":
    A = [60, 50, 80, 30, 40, 10]
    k = 90
    print(findtruepair(A,k))