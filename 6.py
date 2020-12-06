from helper import printsol, read_text_file


@printsol
def part_1(input_data):
    lst = list()
    data=list()
    for i in input_data:
        if i == "":
            data.append(lst)
            lst = list()
            continue
        lst.extend([*i]) 
    sdata = list()
    for i in data: 
        sdata.append(len(set(i)))
    return sum(sdata)


@printsol
def part_2(input_data):
    lst = list()
    data=list()
    for i in input_data:
        if i == "":
            data.append(lst)
            lst = list()
            continue
        lst.append([*i]) 

    opt = 0
    for d in data:
        if len(d) == 1:
            opt += len(d[0])
        else:
            s = set.intersection(*map(set,d))
            opt += len(s)
    return opt


if __name__=="__main__":
    input_data = read_text_file("input_6.txt")
    part_1(input_data)
    part_2(input_data)    



