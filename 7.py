from helper import printsol, read_text_file
import re
import string


@printsol
def part_1(input_data):
    data = {i.split("contain")[0]: i.split("contain")[1].split(",") for i in input_data}

    for k, v in data.items():
        data[k] = [i.lstrip().rstrip().split() for i in v]

    total_data = dict()

    for k, v in data.items():
        total_data[" ".join(k.split()[:2])] = [ ' '.join(z[1:3]) for z in v if z[0]!="no"]
    
    final = set()
    to_search = ["dark red", ]
    match = True


    while match: 
        ret = list()
        for color in to_search:
            ret.extend(get_containers(color, total_data))
        if len(ret) == 0: 
            match = False
        else:
            for i in ret:
                final.add(i) 
            to_search = ret

    print(len(final))
        

def get_containers(color, data):
    can_hold = list() 

    for k, v in data.items():
        for val in v:
            if val == color:
                can_hold.append(k)
    return can_hold


    
                    

        

    

    

    to_check = [] 


    print(can_hold)
    
    # print(total_data)




@printsol
def part_2(input_data):
    pass


if __name__=="__main__":
    input_data = read_text_file("input_7.txt")
    part_1(input_data)
    part_2(input_data)   