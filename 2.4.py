def missing_number(A:list):
    return len(A)*(len(A)+1)/2 - sum(A)
A=[0,1,2,3,4,5,7]
print("so còn thiếu là: ",missing_number(A))