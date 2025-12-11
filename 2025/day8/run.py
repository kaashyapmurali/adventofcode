import heapq
from collections import Counter

def read_data(filename):
    xyz = []
    with open(filename, 'r') as file:
        for line in file:
            text_value = line.strip().split(',')
            xyz.append([int(i) for i in text_value])
    return xyz

def distance(a, b):
    x1, y1, z1 = a[0], a[1], a[2]
    x2, y2, z2 = b[0], b[1], b[2]
    return ((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)**0.5

def get_product_part1(filename):
    data = read_data(filename)
    iterations = 10 if 'test' in filename else 1000
    n_points = len(data)

    pairwise_distances = [] # each element is (distance, i, j)
    for i in range(n_points):
        for j in range(i+1, n_points):
            pairwise_distances.append((distance(data[i], data[j]), i, j))
    pairwise_distances.sort(key = lambda x: x[0])
    
    circuit_number = [-i for i in range(n_points)] # point i index -> circuit number
    search_point = {} # {circuit_number -> [index i of point with that circuit number]}
    for c in range(n_points):
        search_point[-c] = [c]

    for _, p1, p2 in pairwise_distances[:iterations]:
        if circuit_number[p1] == circuit_number[p2]:
            continue
        c1, c2 = circuit_number[p1], circuit_number[p2]
        p1, p2 = (p1, p2) if len(search_point[c1]) >= len(search_point[c2]) else (p2, p1)
        while len(search_point[c2]) > 0:
            idx = search_point[c2].pop()
            circuit_number[idx] = c1
            search_point[c1].append(idx)

    # get product of top 3 circuits
    min_heap = []
    for k, l in search_point.items():
        if len(l) == 0:
            continue
        heapq.heappush(min_heap, len(l))
        if len(min_heap) > 3:
            heapq.heappop(min_heap)
    
    return min_heap[0] * min_heap[1] * min_heap[2]

def get_product_part2(filename):
    data = read_data(filename)
    n_points = len(data)

    pairwise_distances = [] # each element is (distance, i, j)
    for i in range(n_points):
        for j in range(i+1, n_points):
            pairwise_distances.append((distance(data[i], data[j]), i, j))
    pairwise_distances.sort(key = lambda x: x[0])
    
    circuit_number = [-i for i in range(n_points)] # point i index -> circuit number
    search_point = {} # {circuit_number -> [index i of point with that circuit number]}
    for c in range(n_points):
        search_point[-c] = [c]

    for _, p1, p2 in pairwise_distances:
        if circuit_number[p1] == circuit_number[p2]:
            continue
        c1, c2 = circuit_number[p1], circuit_number[p2]
        p1, p2 = (p1, p2) if len(search_point[c1]) >= len(search_point[c2]) else (p2, p1)
        while len(search_point[c2]) > 0:
            idx = search_point[c2].pop()
            circuit_number[idx] = c1
            search_point[c1].append(idx)
        if max(circuit_number) == min(circuit_number):
            return data[p1][0] * data[p2][0]

if __name__ == "__main__":
    test = False
    filename = 'test_input.txt' if test else 'input.txt'

    print('Part: 1')
    print(get_product_part1(filename))

    print('Part: 2')
    print(get_product_part2(filename))