# use of + for appearance of some pattern 1 or more than zero : atmost 1

import re

# if we execute the commented code, error, coz wo must appear atleast once
bat_regex = re.compile(r"bat(wo)+man")
mo = bat_regex.search("I am batwowowowoman")
# mo2 = bat_regex.search("I am batman")

# compare with previous one

# if we want to check occurrence of multiple repetitions: then us * character

print(mo.group())
# print(mo2.group())