def read_data(file_name):
    reports = []
    with open(file_name, 'r') as file:
        for line in file:
            levels = [int(i) for i in line.strip().split(' ')]
            reports.append(levels)
    return reports

def check_safety(report):
    if report[1] > report[0]:
        increasing = 1
    elif report[1] < report[0]:
        increasing = -1
    else:
        increasing = 0
    curr_value = report[0]
    i = 1
    for i in range(1, len(report)):
        difference = report[i] - report[i-1]
        if difference * increasing < 1 or difference * increasing > 3:
            return 0
    return 1

def check_safety_removing_an_item(report):
    for i in range(0, len(report)):
        modified_list = report[:i] + report[i+1:]
        if check_safety(modified_list) == 1:
            return 1
    return 0

def count_safe_reports(file_name):
    reports = read_data(file_name)
    print(f"Total Reports: {len(reports)}")
    safe_count = 0
    for report in reports:
        if check_safety(report) == 1:
            safe_count += 1
        elif check_safety_removing_an_item(report) == 1: # only for part 2
            safe_count += 1
    print(f"Number of safe reports: {safe_count}")
    return safe_count

if __name__ == "__main__":
    count_safe_reports('test_input.txt')
    count_safe_reports('input.txt')
    