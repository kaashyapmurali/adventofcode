from collections import deque
def read_data(filename):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            text_value = line.strip()
            data.append([i for i in text_value])
    return data

def get_total_rolls_part1(filename):
    data = read_data(filename)
    ROWS, COLS = len(data), len(data[0])
    total_rolls = 0
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    for r in range(ROWS):
        for c in range(COLS):
            curr = 0
            if data[r][c] == '@':
                for dx, dy in directions:
                    rdx, cdy = r + dx, c + dy
                    if rdx >= 0 and cdy >= 0 and rdx < ROWS and cdy < COLS and data[rdx][cdy] == '@':
                        curr += 1
                if curr < 4:
                    total_rolls += 1
    return total_rolls

def get_total_rolls_part2(filename):
    data = read_data(filename)
    ROWS, COLS = len(data), len(data[0])
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    total_rolls = 0
    start = True
    visited = set()
    while start or visited:
        start = False
        visited = set()
        for r in range(ROWS):
            for c in range(COLS):
                curr = 0
                if data[r][c] == '@':
                    for dx, dy in directions:
                        rdx, cdy = r + dx, c + dy
                        if rdx >= 0 and cdy >= 0 and rdx < ROWS and cdy < COLS and data[rdx][cdy] == '@':
                            curr += 1
                    if curr < 4:
                        total_rolls += 1
                        visited.add((r, c))
        for r, c in visited:
            data[r][c] = 'x'
    return total_rolls

if __name__ == "__main__":
    test = False
    filename = 'test_input.txt' if test else 'input.txt'
    print(get_total_rolls_part1(filename))
    print(get_total_rolls_part2(filename))