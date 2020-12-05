from helper import printsol

with open("data/input_2.txt", "r") as f:
    raw = f.readlines()
    input_data = [r.replace("\n", "") for r in raw]

data = [i.split(":") for i in input_data]

RULES = list()

# ['3-5 s', ' sbsssss']

for pair in data:
    range_, letter = pair[0].split()
    minimum, maximum = range_.split("-")
    RULES.append(
        {
            "letter": letter,
            "min": int(minimum),
            "max": int(maximum),
            "text": pair[1].replace(" ", ""),
        }
    )
"""
RULES = [
    {'letter': 'm', 'min': '16', 'max': '18', 'text': 'mmtmrxmmmmmmmmmcmmm'},
    {'letter': 'b', 'min': '9', 'max': '11', 'text': 'bkbltdvbtwbbtsb'}
    .
    .
    .
]
"""


@printsol
def part_1():
    valid_count = 0
    for password in RULES:
        letter_count = password["text"].count(password["letter"])
        if letter_count >= password["min"] and letter_count <= password["max"]:
            valid_count += 1
    print(valid_count)
    return valid_count


part_1()

@printsol
def part_2():
    valid_count = 0
    for password in RULES:
        text_split = [*password['text']]
        text_compare = text_split[password["min"]-1] + text_split[password["max"]-1]
        if text_compare.count(password["letter"]) == 1:
            valid_count += 1
    print(valid_count)
    return valid_count


part_2()
