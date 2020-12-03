#!/usr/bin/env python3
import sys

from collections import namedtuple

if len(sys.argv) != 2:
    sys.stderr.write("ERROR: Usage: %s <input>\n" % sys.argv[0])
    sys.exit(1)

input_file = sys.argv[1]
with open(input_file, 'r') as fp:
    input_txt = fp.read()

Slope = namedtuple('Slope', ['right', 'down'])
slope = Slope(3, 1)

col, row = 0, 0
trees = 0

for line in input_txt.splitlines()[1:]:
    col = (col + slope.right) % len(line)
    print(line)
    print(' ' * col + '^')
    if line[col] == '#':
        trees += 1

print(trees)
