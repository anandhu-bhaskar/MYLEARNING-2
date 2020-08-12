# Check if the given text is a phone number

# 415-9999-414

import re

def isphonenum(text):
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 8):
        if not text[i].isdecimal():
            return False
    if text[8] != '-':
        return False
    for i in range(9, 12):
        if not text[i].isdecimal():
            return False
    return True

# the same can be checked using regex as :

def chk_phne(text):
    ph_no_regex = re.compile(r'\d\d\d-\d\d\d\d-\d\d\d')
    if ph_no_regex.search(text):
        # mo = ph_no_regex.search(text) #to print extracted pattern - match object
        # print(mo.group())
        return True
    else:
        return False


num1 = '415-9999-414'
num2 = 'ass15-9999-414'

print(f"Test {num1} using regex:",chk_phne(num1))
print(f"Test {num2} using regex:",chk_phne(num2))
print(f"Test {num1} using normal:",isphonenum(num1))
print(f"Test {num2} using normal:",isphonenum(num2))