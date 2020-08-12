import re

# notice the use of pipe character below
bat_regex = re.compile(r'bat(man|mobile|women)')
mo = bat_regex.findall("I am batman vs batwomen")

print(type(mo))

for i in mo:
    print(i)

