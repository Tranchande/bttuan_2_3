A = ["An", "Lan", "Tan"]
B = [160, 155, 170]
for i in range(len(B)-1):
    for j in range(len(B)-1):
        if B[i] > B[j]:
            B[i], B[j] = B[j], B[i]
            A[i], A[j] = A[j], A[i]

print(A)
print(B)
