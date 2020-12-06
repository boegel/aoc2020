#!/usr/bin/env python3
import sys


if len(sys.argv) != 2:
    sys.stderr.write("ERROR: Usage: %s <input>\n" % sys.argv[0])
    sys.exit(1)

input_file = sys.argv[1]
with open(input_file, 'r') as fp:
    input_txt = fp.read()

all_questions = set()
common_questions = None
tot_all = 0
tot_common = 0
for line in input_txt.splitlines() + ['']:
    print("line: %s" % line)
    if line == '':
        cnt = len(all_questions)
        print(all_questions)
        print(cnt)
        tot_all += cnt
        cnt = len(common_questions)
        print(common_questions)
        print(cnt)
        tot_common += cnt
        all_questions = set()
        common_questions = None
    else:
        all_questions = all_questions.union(set(line))
        print("union: %s" % all_questions)
        if common_questions is None:
            common_questions = set(line)
        else:
            common_questions = common_questions.intersection(set(line))
        print("intersect: %s" % common_questions)

print("count all: %s" % tot_all)
print("count common: %s" % tot_common)
