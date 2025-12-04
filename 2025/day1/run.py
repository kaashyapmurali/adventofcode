def read_data(file_name):
    data = []
    with open(file_name, 'r') as file:
        for line in file:
            text_value = line.strip()
            data.append(text_value)
    return data

def rotate_part1(curr, input):
    factor = {'L': -1, 'R': 1}
    direction = factor[input[0]]
    change = int(input[1:])
    curr = curr + direction*change
    if curr > 99:
        curr = curr % 100
    elif curr < 0:
        curr =  (100 - (-curr % 100)) % 100
    return curr

def rotate_part2(curr, input):
    factor = {'L': -1, 'R': 1}
    hits = 0
    start = 1 if curr == 0 else 0
    direction = factor[input[0]]
    change = int(input[1:])
    curr = curr + direction*change
    if curr > 99:
        hits = curr // 100
        curr = curr % 100
    elif curr < 0:
        hits = (-curr//100) + 1 if start == 0 else (-curr//100)
        curr =  (100 - (-curr % 100)) % 100
    elif curr == 0:
        hits = 1
        
    return curr, hits

def get_result_part1(filename):
    data = read_data(filename)
    curr = 50
    count = 0
    for d in data:
        curr = rotate_part1(curr, d)
        if curr == 0:
            count += 1
    return curr, count

def get_result_part2(filename):
    data = read_data(filename)
    curr = 50
    count = 0
    for d in data:
        curr, hits = rotate_part2(curr, d)
        count += hits
    return curr, count

if __name__ == "__main__":
    print('Part 1')
    print(get_result_part1('test_input.txt'))
    print(get_result_part1('input.txt'))

    print('Part 2')
    print(get_result_part2('test_input.txt'))
    print(get_result_part2('input.txt'))