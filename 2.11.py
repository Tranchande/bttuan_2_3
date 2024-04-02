def findpairs(A, k):
    A.sort()
    pairs = []
    trai, phai = 0, len(A) - 1
    while trai < phai:
        sum = A[trai] + A[phai]
        if sum == k:
            pairs.append([A[trai], A[phai]])
            trai += 1
            phai -= 1
        elif sum < k:
            trai += 1
        else:
            phai -= 1
    return pairs
if __name__ == "__main__":
    A = [10, 50, 20, 30, 40]
    k = 70
    print(findpairs(A, k))
