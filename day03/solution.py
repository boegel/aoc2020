#!/usr/bin/env python3
import sys


if len(sys.argv) != 2:
    sys.stderr.write("ERROR: Usage: %s <input>\n" % sys.argv[0])
    sys.exit(1)

input_file = sys.argv[1]
with open(input_file, 'r') as fp:
    input_txt = fp.read()

lines = input_txt.splitlines()


def check_slope(right, down, verbose=False):
    col = 0
    row = down
    trees = 0
    while row < len(lines):
        line = lines[row]

        col = (col + right) % len(line)
        if verbose:
            print(line)
            print(' ' * col + '^')

        if line[col] == '#':
            trees += 1

        row += down

    return trees


# first half: 3 right, 1 down
print("first half (3 right, 1 down): %s" % check_slope(3, 1))

# second half
print("second half")
product = 1
for (right, down) in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
    trees = check_slope(right, down)
    print("%d right, %d down: %s" % (right, down, trees))
    product *= trees

print("product: %d" % product)
