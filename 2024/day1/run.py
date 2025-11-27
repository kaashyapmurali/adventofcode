from collections import Counter

def read_data(file_name):
    A, B = [], []
    with open(file_name, 'r') as file:
        for line in file:
            entries = line.strip().split()
            A.append(int(entries[0]))
            B.append(int(entries[1]))
    return A, B

def get_distances_part_1():
    A, B = read_data('input.txt')
    A.sort()
    B.sort()
    total_distance = 0
    for a, b in zip(A, B):
        total_distance += abs(a - b)
    return total_distance

def get_distances_part_2():
    A, B = read_data('input.txt')
    count_B = Counter(B)
    total_distance = 0
    for i in A:
        multiplier = count_B.get(i, 0)
        total_distance += abs(i) * multiplier
    return total_distance

if __name__ == "__main__":
    result = get_distances_part_1()
    print(f"Part 1 Total Distance: {result}")
    result = get_distances_part_2()
    print(f"Part 2 Total Distance: {result}")