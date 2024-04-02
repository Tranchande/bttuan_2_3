
def phan_tu_nhieu_nhat(A:list):
    C = set(arr)
    max_count = 0
    most_common = []
    for phantu in C:
        count = A.count(phantu)
        if count > max_count:
            max_count = count
            most_common = [phantu]
        elif count == max_count:
            most_common.append(phantu)
    return most_common
arr = [1, 2, 3, 4, 2, 2, 3, 3, 3, 5,2]
print("Các phần tử xuất hiện nhiều nhất trong mảng:", phan_tu_nhieu_nhat(arr))
