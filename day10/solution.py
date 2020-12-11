#!/usr/bin/env python3
import sys

if len(sys.argv) != 2:
    sys.stderr.write("ERROR: Usage: %s <input>\n" % sys.argv[0])
    sys.exit(1)

input_file = sys.argv[1]
with open(input_file, 'r') as fp:
    input_txt = fp.read()

joltage_ratings = sorted([int(x) for x in input_txt.splitlines()])
print(joltage_ratings)

prev = 0
diffs = {
    1: 0,
    2: 0,
    3: 0,
}
for rat in joltage_ratings:
    diffs[rat - prev] += 1
    prev = rat

diffs[3] += 1

print(diffs)
print("first half: %s" % (diffs[1] * diffs[3]))

joltage_ratings = [0] + joltage_ratings

n = len(joltage_ratings)

counts = {}


def count(idx):
    cnt = 0

    if idx in counts:
        return counts[idx]

    if idx+1 < n:
        cnt += count(idx+1)
        if idx+2 < n and joltage_ratings[idx+2] - joltage_ratings[idx] <= 2:
            cnt += 1 + count(idx+2)
            if idx+3 < n and joltage_ratings[idx+3] - joltage_ratings[idx] <= 3:
                cnt += 1 + count(idx+3)

    counts[idx] = cnt
    return cnt


print("second half: %s" % (count(0)+1))
