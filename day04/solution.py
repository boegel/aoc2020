#!/usr/bin/env python3
import re
import sys


def parse_int(val):
    try:
        year = int(val)
    except ValueError:
        year = 0

    return year


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
    if line == '':
        keys = list(passport.keys())
        if all(k in keys for k in req_keys):
            valid_cnt += 1

        passport = {}
    else:
        passport.update(dict(tuple(x.split(':')) for x in line.split(' ')))

print("solution first half: %s" % valid_cnt)


valid_cnt = 0

passport = {}
for line in lines + ['']:
    if line == '':
        from pprint import pprint
        pprint(passport)

        keys = list(passport.keys())
        if all(k in keys for k in req_keys):

            valid = True
            if not (1920 <= parse_int(passport['byr']) <= 2002):
                valid = False
                print("invalid byr")
            if not (2010 <= parse_int(passport['iyr']) <= 2020):
                valid = False
                print("invalid iyr")
            if not (2020 <= parse_int(passport['eyr']) <= 2030):
                valid = False
                print("invalid eyr")

            hgt = passport['hgt']
            if hgt.endswith('cm'):
                if not (150 <= parse_int(hgt[:-2]) <= 193):
                    valid = False
                    print("invalid hgt (cm)")
            elif hgt.endswith('in'):
                if not (59 <= parse_int(hgt[:-2]) <= 76):
                    valid = False
                    print("invalid hgt (in)")
            else:
                valid = False
                print("invalid hgt")

            if not re.match('^#[0-9a-f]{6}$', passport['hcl']):
                print("invalid hcl")
                valid = False

            if passport['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                print("invalid ecl")
                valid = False

            if not re.match('^[0-9]{9}$', passport['pid']):
                print("invalid pid")
                valid = False

            if valid:
                valid_cnt += 1
        else:
            print("invalid!")

        passport = {}
    else:
        passport.update(dict(tuple(x.split(':')) for x in line.split(' ')))

print("solution second half: %s" % valid_cnt)
