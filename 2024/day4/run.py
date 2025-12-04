def read_data(file_name):
    data = []
    with open(file_name, 'r') as file:
        for line in file:
            text_value = [i for i in line.strip()]
            data.append(text_value)
    return data

def word_search_part1(filename):
    data = read_data(filename)
    ROWS, COLS = len(data), len(data[0])
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    word = "XMAS"
    count = 0

    # DFS function to find the phrase in only one direction
    def dfs(i, j, dx, dy):
        nonlocal count
        for k in range(len(word)):
            i_next, j_next = i + k*dx, j + k*dy
            if i_next < 0 or j_next < 0 or i_next >= ROWS or j_next >= COLS or data[i_next][j_next] != word[k]:
                return
        count+=1
        return

    # run dfs in all directions if there's a match with X
    for r in range(ROWS):
        for c in range(COLS):
            if data[r][c] == 'X':
                for dx, dy in directions:
                    dfs(r, c, dx, dy)
    return count

def word_search_part2(filename):
    data = read_data(filename)
    ROWS, COLS = len(data), len(data[0])
    count = 0

    # DFS function to find the phrase in only one direction
    def dfs(i, j):
        directions_1 = [(-1, -1), (1, 1)]
        directions_2 = [(1, -1), (-1, 1)]
        values = ''
        for dx, dy in directions_1:
            i_new, j_new = i + dx, j + dy
            if i_new < 0 or j_new < 0 or i_new >= ROWS or j_new >= COLS or data[i_new][j_new] not in ['M', 'S']:
                return 0
            values = values + data[i_new][j_new]
        if values not in ['MS', 'SM']:
            return 0

        values = ''
        for dx, dy in directions_2:
            i_new, j_new = i + dx, j + dy
            if i_new < 0 or j_new < 0 or i_new >= ROWS or j_new >= COLS or data[i_new][j_new] not in ['M', 'S']:
                return 0
            values = values + data[i_new][j_new]
        if values not in ['MS', 'SM']:
            return 0
        return 1

    # run dfs in all directions if there's a match with X
    for r in range(ROWS):
        for c in range(COLS):
            if data[r][c] == 'A':
                count += dfs(r, c)
    return count

if __name__ == "__main__":
    test = False
    filename = 'test_input.txt' if test else 'input.txt'
    print(word_search_part1(filename))
    print(word_search_part2(filename))