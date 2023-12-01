from typing import List, Tuple


def can_make_it(grid: List[List[str]], start: Tuple(int, int),
                dest: Tuple(int, int), k: int) -> bool:
    pass


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
