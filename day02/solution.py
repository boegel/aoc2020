#!/usr/bin/env python3
import sys

if len(sys.argv) != 2:
    sys.stderr.write("ERROR: Usage: %s <input>\n" % sys.argv[0])
    sys.exit(1)

input_file = sys.argv[1]
with open(input_file, 'r') as fp:
    input_txt = fp.read()

valid_cnt_part1 = 0
parsed_entries = []

for line in input_txt.splitlines():
    policy, rest = line.split(' ', 1)
    min_cnt, max_cnt = (int(x) for x in policy.split('-'))

    letter, password = rest.split(':')
    password = password.lstrip()

    parsed_entries.append((min_cnt, max_cnt, letter, password))

    if min_cnt <= password.count(letter) <= max_cnt:
        valid_cnt_part1 += 1

print("solution part 1: %d" % valid_cnt_part1)

#############################################################

valid_cnt_part2 = 0

for (idx1, idx2, letter, password) in parsed_entries:
    if password[idx1-1] == letter and password[idx2-1] != letter:
        valid_cnt_part2 += 1
    if password[idx1-1] != letter and password[idx2-1] == letter:
        valid_cnt_part2 += 1

print("solution part 2: %d" % valid_cnt_part2)
