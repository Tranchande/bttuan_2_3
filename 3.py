def read_all_lines(lines):
        for line in lines:
            print(line)
def read_first(lines,n):
    first_n = lines[0:n]
    for i in first_n:
        print(i)
def read_last(lines,n):
    last_n = lines[len(lines)-n:len(lines)]
    for i in last_n:
        print(i)
def find_max(lines):
    max_line = 0
    for i in range(len(lines)):
        if max_line< len(lines[i]):
            max_line = len(lines[i])
    for i in range(len(lines)):
        if max_line == len(lines[i]):
            print(lines[i])
def find_min(lines):
    min_line = len(lines[0])
    for i in range(len(lines)):
        if min_line > len(lines[i]) and len(lines[i])!=1:
            min_line = len(lines[i])
    for i in range(len(lines)):
        if min_line == len(lines[i]) and len(lines[i])!=1:
            print(lines[i])
def count_lines(lines):
    return print(len(lines))
def statics_char(lines):
    temp = []
    for i in range(len(lines)):
        lines[i] = lines[i].replace(',',' ').replace('.','')
    temp = lines[0].split()
    for i in range(1,len(lines)):
        temp.extend(lines[i].split())
    dic = {}
    for i in temp:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    print(dic)
def find_max_char(lines):
    temp = []
    for i in range(len(lines)):
        lines[i] = lines[i].replace(',',' ').replace('.','')
    temp = lines[0].split()
    for i in range(1,len(lines)):
        temp.extend(lines[i].split())
    dic = {}
    for i in temp:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    max = 0
    name_max = None
    for name, number in dic.items():
        if max <= number:
            max = number
            name_max = name
    return name_max, max
def find_min_char(lines):
    temp = []
    for i in range(len(lines)):
        lines[i] = lines[i].replace(',',' ').replace('.','')
    temp = lines[0].split()
    for i in range(1,len(lines)):
        temp.extend(lines[i].split())
    dic = {}
    for i in temp:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    min = 50
    name_max = None
    for name, number in dic.items():
        if min >= number:
            min = number
            name_max = name
    return name_max, min
def find_ket_thuc(lines,k):
    count = 0
    for i in range(len(lines)):
        lines[i] = lines[i].replace(',',' ').replace('.','')
    temp = lines[0].split()
    for i in range(1,len(lines)):
        temp.extend(lines[i].split())
    dic = {}
    for i in temp:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    for name in dic:
        if name[-1] == k:
            print(name)
            count+=1
    return count
def so_luong_chu_cai(lines):
    for i in range(len(lines)):
        lines[i] = lines[i].replace(',', ' ').replace('.', '')
    temp = lines[0].split()
    for i in range(1, len(lines)):
        temp.extend(lines[i].split())
    dic = {}
    for i in temp:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    return sum(dic.values())
def thongke_tu_n_k(lines,n,k):
    for i in range(len(lines)):
        lines[i] = lines[i].replace(',', ' ').replace('.', '')
    temp = lines[0].split()
    for i in range(1, len(lines)):
        temp.extend(lines[i].split())
    dic = {}
    for i in temp:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    for name,number in dic.items():
        if number>= n and number <=k:
            print(name)
def get_most_common_words_before_target(lines, target_word, n):
    for i in range(len(lines)):
        lines[i] = lines[i].replace(',', ' ').replace('.', '')
    words = lines[0].split()
    for i in range(1, len(lines)):
        words.extend(lines[i].split())
    word_counts = {}
#    print(words)
    for i in range(1, len(words)):
        if words[i] == target_word:
            word_before = words[i - 1]
            if word_before in word_counts:
                word_counts[word_before] +=1
            else:
                word_counts[word_before] = 1
    print(word_counts)
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_word_counts[:n]
def copy_new_file(lines,n,k):
    fo = open("output.txt",'w')
    for i in range(n-1,k):
        fo.write(lines[i])
def find_word_in_lines(lines,k):
    check = []
    for i in range(len(lines)):
        lines[i] = lines[i].replace(',', ' ').replace('.', '')
        temp = lines[i].split()
        if k in temp:
            check.append(i)
        temp = []
    if check == []:
        return None
    else:
        return check
if __name__ == "__main__":
    fo=open('text.txt','r')
    lines = fo.readlines()
#    read_all_lines(lines)
#    read_first(lines,2)
#    read_last(lines,2)
#    find_max(lines)
#    find_min(lines)
#    count_lines(lines)
 #   statics_char(lines)
#    print(find_max_char(lines))
#    print(find_min_char(lines))
#    print(find_ket_thuc(lines,"u"))
#    print(so_luong_chu_cai(lines))
#    thongke_tu_n_k(lines,5,10)
#    copy_new_file(lines,1,3)
 #   print(get_most_common_words_before_target(lines,"Pikachu",2))
#    print(find_word_in_lines(lines,"Pikachuu"))
    fo.close()