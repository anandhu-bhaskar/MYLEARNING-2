# use of ? for appearance of some pattern (0 or 1) time

import re

# notice the use of ? character below indicating it may or may not cocur
bat_regex = re.compile(r"bat(wo)?man")  # detects whether a pattern occurs or not -precise
mo = bat_regex.search("I am batwoman")
mo2 = bat_regex.search("I am batman")

# try giving wowoman as input and will result in an error
# coz it can detect only one time

# if we want to check occurrence of multiple repetitions: then us * character : next pgrm

print(mo.group())
print(mo2.group())
