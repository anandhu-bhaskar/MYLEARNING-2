# Non-Greedy Matching


# to make it non greedy - just add a ? to the prevs pgrm

import re

num_regex = re.compile(r"\d{3,5}?")

# this will cause to program to match for the minimum no: of times

mo = num_regex.search("hello from greedy matching - 12345")

print(mo.group())

#  now check variations

num_regex2 = re.compile(r"\d{3,5}")

mo2 = num_regex2.search("hello from greedy matching - 12345")

print(mo2.group())

######################################### output -3

num_regex3 = re.compile(r"\d{,5}")

mo3 = num_regex3.search("hello from greedy matching - 12345")

print(mo3.group()) # blank output coz 0 matching is allowed

######################################### output -4

num_regex4 = re.compile(r"\d{1,}")

mo4 = num_regex4.search("hello from greedy matching - 123457895454545445544")

print(mo4.group()) # blank output coz 0 matching is allowed




