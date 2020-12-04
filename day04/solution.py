#!/usr/bin/env python3
import sys

if len(sys.argv) != 2:
    sys.stderr.write("ERROR: Usage: %s <input>\n" % sys.argv[0])
    sys.exit(1)

input_file = sys.argv[1]
with open(input_file, 'r') as fp:
    input_txt = fp.read()

lines = input_txt.splitlines()

valid_cnt = 0
req_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']  # 'cid' is optional

passport = {}
for line in lines + ['']:
    print("line: " + line)
    if line == '':
        from pprint import pprint
        pprint(passport)

        keys = list(passport.keys())
        if all(k in keys for k in req_keys):
            valid_cnt += 1
        else:
            print("invalid!")

        passport = {}
    else:
        passport.update(dict(tuple(x.split(':')) for x in line.split(' ')))

print(valid_cnt)
