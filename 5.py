from helper import printsol
import math


with open("data/input_5.txt", "r") as f:
    raw = f.readlines()
    input_data = [r.replace("\n", "") for r in raw]




def lower(low, high): 
    """
    LOWER HALF
    """
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


def get_seat_id(row, column):
    return (row*8) + column


@printsol
def part_1():
    MAX_SEAT_ID = 0
    for data in input_data: 
        row = process_row(data)
        col = process_column(data)
        seat_id = get_seat_id(row, col)
        if seat_id > MAX_SEAT_ID:
            MAX_SEAT_ID = seat_id
    return MAX_SEAT_ID


@printsol
def part_2():
    seat_ids = list()
    for data in input_data: 
        row = process_row(data)
        col = process_column(data)
        seat_id = get_seat_id(row, col)
        seat_ids.append(seat_id)
    seat_ids.sort()
    for i in range(len(seat_ids)):
        if abs(seat_ids[i] - seat_ids[i+1]) > 1: 
            return sum([seat_ids[i], seat_ids[i+1]]) // 2



if __name__=="__main__":

    part_1()
    part_2()    