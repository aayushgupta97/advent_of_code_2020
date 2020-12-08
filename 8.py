from helper import printsol, read_text_file


@printsol
def part_1(input_data):
    global accumulator
    start = True
    index = 1
    ran = list()
    while index > 0 and index < len(input_data):
        if start:
            index = 0
            start = False
        if index in ran:
            break
        ran.append(index)
        ins = input_data[index]
        if ins[0] == "nop":
            index +=1
            continue
        elif ins[0] == "acc": 
            index +=1
            accumulator += int(ins[1])
        elif ins[0] == "jmp":
            index += int(ins[1])
        
    return (accumulator)
    


@printsol
def part_2(input_data):
    global indexes
    jmp_change_counter = 0
    nop_change_counter = 0
    change_jmp = True
    
    run_again = True
    accumulator = 0
    change_back_to = {"index": 0, "value": "nop"}

    mapping = {"jmp": "nop", 
    "nop": "jmp"}
    ended_normally = list()
    for i in indexes:       
 
        accumulator = 0
        start = True
        ran = list()
        index = 0
        input_data[i][0] = mapping[input_data[i][0]] 


        ans = True
        while index >= 0:

            if index >= len(input_data) or index in ran:
                ended_normally.append({"index": index, "acc": accumulator})
                index = -1
                ans = False
                break

            ran.append(index)
            ins = input_data[index]
            if ins[0] == "nop":
                index +=1
                continue
            elif ins[0] == "acc": 
                index +=1
                accumulator += int(ins[1])
            elif ins[0] == "jmp":
                index += int(ins[1])
        if ans:
            break
        input_data[i][0] = mapping[input_data[i][0]] 

    for i in ended_normally:
        if i["index"]> 633:
            return i['acc']
    return None

if __name__=="__main__":
    accumulator = 0
    index = 0

    input_data = read_text_file("input_8.txt")
    raw_split = [i.split() for i in input_data]
    # print(raw_split)
    indexes = [i for i, v in enumerate(raw_split) if v[0] =='nop' or v[0] == 'jmp']
    data = {i: v for i, v in enumerate(raw_split)}
    print("Lengths: Indexes: {}, DATA: {}".format(len(indexes) , len(data)))
    part_1(data)
    part_2(data)    