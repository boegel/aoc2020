#!/usr/bin/env python3
import re
import sys


if len(sys.argv) != 2:
    sys.stderr.write("ERROR: Usage: %s <input>\n" % sys.argv[0])
    sys.exit(1)

input_file = sys.argv[1]
with open(input_file, 'r') as fp:
    input_txt = fp.read()

max_seat_id = 0
for line in input_txt.splitlines():
    print(line)
    row_spec = line[:7]
    row_range = (0, 127)
    print(row_range)
    for char in row_spec:
        step = 1 + (row_range[1] - row_range[0]) // 2
        if char == 'F':
            row_range = (row_range[0], row_range[1] - step)
        elif char == 'B':
            row_range = (row_range[0] + step, row_range[1])
        else:
            raise ValueError
        print(char, row_range)

    assert row_range[0] == row_range[1]
    row = row_range[0]

    col_spec = line[7:]
    col_range = (0, 7)
    for char in col_spec:
        step = 1 + (col_range[1] - col_range[0]) // 2
        if char == 'L':
            col_range = (col_range[0], col_range[1] - step)
        elif char == 'R':
            col_range = (col_range[0] + step, col_range[1])
        else:
            raise ValueError
        print(char, col_range)

    assert col_range[0] == col_range[1]
    col = col_range[0]

    seat_id = row * 8 + col
    print(row, col, ' => ', seat_id)
    if seat_id > max_seat_id:
        max_seat_id = seat_id

print(max_seat_id)
