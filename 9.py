from helper import printsol, read_text_file
import sys


@printsol
def part_1(input_data):
    preamble = 25
    data = [int(i) for i in input_data]
    print(data)
    cool = True
    num = 0
    for i, v in enumerate(data): 
        if i >=5: 
            new_list = data[i-preamble : i]
            for a in new_list:
                for b in new_list:
                    if a+b == v:
                        print(cool)
                        cool = True
                        break
                    else: 
                        cool = False
                if cool:
                    break
            if cool == True:
                continue
            else: 
                num =  v
                return num
                sys.exit()
        else:
            print(i, v)
    return num


@printsol
def part_2(input_data):
    data = [int(i) for i in input_data]
    s = 26796446
    curr_sum = 0 
    for i in range(len(data)):
        curr_sum = data[i]

        j = i+1
        while j <= len(data): 
            if curr_sum == s:
                lst =  data[i: j-1]
                return sum([min(lst) , max(lst)])
            if curr_sum > s or j == len(data):
                break 

            curr_sum = curr_sum + data[j]
            j+=1
    print("No sum found")




if __name__=="__main__":
    input_data = read_text_file("input_9.txt")
    part_1(input_data)
    part_2(input_data)    