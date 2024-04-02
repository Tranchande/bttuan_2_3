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
if __name__ == "__main__":
    fo=open('text.txt','r')
    lines = fo.readlines()
#    read_all_lines(lines)
#    read_first(lines,2)
#    read_last(lines,2)
    find_max(lines)
    find_min(lines)
#    count_lines(lines)
    statics_char(lines)
    print(find_max_char(lines))

    fo.close()