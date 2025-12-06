def read_data(filename):
    fresh, ingredients = [], []
    with open(filename, 'r') as file:
        for line in file:
            text_value = line.strip()
            if '-' in text_value:
                start, finish = text_value.split('-')
                start, finish = int(start), int(finish)
                fresh.append((start, finish))
            elif len(text_value) > 0:
                ingredients.append(int(text_value))
    fresh.sort()
    return fresh, ingredients

def get_total_fresh_ingredients_part1(filename):
    fresh, ingredients = read_data(filename)
    total = set()
    n = len(fresh)
    for i in ingredients:
        for start, end in fresh:
            if i >= start and i <= end:
                total.add(i)
                continue
            elif i > end:
                continue
    return len(total)

def get_total_fresh_ingredients_part2(filename):
    fresh, _ = read_data(filename)
    s, e = fresh[0]
    total = e-s+1
    for start, end in fresh[1:]:
        if start <= e:
            total = total + max(end, e) - e
            e = max(end, e)
        elif start > e:
            total += end - start + 1
            s, e = start, end
    return total

if __name__ == "__main__":
    test = True
    filename = 'test_input.txt' if test else 'input.txt'

    print('Part: 1')
    print(get_total_fresh_ingredients_part1(filename))

    print('Part: 2')
    print(get_total_fresh_ingredients_part2(filename))