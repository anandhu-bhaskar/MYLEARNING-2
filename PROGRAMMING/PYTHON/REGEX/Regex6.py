# use of * for appearance of some pattern o or more than zero

import re


bat_regex = re.compile(r"bat(wo)*man")
mo = bat_regex.search("I am batwowowowoman")
mo2 = bat_regex.search("I am batman")

# compare with previous one

# if we want to check occurrence of multiple repetitions: then us * character

print(mo.group())
print(mo2.group())