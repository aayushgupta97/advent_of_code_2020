with open("data/input_3.txt", "r") as f:
    raw = f.readlines()
    input_data = [r.replace("\n", "") for r in raw]

print(input_data)
# valid = "."
# tree = "#"
# right = 3
# down = 1
# tree_count = 0 

# pos = [0, 0]

# for i in range(len(input_data)):
#     pos = [pos[0] , pos[1] + 3]
#     to_right_pos = pos
#     to_right_char = input_data[to_right_pos[0]][to_right_pos[1]]
#     print(to_right_pos, to_right_char)
    
#     pos = [pos[0] + 1 , pos[1]]
#     to_down_pos = pos
#     if pos[0] == 323:
#         break
#     to_down_char = input_data[to_down_pos[0]][to_down_pos[1]]
#     i+=1
#     if pos[1] > 27:
#         pos[1] = pos[1] + 3 - 31
    
#     if to_down_char == tree:
#         tree_count+=1

# print(tree_count)



# tree_count = 0
# pos = 0
# go_right = True
# for row in input_data:
#     if row[pos] == "#":
#         tree_count += 1
#     print(pos)
#     if go_right:
#         if pos > 27:
#             pos = pos + 3 - len(row)
#         else:
#             pos = pos + 3
#         go_right = False

#     elif not go_right:
#         go_right = True

    

# print(tree_count)


    
data = [r*100 for r in input_data]

tree_count = 0
pos = 0
go_right = True
if data[0][0] == "#":
    tree_count += 1

for index, row in enumerate(data):
    print(index, pos)

    if row[pos] == "#":
            tree_count += 1
    pos += 3
    


print(tree_count)




def part_2():
    data = [r*80 for r in input_data]
    counts = []
    for i in [1, 3, 5, 7]:
        pos = 0
        tree_count = 0
        for index, row in enumerate(data):
            if row[pos] == "#":
                tree_count += 1
            pos += i
        counts.append(tree_count)

    pos = 0
    tree_count = 0  
    for index, row in enumerate(data):
        if index % 2 == 0 and index > 1:
            pos += 1
            if row[pos] == "#":
                    tree_count += 1
    counts.append(tree_count)
    return counts

p2 = part_2()
print(p2)
result = 1
for num in p2:
    result = result * num
print("The answer for part 2 is {}".format(result))
    


        
