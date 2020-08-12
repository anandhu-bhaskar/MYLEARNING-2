# if we want to detect a pattern for a specifc number of time, then use the following

import re

# max occurance allowed : 5 , minimum occurance: 3
bat_regex = re.compile(r"bat(wo){3,5}man")
mo = bat_regex.search("I am batwowowowoman")
# mo2 = bat_regex.search("I am batman")

print(mo.group())
# print(mo2.group())