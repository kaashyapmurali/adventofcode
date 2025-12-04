from collections import deque
def read_data(filename):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            text_value = line.strip()
            data.append(text_value)
    return data

def get_max_voltage(value):
    l = deque()
    for i in value:
        curr = int(i)
        l.append(curr)
        if len(l) > 2:
            if l[0] >= l[1]:
                if l[-2] > l[-1]:
                    _ = l.pop()
                else:
                    tmp = l.pop()
                    l[-1] = tmp
            else:
                _ = l.popleft()
    return int(l[0]*10 + l[1])

def get_max_voltage_part2(value):
    s = []
    n = len(value)
    for i in range(n):
        curr = int(value[i])
        while len(s) > 0 and n - i - 1 >= 12 - len(s) and curr > s[-1]:
            s.pop()
        s.append(curr)
    result = int(''.join([str(i) for i in s[:12]]))
    return result

def total_voltage(filename, part=1):
    data = read_data(filename)
    output = 0
    for d in data:
        if part == 1:
            output += get_max_voltage(d)
        elif part == 2:
            output += get_max_voltage_part2(d)
    return output

if __name__ == "__main__":
    test = False
    filename = 'test_input.txt' if test else 'input.txt'
    print(total_voltage(filename, part=1))
    print(total_voltage(filename, part=2))