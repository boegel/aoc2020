#!/usr/bin/env python3
import re
import sys

if len(sys.argv) != 2:
    sys.stderr.write("ERROR: Usage: %s <input>\n" % sys.argv[0])
    sys.exit(1)

input_file = sys.argv[1]
with open(input_file, 'r') as fp:
    input_txt = fp.read()


def add_bags(bag_type):
    regex = re.compile("contain .* " + bag_type)
    for line in input_txt.splitlines():
        if regex.search(line):
            bag_type = ' '.join(line.split(' ')[:2])
            if bag_type not in bags:
                bags.add(bag_type)
                add_bags(bag_type)


bags = set()
add_bags("shiny gold")
print("bags containining shiny gold bags: %d" % len(bags))

cnt_bags_regex = re.compile("(?P<cnt>[0-9]+) (?P<type>[a-z]+ [a-z]+) bag(s)?")


def cnt_bags(bag_type):
    tot_cnt = 0
    regex = re.compile('^' + bag_type + " bags contain")
    for line in input_txt.splitlines():
        if regex.search(line):
            for cnt, new_bag_type, _ in cnt_bags_regex.findall(line):
                cnt = int(cnt)
                tot_cnt += cnt + cnt * cnt_bags(new_bag_type)
            return tot_cnt


print("bags contained in a shiny gold bag: %d" % cnt_bags("shiny gold"))
