from helper import printsol, read_text_file
import math


def lower(low, high): 
    return low , (low+high) // 2


def upper(low, high):
    return math.ceil((low+high) / 2) , high


def process_row(data):
    mapping = {
        "F": lower,
        "B": upper
    }

    low, high = 0, 127
    for char in data[:6]: 
        low, high = mapping[char](low, high)
    
    return low if data[6] == "F" else high


def process_column(data):
    mapping = {
        "L": lower,
        "R": upper
    }

    low, high = 0, 7
    for char in data[7:9]: 
        low, high = mapping[char](low, high)
        
    return low if data[-1] == "L" else high


def get_seat_id(row, col):
    return (row*8) + col


@printsol
def part_1(input_data):
    MAX_SEAT_ID = 0
    for data in input_data: 
        if (seat_id:=get_seat_id(process_row(data), process_column(data))) > MAX_SEAT_ID:
            MAX_SEAT_ID = seat_id
    return MAX_SEAT_ID


@printsol
def part_2(input_data):
    seat_ids = list()
    for data in input_data: 
        seat_ids.append(get_seat_id(process_row(data), process_column(data)))
    
    seat_ids.sort()
    for i in range(len(seat_ids)):
        if abs(seat_ids[i] - seat_ids[i+1]) > 1: 
            return sum([seat_ids[i], seat_ids[i+1]]) // 2


if __name__=="__main__":
    input_data = read_text_file("input_5.txt")
    part_1(input_data)
    part_2(input_data)    