with open("data/input_1.txt", 'r') as f:
    input_data = f.readlines()


data = [int(i.replace("\n", "")) for i in input_data]

print(len(data))

def part_1():
    for i in data: 
        for j in data: 
            if i + j == 2020:
                print(i * j) 
            

def part_2():
    for i in data: 
        for j in data: 
            for k in data: 
                if i + j + k == 2020:
                    print(i*j*k)
                    exit()

part_2()