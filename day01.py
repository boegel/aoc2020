#!/usr/bin/env python3
import sys

if len(sys.argv) != 2:
    sys.stderr.write("ERROR: Usage: %s <input>\n" % sys.argv[0])
    sys.exit(1)

input_file = sys.argv[1]
with open(input_file, 'r') as fp:
    input_txt = fp.read()

entries = [int(x.strip()) for x in input_txt.splitlines()]

solution_pair = None
for id1, entry1 in enumerate(entries):
    for entry2 in entries[id1+1:]:
        if entry1 + entry2 == 2020:
            solution_pair = (entry1, entry2)
            break
    if solution_pair:
        break

if solution_pair:
    print("%d * %d = %d" % (entry1, entry2, entry1 * entry2))
else:
    sys.stderr.write("No solution pair found?!\n")
    sys.exit(1)

solution_triple = None
for id1, entry1 in enumerate(entries):
    for id2, entry2 in enumerate(entries[id1+1:]):
        for entry3 in entries[id1+id2+2:]:
            if entry1 + entry2 + entry3 == 2020:
                solution_triple = (entry1, entry2, entry3)
                break
        if solution_triple:
            break
    if solution_triple:
        break

if solution_triple:
    print("%d * %d * %d = %d" % (entry1, entry2, entry3, entry1 * entry2 * entry3))
else:
    sys.stderr.write("No solution triple found?!\n")
    sys.exit(1)
