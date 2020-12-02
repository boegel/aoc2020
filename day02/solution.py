#!/usr/bin/env python3
import sys

if len(sys.argv) != 2:
    sys.stderr.write("ERROR: Usage: %s <input>\n" % sys.argv[0])
    sys.exit(1)

input_file = sys.argv[1]
with open(input_file, 'r') as fp:
    input_txt = fp.read()

valid_cnt = 0

for line in input_txt.splitlines():
    policy, rest = line.split(' ', 1)
    min_cnt, max_cnt = (int(x) for x in policy.split('-'))

    letter, password = rest.split(':')
    password = password.lstrip()

    if min_cnt <= password.count(letter) <= max_cnt:
        valid_cnt += 1

print(valid_cnt)
