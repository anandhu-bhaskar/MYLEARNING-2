# find and extract all phone numbers in a sentence


message = "call me at 641-2314-225 or 641-2314-225"


def extract_nums(text):
    import re
    ph_num_regex = re.compile(r'\d\d\d-\d\d\d\d-\d\d\d')


    # search is used to find only one item
    # mo = ph_num_regex.search(text)
    # print(mo.group())

    return ph_num_regex.findall(text)


print(extract_nums(message))
