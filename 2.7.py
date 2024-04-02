A = [3, 30, 34, 5, 9]
arr_1 = list(map(str, A))
for i in range(len(arr_1)):
    for j in range(i+1,len(arr_1)):
        if arr_1[i] + arr_1[j] < arr_1[j] + arr_1[i]:
            arr_1[i],arr_1[j] = arr_1[j],arr_1[i]
s = "".join(map(str,arr_1))
print(s)