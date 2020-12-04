import re
import string

with open("data/input_4.txt", "r") as f:
    data = list()
    one_pass = list()
    for line in f.readlines():
        if line == "\n":
            data.append({i.split(":")[0]: i.split(":")[1] for i in one_pass})
            one_pass = []
            continue
        op = line.replace("\n", "").split()

        one_pass.extend(op)


# def part_1():
#     northpole_valid = sorted(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
#     passport_valid = sorted(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"])
#     valid_count = 0 

#     for d in data:
#         if (
#             sorted(d.keys()) == northpole_valid or
#             sorted(d.keys()) == passport_valid
#             ):
#             valid_count+=1
#     return valid_count


# Optimized one line solution
def part_1():
    valid_fields = sorted(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
    return [all([field in passport for field in valid_fields]) for passport in data].count(True)
    

a_f = [*string.ascii_lowercase[:6]]
digits = [*string.digits]

def part_2():
    northpole_valid = sorted(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
    passport_valid = sorted(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"])
    valid_count = 0 
    

    for d in data:
        valid = True
        try: 
            if (
                sorted(d.keys()) == northpole_valid or
                sorted(d.keys()) == passport_valid
                ):
                for k, v in d.items():

                    if k == "byr": 
                        if len(v) == 4:
                            assert int(v) >= 1920 and int(v) <=2002

                    if k == "iyr": 
                        if len(v) == 4:
                            assert int(v) >= 2010 and int(v) <=2020

                    if k == "eyr": 
                        if len(v) == 4:
                            assert int(v) >= 2020 and int(v) <=2030

                    if k == "hgt": 
                        match = re.match(r"([0-9]+)([a-z]+)", v, re.I)
                        if match:
                            items = match.groups()
                            assert items[1] == "cm" or items[1] == "in"
                            if items[1] == "cm":
                                assert int(items[0]) >= 150 and int(items[0]) <=193
                            elif items[1] == "in":
                                assert int(items[0]) >= 59 and int(items[0]) <=76
                        else:
                            raise AssertionError
                        

                    if k == "hcl": 
                        match = re.match(r"^#([A-Fa-f0-9]{6})", v, re.I)
                        if match is None:
                            raise AssertionError
                    if k == "ecl": 
                        assert v in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
                        
                    if k == "pid": 
                        assert len(v) == 9
                        match = re.match(r"([0-9]{9})", v)
                        if match is None:
                            raise AssertionError


                if valid:
                    valid_count+=1

                    
                
        except AssertionError:
            valid = False
        

        
    return valid_count

# print(part_2())



if __name__=="__main__":
    p1 = part_1()
    p2 = part_2()
    print("The Solution to part 1 is : {}".format(p1))
    print("The Solution to part 2 is : {}".format(p2))
