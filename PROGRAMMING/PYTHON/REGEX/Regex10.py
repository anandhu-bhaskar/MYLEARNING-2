# Greedy Matching


# Curly braces are mostly used in detecting number patterns

import re

num_regex = re.compile(r"\d{3,5}")

mo = num_regex.search("hello from greedy matching - 12345")

print(mo.group())

# if we see check the output : it has matched all the values. instead it could have matched only the
# first 3 considering the minumum match specified is only 3