def can_make_it(grid, start, dest, k):
    # each element follows the form (position, gas, visited)
    queue = [(start, k, set())]

    while queue:
        pos, gas, visited = queue.pop(0)

        if pos == dest:
            return True

        if gas == 0:
            continue

        visited.add(pos)
        for n in get_neighbors(grid, pos):
            if n in visited:
                continue

            x, y = n
            if grid[x][y] == "x":
                continue

            new_gas = 0
            if grid[x][y] != "o":
                new_gas += int(grid[x][y])

            new_visited = visited.copy()
            queue.append((n, gas - 1 + new_gas, new_visited))

    return False


def get_neighbors(grid, pos):
    neighbors = []

    x, y = pos
    if x + 1 < len(grid):
        neighbors.append((x+1, y))
    if x - 1 >= 0:
        neighbors.append((x-1, y))
    if y + 1 < len(grid[0]):
        neighbors.append((x, y+1))
    if y - 1 >= 0:
        neighbors.append((x, y-1))

    return neighbors


INPUT_1 = [
    ["o", "o", "o", "o", "3"],
    ["o", "x", "x", "x", "o"],
    ["o", "x", "o", "o", "o"],
    ["o", "x", "o", "o", "o"],
    ["o", "o", "o", "o", "o"],
]


def main():
    if can_make_it(INPUT_1, (0, 0), (0, 4), 4):
        print("Test passed!")
    else:
        print("Test failed")


if __name__ == '__main__':
    main()
