#!/usr/bin/env python3
import sys

if len(sys.argv) != 2:
    sys.stderr.write("ERROR: Usage: %s <input>\n" % sys.argv[0])
    sys.exit(1)

input_file = sys.argv[1]
with open(input_file, 'r') as fp:
    input_txt = fp.read()

last = []
lines = list(input_txt.splitlines())

last_n = 25
while len(last) < last_n:
    last.append(int(lines.pop(0)))

sol = None
for line in lines:
    val = int(line)

    match = False
    for idx in range(last_n):
        x = last[idx]
        for y in last[idx+1:]:
            if val == x + y:
                match = True
                break
        if match:
            break

    if not match:
        sol = val
        break

    last.pop(0)
    last.append(val)

print("first half: %s" % sol)

lines = list(input_txt.splitlines())
contig = []
for line in lines:
    tot = sum(contig)
    if tot < sol:
        contig.append(int(line))

    while(sum(contig) > sol):
        contig.pop(0)

    if sum(contig) == sol:
        print("second half: %s" % (min(contig) + max(contig)))
