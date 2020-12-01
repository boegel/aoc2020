#!/usr/bin/env python3
import sys

if len(sys.argv) != 2:
    sys.stderr.write("ERROR: Usage: %s <input>\n" % sys.argv[0])
    sys.exit(1)

input_file = sys.argv[1]
with open(input_file, 'r') as fp:
    input_txt = fp.read()

entries = [int(x.strip()) for x in input_txt.splitlines()]

for id1, entry1 in enumerate(entries):
    for entry2 in entries[id1+1:]:
        if entry1 + entry2 == 2020:
            print("%d * %d = %d" % (entry1, entry2, entry1 * entry2))
            sys.exit(0)

sys.stderr.write("No solution found?!\n")
sys.exit(1)
