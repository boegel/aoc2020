#!/usr/bin/env python3
import copy
import sys

if len(sys.argv) != 2:
    sys.stderr.write("ERROR: Usage: %s <input>\n" % sys.argv[0])
    sys.exit(1)

input_file = sys.argv[1]
with open(input_file, 'r') as fp:
    input_txt = fp.read()


def apply_rules(seat_rows):
    orig_seat_rows = copy.deepcopy(seat_rows)

    n_rows = len(seat_rows)
    n_cols = len(seat_rows[0])

    for i in range(n_rows):
        if i > 0:
            prev_row = orig_seat_rows[i - 1]
        else:
            prev_row = None

        if i + 1 < n_rows:
            next_row = orig_seat_rows[i + 1]
        else:
            next_row = None

        for j in range(n_cols):

            if j == 0:
                left, right = 0, 1
            elif j == n_cols - 1:
                left, right = j - 1, j
            else:
                left, right = j - 1, j + 1

            cnt = 0
            if prev_row:
                cnt += len([x for x in prev_row[left:right+1] if x == '#'])
            if j != left and orig_seat_rows[i][j-1] == '#':
                cnt += 1
            if j != right and orig_seat_rows[i][j+1] == '#':
                cnt += 1
            if next_row:
                cnt += len([x for x in next_row[left:right+1] if x == '#'])

            seat = orig_seat_rows[i][j]
            if seat == 'L' and cnt == 0:
                seat_rows[i][j] = '#'
            elif seat == '#' and cnt >= 4:
                seat_rows[i][j] = 'L'


def show(seat_rows):
    for row in seat_rows:
        print(''.join(row))


seat_rows = [list(x) for x in input_txt.splitlines()]
show(seat_rows)

prev = []
idx = 0
while prev != seat_rows:
    prev = copy.deepcopy(seat_rows)
    apply_rules(seat_rows)
    print("\nafter pass #%d:\n" % idx)
    show(seat_rows)
    idx += 1

print("first half: %d" % len([x for row in seat_rows for x in row if x == '#']))
