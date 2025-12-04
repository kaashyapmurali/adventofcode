import re

def read_data(filename):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            text_value = line.strip().split(',')
            for t in text_value:
                if len(t) > 0:
                    start, end = t.split('-')
                    data.append((int(start), int(end)))
    return data

def check_validity_part1(k):
    k_string = str(k)
    if len(k_string) % 2 == 1:
        return 0
    mid = int(len(k_string)/2)
    if k_string[:mid] == k_string[mid:]:
        return k
    return 0

def check_validity_part2(k):
    k_string = str(k)
    for i in range(1, len(k_string)//2+1):
        pattern = f"({k_string[:i]})"
        repeats = re.findall(pattern, k_string)
        if ''.join(repeats) == k_string:
            return k
    return 0


def search(filename, part=1):
    data = read_data(filename)
    output = 0
    for start, end in data:
        for i in range(start, end+1):
            if part == 1:
                output += check_validity_part1(i)
            elif part == 2:
                output += check_validity_part2(i)
    return output

if __name__ == "__main__":
    test = False
    filename = 'test_input.txt' if test else 'input.txt'
    print(search(filename, part=2))