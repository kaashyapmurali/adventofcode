def read_data(filename, part=1):
    numbers = []
    if part == 1:
        with open(filename, 'r') as file:
            for line in file:
                text_value = line.strip().split()
                numbers.append(text_value)
        operations = numbers[-1].copy()
    elif part == 2:
        with open(filename, 'r') as file:
            for line in file:
                text_value = line.strip('\n')
                numbers.append(text_value)
        operations = numbers[-1].split()
    numbers = numbers[:-1]
    return numbers, operations

def compute(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '*':
        return num1 * num2

def get_math_result(filename, part=1):
    numbers, operations = read_data(filename, part=part)
    if part == 1:
        ROWS, COLS = len(numbers), len(numbers[0])
        total = 0
        for o in range(COLS):
            curr = 1 if operations[o] == '*' else 0
            for n in range(ROWS):
                curr = compute(curr, int(numbers[n][o]), operations[o])
            total += curr
        return total
    
    elif part == 2:
        ROWS, ROW_idx, n_operations = len(numbers), len(numbers[0]) - 1, len(operations) - 1
        result = 0
        curr_list = []
        while n_operations >= 0 and ROW_idx >= 0:
            detect_number = False
            curr_number = ''
            for i in range(ROWS):
                if numbers[i][ROW_idx] != ' ':
                    detect_number = True
                    curr_number = curr_number + numbers[i][ROW_idx]
            if detect_number:
                curr_list.append(int(curr_number))
            else:
                col_total = 1 if operations[n_operations] == '*' else 0
                for item in curr_list:
                    col_total = compute(col_total, item, operations[n_operations])
                result += col_total
                n_operations -= 1
                curr_list = []
            ROW_idx -= 1

        # compute the last set of numbers
        col_total = 1 if operations[n_operations] == '*' else 0
        for item in curr_list:
            col_total = compute(col_total, item, operations[n_operations])
        result += col_total
        return result

if __name__ == "__main__":
    test = False
    filename = 'test_input.txt' if test else 'input.txt'

    print('Part: 1')
    print(get_math_result(filename, part=1))

    print('Part: 2')
    print(get_math_result(filename, part=2))