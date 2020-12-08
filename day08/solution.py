#!/usr/bin/env python3
import sys

if len(sys.argv) != 2:
    sys.stderr.write("ERROR: Usage: %s <input>\n" % sys.argv[0])
    sys.exit(1)

input_file = sys.argv[1]
with open(input_file, 'r') as fp:
    input_txt = fp.read()


code = []
for line in input_txt.splitlines():
    instr, val = line.split(' ')
    val = int(val)
    print(instr, val)
    code.append((False, instr, val))

orig_code = code[:]


acc = 0
idx = 0
visited, instr, val = code[idx]
while(not visited):

    code[idx] = (True, instr, val)

    if instr in ['acc', 'nop']:
        idx += 1
    if instr == 'acc':
        acc += val

    if instr == 'jmp':
        idx += val

    visited, instr, val = code[idx]

print("acc (first half): %s" % acc)

for change_idx in range(0, len(orig_code)):

    print("change_idx: %s" % change_idx)
    code = orig_code[:]

    visited, instr, val = code[change_idx]
    if instr == 'jmp':
        code[change_idx] = (visited, 'nop', val)
        print("tweaked code[%s]: %s (was %s)" % (change_idx, code[change_idx], orig_code[change_idx]))
    elif instr == 'nop':
        code[change_idx] = (visited, 'jmp', val)
        print("tweaked code[%s]: %s (was %s)" % (change_idx, code[change_idx], orig_code[change_idx]))

    acc = 0
    idx = 0
    visited, instr, val = code[idx]
    while(not visited and idx < len(code)):

        code[idx] = (True, instr, val)

        if instr in ['acc', 'nop']:
            idx += 1
        if instr == 'acc':
            acc += val

        if instr == 'jmp':
            idx += val

        if idx < len(code):
            visited, instr, val = code[idx]

    if idx == len(code):
        print("acc (second half): %s" % acc)
        break
