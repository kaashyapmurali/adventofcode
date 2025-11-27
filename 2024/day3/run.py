import re

def read_data(file_name):
    programs = []
    with open(file_name, 'r') as file:
        for line in file:
            text_value = line.strip()
            programs.append(text_value)
    return programs

def process_text(file_name):
    q = []
    programs = read_data(file_name)
    pattern = "mul\(([0-9]+),([0-9]+)\)"
    for program in programs:
        q = q + re.findall(pattern, program)
    
    result = 0
    for i, j in q:
        result += int(i) * int(j)
    return result

def process_text_part2(file_name):
    q = []
    programs = read_data(file_name)
    pattern = "(do\(\))|(don't\(\))|mul\(([0-9]+),([0-9]+)\)"
    for program in programs:
        q = q + re.findall(pattern, program)
    multiply = 1
    result = 0
    for do, dont, i, j in q:
        if do == 'do()':
            multiply = 1
        elif dont == "don't()":
            multiply = 0
        elif multiply == 1:
            result += int(i) * int(j)
    return result

if __name__ == "__main__":
    print(process_text("test_input.txt"))
    print(process_text("input.txt"))
    print(process_text_part2("test_input.txt"))
    print(process_text_part2("input.txt"))