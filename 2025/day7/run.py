def read_data(filename):
    numbers = []
    with open(filename, 'r') as file:
        for line in file:
            text_value = line.strip()
            numbers.append(text_value)
    return numbers


def get_total_splits_part1(filename):
    data = read_data(filename)
    ROWS, COLS = len(data), len(data[0])
    beams = [1 if data[0][c] == 'S' else 0 for c in range(COLS)]
    splits = 0

    for r in range(1, ROWS):
        for c in range(COLS):
            if data[r][c] == '^' and beams[c] == 1:
                beams[c-1], beams[c+1], beams[c] = 1, 1, 0
                splits += 1
    return splits

def get_total_splits_part2(filename):
    data = read_data(filename)
    ROWS, COLS = len(data), len(data[0])
    beams = [1 if data[0][c] == 'S' else 0 for c in range(COLS)]
    memory = {}

    def backtrack(r, b):
        nonlocal memory
        if r == ROWS - 1:
            return 1
        
        if (r, b) in memory:
            return memory[(r, b)]

        if data[r][b] == '^':
            result =  backtrack(r+1, b-1) + backtrack(r+1, b+1)
        else:
            result = backtrack(r+1, b)
        memory[(r, b)] = result
        return result

    return backtrack(0, beams.index(1, 0)) 

if __name__ == "__main__":
    test = False
    filename = 'test_input.txt' if test else 'input.txt'

    print('Part: 1')
    print(get_total_splits_part1(filename))

    print('Part: 2')
    print(get_total_splits_part2(filename))