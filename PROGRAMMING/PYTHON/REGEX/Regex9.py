# Curly braces are mostly used in detecting number patterns
# detect and print numbers in Canada

import re

# max occurance allowed : 5 , minimum occurance: 3
bat_regex = re.compile(r"((\d\d\d-)?\d\d\d\-\d\d\d\d(,)?){3}")

# Meaning area code is optional, must be seperated with comams and cann occur max :3

mo = bat_regex.search("Batmans Contact : 777-888-9898,898-858-6633,222-3232") # last num no area code

print(mo.group())